"""Feature Key Module."""
from __future__ import annotations

from enum import Enum
from itertools import chain
from typing import Any, Iterable

from datasets.features.features import Features, FeatureType, Sequence
from datasets.iterable_dataset import _batch_to_examples
from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from .feature_checks import (
    check_feature_equals,
    get_sequence_feature,
    get_sequence_length,
    raise_feature_equals,
    raise_feature_is_sequence,
)


def _iter_keys_in_features(
    features: FeatureType, max_depth: int, max_seq_len_to_unpack: int
) -> Iterable[tuple[str | int | slice]]:
    """Internal helper function.

    Iterate through all sub-feature keys of a given feature.
    """
    if max_depth == 0:
        # trivial case, maximum depth reached
        yield tuple()

    elif isinstance(features, (dict, Features)):
        # recursivly flatten all features in mapping and
        # prefix each sub-key with the current key of the mapping
        yield from chain.from_iterable(
            (
                map(
                    (k,).__add__,
                    _iter_keys_in_features(
                        v, max_depth - 1, max_seq_len_to_unpack
                    ),
                )
                for k, v in features.items()
            )
        )

    elif isinstance(features, Sequence):
        length = get_sequence_length(features)
        # only unpack sequences of fixed length
        if 0 < length < max_seq_len_to_unpack:
            yield from (
                (i,) + sub_key
                for sub_key in _iter_keys_in_features(
                    get_sequence_feature(features),
                    max_depth - 1,
                    max_seq_len_to_unpack,
                )
                for i in range(length)
            )

        else:
            yield from map(
                (slice(None),).__add__,
                _iter_keys_in_features(
                    get_sequence_feature(features),
                    max_depth - 1,
                    max_seq_len_to_unpack,
                ),
            )

    else:
        # all other feature types are considered primitive/unpackable
        yield tuple()


