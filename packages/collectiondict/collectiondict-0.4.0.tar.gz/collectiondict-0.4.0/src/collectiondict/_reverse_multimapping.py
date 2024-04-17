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
def reverse_multimapping(  # pragma: nocover
    clct: t.Type[Counter[_KeyT]],
    mapping: t.Mapping[_KeyT, t.Iterable[_HashableValueT]],
) -> dict[_HashableValueT, Counter[_KeyT]]: ...


@t.overload
def reverse_multimapping(  # pragma: nocover
    clct: t.Type[frozenset[_KeyT]],
    mapping: t.Mapping[_KeyT, t.Iterable[_HashableValueT]],
) -> dict[_HashableValueT, frozenset[_KeyT]]: ...


@t.overload
def reverse_multimapping(  # pragma: nocover
    clct: t.Type[list[_KeyT]], mapping: t.Mapping[_KeyT, t.Iterable[_HashableValueT]]
) -> dict[_HashableValueT, list[_KeyT]]: ...


@t.overload
def reverse_multimapping(  # pragma: nocover
    clct: t.Type[tuple[_KeyT, ...]],
    mapping: t.Mapping[_KeyT, t.Iterable[_HashableValueT]],
) -> dict[_HashableValueT, tuple[_KeyT, ...]]: ...


@t.overload
def reverse_multimapping(  # pragma: nocover
    clct: t.Type[set[_KeyT]], mapping: t.Mapping[_KeyT, t.Iterable[_HashableValueT]]
) -> dict[_HashableValueT, set[_KeyT]]: ...


def reverse_multimapping(
    clct: t.Union[
        t.Type[Counter[_KeyT]],
        t.Type[frozenset[_KeyT]],
        t.Type[list[_KeyT]],
        t.Type[set[_KeyT]],
        t.Type[tuple[_KeyT, ...]],
    ],
    mapping: t.Mapping[_KeyT, t.Iterable[_HashableValueT]],
) -> t.Union[
    dict[_HashableValueT, Counter[_KeyT]],
    dict[_HashableValueT, frozenset[_KeyT]],
    dict[_HashableValueT, list[_KeyT]],
    dict[_HashableValueT, set[_KeyT]],
    dict[_HashableValueT, tuple[_KeyT, ...]],
]:
    """
    Reverse multimapping to map from values to keys

    Given a mapping, e.g. a dictionary, from keys to an iterable of values,
    this function reverses the mapping so it maps from values to keys. The
    keys are collected in a collection specified by `clct`.

    Examples:
    ---------
    Simple usage using `set`:
    >>> reverse_multimapping(set, {1: "abc", 2: "bcd", 3: "a"})
    {'a': {1, 3}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2}}

    Usage using `frozenset` and a cast to have the best type inference:
    >>> import typing as t
    >>> clct = t.cast(t.Type[frozenset[int]], frozenset)
    >>> reverse_multimapping(clct, {1: [13, 37], 2: [13, 42], 3: [42]})
    {13: frozenset({1, 2}), 37: frozenset({1}), 42: frozenset({2, 3})}
    """

    return collectiondict(
        clct, ((v, k) for k, values in mapping.items() for v in values)
    )
