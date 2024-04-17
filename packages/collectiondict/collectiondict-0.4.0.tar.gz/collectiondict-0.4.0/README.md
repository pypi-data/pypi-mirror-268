# collectiondict - Create multidicts more easily

This package simplifies the creation of multimappings from various sources. It
provides the functions `collectiondict`, `reverse_mapping` and
`reverse_multimapping`. In all three cases the return value will be of type
`dict[_ValueT, Collection[_KeyT]]`.

All three functions expect the target collection to be provided as an argument.
The supported collections are fixed. Only the built-in collections `Counter`,
`frozenset`, `list`, `set`, and `tuple` as well as their subclasses are
supported. If a unsupported collection is passed, an exception is raised.
However, `mypy` will warn about it.

Due to the limits of Pythons type annotations, it is not possible to specify
the correct return type for the custom classes. Thus, custom classes are
supported but the return type is inferred to be the parent class (e.g. `set`),
as opposed to be the class passed in (e.g. `class MySet(set)`).

In order to have the best type inference, it is recommended to **cast** `clct_t`
to specify the value type. Passing a specialised collection class is **not**
supported currently. The examples show how to use a cast.


## collectiondict

Given any stream of key-value tuples, this function creates a multi-dictionary
which maps all values to the corresponding key. Thus, `collectiondict(clct,
stream)` is similar to `dict(stream)` but does not discard values. It is
conceptually similar to [multidict](https://pypi.org/project/multidict/) but
much broader with respect to the supported types.

The implementation tries to be memory efficient and performant. Therefore, it
is possible to use it on extremely large streams, as long as the end result
fits in memory. Thus, if a list of the stream consumes more than half of the
available memory, `collectiondict` can still be used. Furthermore, for
deduplicating collections, e.g. `set`, the stream could exceed available
memory, as long as the key-value pairs do not. One of the examples covers this
scenario.

Simple usage using `set`:

    >>> from collectiondict import collectiondict
    >>> collectiondict(set, [("a", 1), ("b", 2), ("a", 3)])
    {'a': {1, 3}, 'b': {2}}

Usage using `frozenset` and a cast to have the best type inference:

    >>> import typing as t
    >>> from collectiondict import collectiondict
    >>> clct = t.cast(t.Type[frozenset[int]], frozenset)
    >>> collectiondict(clct, [("a", 1), ("b", 2), ("a", 3)])
    {'a': frozenset({1, 3}), 'b': frozenset({2})}

Scenario that might exceed memory:

    >>> from collectiondict import collectiondict
    >>> N=1000  # could be humongous, e.g. 10**20
    >>> collectiondict(set, ((str(n%2), n%3) for n in range(N)))
    {'0': {0, 1, 2}, '1': {0, 1, 2}}


## reverse_mapping

Given a mapping, e.g. a dictionary, from keys to values, this function reverses
the mapping so it maps from values to keys. The keys are collected in a
collection specified by passing a constructor as argument.

Simple usage using `set`:

    >>> from collectiondict import reverse_mapping
    >>> reverse_mapping(set, {1: "foobar", 2: "blablubb", 3: "foobar"})
    {'foobar': {1, 3}, 'blablubb': {2}}

Usage using `frozenset` and a cast to have the best type inference:

    >>> import typing as t
    >>> from collectiondict import reverse_mapping
    >>> clct = t.cast(t.Type[frozenset[int]], frozenset)
    >>> reverse_mapping(clct, {1: "foobar", 2: "blablubb", 3: "foobar"})
    {'foobar': frozenset({1, 3}), 'blablubb': frozenset({2})}


## reverse_multimapping

Given a mapping, e.g. a dictionary, from keys to an iterable of values, this
function reverses the mapping so it maps from values to keys. The keys are
collected in a collection specified by passing a constructor as argument.

Simple usage using `set`:

    >>> from collectiondict import reverse_multimapping
    >>> reverse_multimapping(set, {1: "abc", 2: "bcd", 3: "a"})
    {'a': {1, 3}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2}}

Usage using `frozenset` and a cast to have the best type inference:

    >>> import typing as t
    >>> from collectiondict import reverse_multimapping
    >>> clct = t.cast(t.Type[frozenset[int]], frozenset)
    >>> reverse_multimapping(clct, {1: [13, 37], 2: [13, 42], 3: [42]})
    {13: frozenset({1, 2}), 37: frozenset({1}), 42: frozenset({2, 3})}

Since `reverse_multimapping` is its own inverse, there is also a nice roundtrip
behaviour:

    >>> import typing as t
    >>> from collectiondict import reverse_multimapping
    >>> start = {1: {13, 37}, 2: {13, 42}, 3: {42}}
    >>> reversed_ = reverse_multimapping(set, start)
    >>> roundtripped = reverse_multimapping(set, reversed_)
    >>> start == roundtripped
    True