class FeatureKey(tuple[str | int | slice]):
    """Feature Key used to index features and examples.

    Arguments:
        *key (str | int | slice): key entries
    """

    @classmethod
    def from_tuple(self, key: tuple[str | int | slice]) -> FeatureKey:
        """Generate a feature key from a tuple.

        Arguments:
            key (tuple[str|int|slice]): key entries

        Returns:
            key (FeatureKey): feature key
        """
        return FeatureKey(*key)

    def __new__(self, *key: str | int | slice) -> None:
        """Instantiate a new feature key.

        Arguments:
            *key (tuple[str|int|slice]): key entries
        """
        if len(key) == 1 and isinstance(key[0], tuple):
            return FeatureKey.from_tuple(key[0])

        if len(key) > 0 and not isinstance(key[0], str):
            raise ValueError(
                "First entry of a feature key must be a string, got %s."
                % repr(key[0])
            )

        # unpack enums
        key = tuple(k.value if isinstance(k, Enum) else k for k in key)

        for key_entry in key:
            if not isinstance(key_entry, (str, int, slice)):
                raise TypeError(
                    "Feature key entries must be either str, int or slice "
                    "objects, got %s" % key_entry
                )

        return tuple.__new__(FeatureKey, key)

    def __getitem__(self, idx) -> FeatureKey | str | int | slice:
        """Get specific key entries of the feature key."""
        if isinstance(idx, slice) and (
            (idx.start == 0) or (idx.start is None)
        ):
            return FeatureKey(*super(FeatureKey, self).__getitem__(idx))
        return super(FeatureKey, self).__getitem__(idx)

    def __str__(self) -> str:
        """String representation of the feature key."""
        return "FeatureKey(%s)" % "->".join(map(repr, self))

    def __repr__(self) -> str:
        """String representation of the feature key."""
        return str(self)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        """Integrate feature key with pydantic."""
        return core_schema.no_info_after_validator_function(
            cls, handler(str | tuple)
        )

    @property
    def is_simple(self) -> bool:
        """Check whether the feature key is simple.

        A feature key is considered simple if it only consists of
        strings or full slices.

        The concept behind a simple key is that is only
        indexes dictionaries or sequences but not just a slice of it.

        It does not require fancy sequence slicing. Also modifying
        the value at the key modifies the full feature and not just
        a part of it.

        As a counter example consider the following complex keys

            - ("A", 0, "B")
            - ("A", slice(4, 10), "B")

        Both incorporate indexing a sequence feature and modifying it
        would only modify a specific value or sub-area of the sequence.

        Returns:
            is_simple (bool): boolean indicating whether the key is simple
        """
        return all(
            isinstance(k, str) or (isinstance(k, slice) and k == slice(None))
            for k in self
        )

    def raise_is_simple(self) -> None:
        """Check whether a given feature key is simple.

        A feature key is considered simple if it only consists of
        strings.

        Raises:
            exc (TypeError): when the given key is complex
        """
        if not self.is_simple:
            raise TypeError("Expected simple key, got %s" % str(str))

    def cutoff_at_slice(self) -> FeatureKey:
        """Cutoff given key at first occurance of a slice.

        Consider the following example:

            FeatureKey("A", "B", 0, "C", slice(-1), "D")
                => FeatureKey("A", "B", 0, "C")

        Returns:
            cut_key (FeatureKey):
                truncated key guaranteed to not contain a slice
        """
        # find slice in key
        for i, k in enumerate(self):
            if isinstance(k, slice):
                # cutoff before slice
                return self[:i]

        # no slice detected
        return self

    @property
    def simple_subkey(self) -> FeatureKey:
        """Get simple subkey of the feature key.

        Consider the following example:

            FeatureKey("A", "B", 0, "C", slice(-1), "D")
                => FeatureKey("A", "B")

        Returns:
            simple_subkey (FeatureKey):
                truncated key guaranteed to be simple
        """
        for i in range(2, len(self)):
            if not self[:i].is_simple:
                return self[: i - 1]

        # full key is simple
        return self

    def index_features(self, features: Features) -> FeatureType:
        """Get the feature type of the feature indexed by the key.

        Arguments:
            features (Features):
                The feature mapping to index with the given key.

        Returns:
            feature (FeatureType):
                the extracted feature type at the given key.
        """
        for i, key_entry in enumerate(self):
            if isinstance(key_entry, str):
                # check feature type
                raise_feature_equals(self[:i], features, [Features, dict])
                # check key entry is present in features
                if key_entry not in features.keys():
                    raise KeyError(
                        "Key `%s` not present in features at `%s`, "
                        "valid keys are %s"
                        % (key_entry, self[:i], list(features.keys()))
                    )
                # get the feature at the key entry
                features = features[key_entry]

            elif isinstance(key_entry, (int, slice)):
                # check feature type
                raise_feature_is_sequence(self[:i], features)
                # get sequence feature and length
                length = get_sequence_length(features)
                features = get_sequence_feature(features)

                if isinstance(key_entry, int) and (
                    (length == 0) or ((length > 0) and (key_entry >= length))
                ):
                    raise IndexError(
                        "Index `%i` out of bounds for sequence of "
                        "length `%i` of feature at key %s"
                        % (key_entry, length, self[:i])
                    )

                if isinstance(key_entry, slice):
                    if length >= 0:
                        # get length of reminaing sequence after slicing
                        start, stop, step = key_entry.indices(length)
                        length = (stop - start) // step

                    # get features and pack them into a sequence of
                    # appropriate length
                    key = tuple.__new__(FeatureKey, self[i + 1 :])
                    return Sequence(
                        key.index_features(features), length=length
                    )

        return features

    def index_example(self, example: dict[str, Any]) -> Any:
        """Index the example with the key and retrieve the value.

        Arguments:
            example (dict[str, Any]): The example to index.

        Returns:
            value (Any): the value of the example at the given key.
        """
        for i, key_entry in enumerate(self):
            if isinstance(key_entry, slice):
                assert isinstance(example, list)
                # recurse on all examples indexed by the slice
                # create a new subkey for recursion while avoiding
                # key checks asserting that the key must start with
                # a string entry
                key = tuple.__new__(FeatureKey, self[i + 1 :])
                return list(map(key.index_example, example[key_entry]))

            # index the example
            example = example[key_entry]

        return example

    def index_batch(self, batch: dict[str, list[Any]]) -> list[Any]:
        """Index batch.

        Index a batch of examples with the given key and retrieve
        the batch of values.

        Arguments:
            batch (dict[str, list[Any]]): Batch of example to index.

        Returns:
            values (list[Any]):
                the batch of values of the example at the given key.
        """
        return FeatureKey(self[0], slice(None), *self[1:]).index_example(batch)

    def remove_from_features(self, features: Features) -> Features:
        """Remove a feature from a feature mapping.

        Arguments:
            features (Features): features to remove the feature from

        Returns:
            remaining_features (Features): the remaining features
        """
        if not self[:-1].is_simple:
            raise ValueError(
                "Can only remove from feature at simple key, "
                "got `%s`" % self
            )

        container = self[:-1].index_features(features)
        num_slices = sum(isinstance(k, slice) for k in self[:-1])

        # unpack nested sequences coming from slicing
        for _ in range(num_slices):
            container = get_sequence_feature(container)

        # get the key to remove
        key_to_remove = self[-1]

        if isinstance(key_to_remove, str):
            # check key entry is present in features
            if key_to_remove not in container.keys():
                raise KeyError(
                    "Key `%s` not present in feature mapping at "
                    "path `%s`, valid keys are %s"
                    % (key_to_remove, self[:-1], list(container.keys()))
                )
            # remove
            container.pop(key_to_remove)

        elif isinstance(key_to_remove, (int, slice)):
            # get the length of the sequence
            length = get_sequence_length(container)

            if isinstance(key_to_remove, int):
                # check if index is out of bounds
                if (length == 0) or (
                    (length > 0) and (key_to_remove >= length)
                ):
                    raise IndexError(
                        "Index `%i` out of bounds for sequence of "
                        "length `%i` of feature at key %s"
                        % (key_to_remove, length, self[:-1])
                    )

                # only sequence has length information
                if isinstance(container, Sequence) and (length > 0):
                    container.length = length - 1

            elif isinstance(key_to_remove, slice):
                # only sequence has length information
                if isinstance(container, Sequence) and (length > 0):
                    # get length of reminaing sequence after slicing
                    start, stop, step = key_to_remove.indices(length)
                    container.length = length - ((stop - start) // step)
                    assert container.length >= 0

        return features

    def remove_from_example(self, example: dict[str, Any]) -> dict[str, Any]:
        """Remove a feature from a given example.

        Arguments:
            example (dict[str, Any]): example

        Returns:
            remaining_example (dict[str, Any]): remaining example
        """
        if not self[:-1].is_simple:
            raise ValueError(
                "Can only remove from feature at simple key, "
                "got `%s`" % self
            )

        container = self[:-1].index_example(example)
        num_slices = sum(isinstance(k, slice) for k in self[:-1])

        # make container iterable when there is not slicing involved
        if num_slices == 0:
            container = [container]

        # flatten nested in case of multiple slicing operations
        for _ in range(num_slices - 1):
            container = chain.from_iterable(container)

        # get the key to remove
        key_to_remove = self[-1]

        if isinstance(key_to_remove, (str, int)):
            for item in container:
                item.pop(key_to_remove)

        elif isinstance(key_to_remove, slice):
            for item in container:
                start, stop, step = key_to_remove.indices(len(item))
                for i in reversed(range(start, stop, step)):
                    item.pop(i)

        return example

    def remove_from_batch(
        self, batch: dict[str, list[Any]]
    ) -> dict[str, list[Any]]:
        """Remove a feature from a given batch.

        Arguments:
            batch (dict[str, list[Any]]): batch

        Returns:
            remaining_batch (dict[str, list[Any]]): remaining batch
        """
        if len(self) == 1:
            return self.remove_from_example(batch)

        return FeatureKey(self[0], slice(None), *self[1:]).remove_from_example(
            batch
        )

    @classmethod
    def iter_keys_in_features(
        cls,
        features: Features,
        max_depth: int = -1,
        max_seq_len_to_unpack: int = 8,
    ) -> Iterable[FeatureKey]:
        """Iterate over all keys present in the given features.

        Take for example the following feature mapping

            {
                "A": {"B": Value("string")},
                "X": Sequence(Value("int32"), length=2)
            }

        Then the iterator would yield the following keys

            ("A", "B"), ("X", 0), ("X", 1)

        Arguments:
            features (FeatureType): features to build the keys for
            max_depth (int):
                when set to a positive integer, the nested structure
                of the feature mapping will only be traversed to the
                specified depth. The maximum length of each key is
                restricted by that value. Defaults to -1.
            max_seq_len_to_unpack (int):
                upper threshold of length to flatten sequences. If the
                sequence length exceeds that threshold, the sequence
                will not be flattened

        Returns:
            keys (Iterable[FeatureKey]): iterator over keys
        """
        return map(
            FeatureKey.from_tuple,
            _iter_keys_in_features(features, max_depth, max_seq_len_to_unpack),
        )


_FeatureKeyCollectionValue = (
    FeatureKey
    | list["_FeatureKeyCollectionValue"]
    | dict[str, "_FeatureKeyCollectionValue"]
)


def _convert_to_feature_keys(
    col: _FeatureKeyCollectionValue | str | tuple[str | int | slice],
) -> _FeatureKeyCollectionValue:
    """Internal helper function."""
    if isinstance(col, dict):
        return {k: _convert_to_feature_keys(v) for k, v in col.items()}
    if isinstance(col, list):
        return list(map(_convert_to_feature_keys, col))
    if isinstance(col, tuple):
        return FeatureKey.from_tuple(col)
    if not isinstance(col, FeatureKey):
        return FeatureKey(col)

    raise ValueError()


def _collect_from_example(
    col: _FeatureKeyCollectionValue, example: dict[str, Any]
) -> Any:
    """Internal helper function."""
    if isinstance(col, FeatureKey):
        return col.index_example(example)
    if isinstance(col, dict):
        return {
            key: _collect_from_example(val, example)
            for key, val in col.items()
        }
    if isinstance(col, list):
        return [_collect_from_example(x, example) for x in col]

    raise ValueError()


class FeatureKeyCollection(dict[str, _FeatureKeyCollectionValue]):
    """Feature Key Collection.

    Represents a (nested) collection of feature keys in the form of
    a dictionary on the top-level but can include lists in nested
    structures.
    """

    def __init__(
        self, collection: dict[str, _FeatureKeyCollectionValue] = {}
    ) -> None:
        """Instantiate new feature key collection.

        Arguments:
            collection (dict[str, _FeatureKeyCollectionValue]):
                feature key collection
        """
        dict.__init__(self, _convert_to_feature_keys(collection))

    def __setitem__(self, idx: str, val: _FeatureKeyCollectionValue) -> None:
        """Set value in collection.

        Arguments:
            idx (str): string index key
            val (_FeatureKeyCollectionValue): new value
        """
        super(FeatureKeyCollection, self).__setitem__(
            idx, _convert_to_feature_keys(val)
        )

    @classmethod
    def from_feature_keys(
        self, feature_keys: Iterable[FeatureKey]
    ) -> FeatureKeyCollection:
        """Build a feature collection from a list of feature keys.

        The resulting feature collection matches the format of the
        feature keys, i.e. the feature keys apply to the collection.

        Take for example to following feature keys:

            FeatureKey("A", "X")
            FeatureKey("A", "Y")

        Then the resulting feature collection would be:

            FeatureKeyCollection({"A": {"X": ("A", "X"), "Y": ("A", "Y")}})

        Arguments:
            feature_keys (Iterable[FeatureKey]):
                iterable of feature keys to build a collection from

        Returns:
            collection (FeatureCollection):
                resulting feature collection
        """
        collection = FeatureKeyCollection()

        for key in feature_keys:
            c = collection
            # add all sub-entries
            for key_entry in key[:-1]:
                if not isinstance(key_entry, str):
                    raise NotImplementedError()
                if key_entry not in c:
                    c[key_entry] = {}
                c = c[key_entry]
            # set key
            c[key[-1]] = key

        return collection

    def __str__(self) -> str:
        """String representation of the feature key collection."""
        return "FeatureKeyCollection(%s)" % str(dict(self))

    def __repr__(self) -> str:
        """String representation of the feature key collection."""
        return str(self)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        """Integrate feature key with pydantic."""
        return core_schema.no_info_after_validator_function(cls, handler(dict))

    @property
    def feature_keys(self) -> Iterable[FeatureKey]:
        """Iterator over all feature keys listed in the collection."""

        def _iter_feature_keys(col: _FeatureKeyCollectionValue):
            if isinstance(col, FeatureKey):
                yield col
            elif isinstance(col, dict):
                yield from chain.from_iterable(
                    map(_iter_feature_keys, col.values())
                )
            elif isinstance(col, list):
                yield from chain.from_iterable(map(_iter_feature_keys, col))

        yield from _iter_feature_keys(self)

    def collect_features(self, features: Features) -> Features:
        """Collect features.

        Collect all features requested in the feature collection
        and maintain the format of the collection.

        Arguments:
            features (Features):
                source feature mapping from which to collect the requested
                features

        Returns:
            collected_features (Features):
                collected features in the format of the feature key collection
        """

        def _collect(v):
            if isinstance(v, FeatureKey):
                return v.index_features(features)
            if isinstance(v, dict):
                return FeatureKeyCollection.collect_features(v, features)
            if isinstance(v, list):
                assert len(v) > 0
                # collect all features in specified in the list
                collected_features = map(_collect, v)
                f = next(collected_features)
                # make sure the feature types match
                for ff in collected_features:
                    if not check_feature_equals(f, ff):
                        raise TypeError(
                            "Expected all items of a sequence to be of the "
                            "same feature type, got %s != %s"
                            % (str(f), str(ff))
                        )
                return Sequence(f, length=len(v))

        return Features({key: _collect(val) for key, val in self.items()})

    def collect_values(self, example: dict[str, Any]) -> dict[str, Any]:
        """Collect Values.

        Collect all values requested by the feature collection
        and maintain the format of the collection.

        Arguments:
            example (dict[str, Any]):
                example from which to collect the requested values

        Returns:
            collected_values (dict[str, Any]):
                collected values in the format of the feature key collection
        """
        return _collect_from_example(self, example)

    def collect_batch(
        self, batch: dict[str, list[Any]]
    ) -> dict[str, list[Any]]:
        """Collect Batch.

        Collect all values from a batch of examples requested by the
        feature collection and maintain the format of the collection.

        Arguments:
            batch (dict[str, list[Any]]):
                example from which to collect the requested values

        Returns:
            collected_values (dict[str, list[Any]]):
                collected values in the format of the feature key collection
        """
        collected_batch = {key: [] for key in self.keys()}
        for example in _batch_to_examples(batch):
            for key, col in self.items():
                collected_batch[key].append(
                    _collect_from_example(col, example)
                )

        return collected_batch
