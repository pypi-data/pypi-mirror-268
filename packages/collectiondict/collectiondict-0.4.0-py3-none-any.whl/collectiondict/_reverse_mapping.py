import typing as t
from collections import Counter

from ._collectiondict import collectiondict

_KeyT = t.TypeVar("_KeyT", bound=t.Hashable)
_HashableValueT = t.TypeVar("_HashableValueT", bound=t.Hashable)


# TODO Currently, the type annotations are not perfect. Due to the limited
# nature of Python's type annotations, it is not possible to specify the correct
# return type for the custom classes. Thus, custom classes are supported but the
# return type is not inferred to be the parent class.


@t.overload
def reverse_mapping(  # pragma: nocover
    clct: t.Type[Counter[_KeyT]],
    mapping: t.Mapping[_KeyT, _HashableValueT],
) -> dict[_HashableValueT, Counter[_KeyT]]: ...


@t.overload
def reverse_mapping(  # pragma: nocover
    clct: t.Type[frozenset[_KeyT]], mapping: t.Mapping[_KeyT, _HashableValueT]
) -> dict[_HashableValueT, frozenset[_KeyT]]: ...


@t.overload
def reverse_mapping(  # pragma: nocover
    clct: t.Type[list[_KeyT]], mapping: t.Mapping[_KeyT, _HashableValueT]
) -> dict[_HashableValueT, list[_KeyT]]: ...


@t.overload
def reverse_mapping(  # pragma: nocover
    clct: t.Type[tuple[_KeyT, ...]], mapping: t.Mapping[_KeyT, _HashableValueT]
) -> dict[_HashableValueT, tuple[_KeyT, ...]]: ...


@t.overload
def reverse_mapping(  # pragma: nocover
    clct: t.Type[set[_KeyT]], mapping: t.Mapping[_KeyT, _HashableValueT]
) -> dict[_HashableValueT, set[_KeyT]]: ...


def reverse_mapping(
    clct: t.Union[
        t.Type[Counter[_KeyT]],
        t.Type[frozenset[_KeyT]],
        t.Type[list[_KeyT]],
        t.Type[set[_KeyT]],
        t.Type[tuple[_KeyT, ...]],
    ],
    mapping: t.Mapping[_KeyT, _HashableValueT],
) -> t.Union[
    dict[_HashableValueT, Counter[_KeyT]],
    dict[_HashableValueT, frozenset[_KeyT]],
    dict[_HashableValueT, list[_KeyT]],
    dict[_HashableValueT, set[_KeyT]],
    dict[_HashableValueT, tuple[_KeyT, ...]],
]:
    """
    Reverse mapping to map from values to keys

    Given a mapping, e.g. a dictionary, from keys to values, this function
    reverses the mapping so it maps from values to keys. The keys are collected
    in a collection specified by `clct`.

    Examples:
    ---------
    Simple usage using `set`:
    >>> reverse_mapping(set, {1: "foobar", 2: "blablubb", 3: "foobar"})
    {'foobar': {1, 3}, 'blablubb': {2}}

    Usage using `frozenset` and a cast to have the best type inference:
    >>> import typing as t
    >>> clct = t.cast(t.Type[frozenset[int]], frozenset)
    >>> reverse_mapping(clct, {1: "foobar", 2: "blablubb", 3: "foobar"})
    {'foobar': frozenset({1, 3}), 'blablubb': frozenset({2})}
    """

    return collectiondict(clct, ((v, k) for k, v in mapping.items()))
