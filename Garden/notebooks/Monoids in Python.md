```python trusted=true
from typing import TypeVar, Generic
from abc import ABCMeta, abstractmethod


T = TypeVar('T')


class Monoid(Generic[T], metaclass=ABCMeta):

    @property
    @abstractmethod
    def identity(self) -> T: pass

    @abstractmethod
    def compose(self, x: T, y: T) -> T: pass

Monoid
```

```python trusted=false
class IntMonoid(Monoid[int]):

    @property
    def identity(self):
        return 0

    def compose(self, x, y):
        return x + y
```

```python trusted=false
class StringMonoid(Monoid[str]):
    @property
    def identity(self):
        return ""

    def compose(self, x, y):
        return f"{y}{x}"
```

```python trusted=false
from hypothesis import given
from hypothesis.strategies import data, from_type
import pytest
from typing import get_args


monoids = [
    IntMonoid(),
    StringMonoid(),
]


@given(data())
@pytest.mark.parametrize("m", monoids)
def test_identity(m: Monoid[T], data):
    t = type(m.identity)

    x: T = data.draw(from_type(t))

    print(x, m.identity)
    assert x == m.compose(x, m.identity)
    assert x == m.compose(m.identity, x)


@given(data())
@pytest.mark.parametrize("m", monoids)
def test_composition(m, data):
    t = type(m.identity)

    x: T = data.draw(from_type(t))
    y: T = data.draw(from_type(t))
    assert type(m.compose(x, y)) == t


@given(data())
@pytest.mark.parametrize("m", monoids)
def test_associativity(m, data):
    t = type(m.identity)

    x: T = data.draw(from_type(t))
    y: T = data.draw(from_type(t))
    z: T = data.draw(from_type(t))

    xy: T = m.compose(x, y)
    yz: T = m.compose(y, z)

    assert m.compose(xy, z) == m.compose(x, yz)

import ipytest
ipytest.config(addopts=['-q'])
ipytest.run()

```

```python trusted=false
from __future__ import annotations
from typing import Callable


U = TypeVar("U")
A = TypeVar("A")
B = TypeVar("B")


class Functor(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def map(t: T, f: Callable[A, B]) -> T[B]: pass

class Maybe(Functor[A], metaclass=ABCMeta):
    def map(m: Maybe, f): pass

class Nothing(Maybe[A]):
    def __init__(self, *args):
        pass
    def map(self: Maybe, _):
        return Nothing()
    def __eq__(self, _):
        return True
    def __str__(self):
        return '[Nothing]'

class Just(Maybe[A]):
    def __init__(self, x: A):
        self.x = x
    def map(self: Maybe, f: Callable[A, B]) -> Just[B]:
        return Just(f(self.x))
    def __eq__(self, y):
        return self.x == y
    def __str__(self):
        return f'[Just({self.x})]'


from hypothesis import given
from hypothesis.strategies import data, from_type, functions
from hypothesis import settings, Verbosity
import pytest
from typing import get_args


functors = [
    Nothing,
    Just,
]
types = [
    int,
    str,
    frozenset,
    bool,
]

identity = lambda x: x

@given(data())
@pytest.mark.parametrize("t", types)
@pytest.mark.parametrize("f", functors)
def test_identity(f: Functor, t: type, data):
    F = f[t]
    x = data.draw(from_type(t))

    print(F(x), F(x).map(identity))
    assert F(x) == F(x).map(identity)


@given(data())
@pytest.mark.parametrize("C", types)
@pytest.mark.parametrize("B", types)
@pytest.mark.parametrize("A", types)
@pytest.mark.parametrize("f", functors)
def test_composition(f: Functor, A: type, B:type, C: type, data):

    F = f[A]
    a: A = data.draw(from_type(A))

    def f_spec(x: A) -> B: pass
    f: Callable[A, B] = data.draw(functions(like=f_spec, returns=from_type(B), pure=True))

    def g_spec(y: B) -> C: pass
    g: Callable[b, c] = data.draw(functions(like=g_spec, returns=from_type(C), pure=True))

    def h(x: A) -> C:
        return g(f(x))

    assert F(a).map(h) == F(a).map(f).map(g)

@given(data())
@pytest.mark.parametrize("D", types)
@pytest.mark.parametrize("C", types)
@pytest.mark.parametrize("B", types)
@pytest.mark.parametrize("A", types)
@pytest.mark.parametrize("f", functors)
def test_associativity(f: Functor, A: type, B:type, C: type, D: type, data):
    F = f[A]
    a: A = data.draw(from_type(A))

    def f_spec(x: A) -> B: pass
    f: Callable[A, B] = data.draw(functions(like=f_spec, returns=from_type(B), pure=True))

    def g_spec(y: B) -> C: pass
    g: Callable[b, c] = data.draw(functions(like=g_spec, returns=from_type(C), pure=True))

    def h_spec(z: C) -> D: pass
    h: Callable[b, c] = data.draw(functions(like=h_spec, returns=from_type(D), pure=True))

    fg: Callable[A, C] = lambda x: g(f(x))
    gh: Callable[B, D] = lambda y: h(g(y))

    assert F(a).map(f).map(gh) == F(a).map(fg).map(h)

import ipytest
ipytest.run()
```
