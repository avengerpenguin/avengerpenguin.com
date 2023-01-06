---
jupyter:
  jupytext:
    cell_metadata_filter: all
    notebook_metadata_filter: all
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.3"
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.10.4
---

This is an exploration of building up Zermelo–Fraenkel set theory as a foundational basis of mathematics, but actually implemented in Python.

There is no clear application for any of this other than the challenge of trying to reimplement arithmetic (inefficiently) without being able to use literal numbers.

The challenge here is to recreate arithemtic operations such as addition and multiplication and representations of sets of different kinds of numbers using only a "set" object in Python. No literal numbers are allowed and we may even try to avoid `lambda` so that we are forced to recreate functions.

What we will need to do though is allow the use of `class` to wrap the native Python set and use operator overloading to allow us to define operations of that set as we can justify them from axioms. Part of the reason for this will be the need to represent infinite sets which requires some pairing up of sets and generators.

Firstly, we start from a very basic assertion:

## Things Exist

The most philosophical foundation before we get into what we can be sure exists and is correct is to accept that at least something exists (as in "I think therefore I am").

If we imagine that it is reasonable to group things together arbitrarily, then it follows we can create some empty grouping we can call the empty set:

```python trusted=true
Ø = frozenset()
len(Ø)
```

Note for now we can just use Python's built-in concept of `frozenset` since it has all the properties we want for now (i.e. it's empty).

## Axiom of Infinity

```python trusted=true
class Set(frozenset):
    def __init__(self, definition=frozenset()):
        if hasattr(definition, '__call__'):
            self.gen_func = definition
        else:
            self.gen_func = None
            super(definition)

Set()
```

```python trusted=true
# # Empty set
# 〇 = frozenset()
# # pair
# 𝕡 = lambda a, b: frozenset({a, b})


# 𝑺 = lambda domain, cond: (x for x in domain if cond(x))

```

```python trusted=true
𝕡 = lambda a, b: frozenset({a, b})
𝑃 = lambda a, b: 𝕡(𝕡("l", a), 𝕡("r", b))

class Set:
    def __init__(self, genf=set):
        self.genf = genf
        self.vals = set()
    def __iter__(self):
        gen = self.genf()
        for n in gen:
            if n not in self.vals:
                self.vals.add(n)
                yield n
    def __or__(self, o):
        def _gen():
            A, B = iter(self), iter(o)
            while A and B:
                if A:
                    try:
                        a = next(A)
                        yield a
                    except StopIteration:
                        A = None
                if B:
                    try:
                        b = next(B)
                        yield b
                    except StopIteration:
                        B = None
        return Set(_gen)
    def __mul__(self, o):
        def _gen():
            out = set()
            A, B = iter(self), iter(o)
            while A and B:
                try:
                    a, b = next(A), next(B)
                except StopIteration:
                    break
                c = 𝑃(a, b)
                if c not in out:
                    out.add(c)
                    yield c
        return Set(_gen)


〇 = Set()
succ = lambda n: Set(lambda: {n}) | n

class Naturals:
    n = None
    def __next__(self):
        self.n = 〇 if self.n is None else succ(self.n)
        return self.n
    def __iter__(self):
        return self


ℕ = Set(Naturals)
add = lambda 𝑚, 𝑛: Set(lambda: (𝑚 * {〇}) | (𝑛 * {succ(〇)}))
set(add(〇, 〇))

```

```python trusted=true
𝑃 = lambda a, b: 𝕡(𝕡("l", a), 𝕡("r", b))
𝑃("a", "b")
```

```python trusted=true
left = lambda p: {r for r in {q for q in p if "l" in q}.pop() if r != "l"}.pop()
right = lambda p: {r for r in {q for q in p if "r" in q}.pop() if r != 'r'}.pop()
left(𝑃("a", "b")), right(𝑃("a", "b"))
```

```python trusted=true
𝑓 = lambda P: lambda a: next(right(p) for p in P if left(p) == a)
succ = 𝑓(𝑃(n, frozenset({n}) | n) for n in ℕ())
len(succ(succ(〇)))
```

```python trusted=true
class InfSet:
    def __init__(self, genf):
        self.genf = genf
        self.vals = set()
    def __iter__(self):
        gen = self.genf()
        for n in gen:
            if n not in self.vals:
                self.vals.add(n)
                yield n
    def __or__(self, o):
        iterators = (iter(self), iter(o))
        while iterators:
            for v in map(next, iterators):
                yield v


ℕ2 = InfSet(ℕ)
S = ℕ2 | ℕ2
for n in S:
    print(len(n))
```
