# The four tasks

One task per person. Each is an issue in this repository and each has a branch
already created for you. Work only on your own files in Stage 1.

---

## Issue 1 - Student A - `toolbox/stats.py`
Branch: `feature/stats`

Implement `describe(values)` so that it returns a dictionary with the keys
`n`, `mean`, `median`, `stdev`, `min`, `max`.

- `stdev` is the **sample** standard deviation (divide by `n - 1`), and `None` when `n < 2`.
- An empty list raises `ValueError`.
- Standard library only. `statistics` is part of the standard library and you may use it.

Add `tests/test_stats.py` with at least three test cases, one of which is the
empty-list error.

---

## Issue 2 - Student B - `toolbox/text.py`
Branch: `feature/text`

Implement `word_counts(text, top=None)` returning a list of `(word, count)`
tuples, sorted by count descending and then by word ascending.

- Lowercase everything, strip surrounding punctuation (`.,;:!?"'()`).
- `top=3` returns only the three most frequent words.
- Empty text returns an empty list.

Add `tests/test_text.py` with at least three test cases, one of which checks
the tie-breaking order.

---

## Issue 3 - Student C - `toolbox/sequences.py`
Branch: `feature/sequences`

Implement `fibonacci(n)` and `primes_below(limit)`.

- `fibonacci(0) == []`, `fibonacci(1) == [0]`, `fibonacci(5) == [0, 1, 1, 2, 3]`.
- Negative `n` raises `ValueError`.
- `primes_below(10) == [2, 3, 5, 7]`, `primes_below(2) == []`.

Add `tests/test_sequences.py` with at least three test cases.

---

## Issue 4 - Student D - `toolbox/validate.py`
Branch: `feature/validate`

Implement `require_number(value, name="value")` and
`require_non_empty(sequence, name="sequence")`.

- `require_number` accepts `int`, `float` and numeric strings, and returns a `float`.
- `True` and `False` raise `TypeError` (a bool is not a measurement).
- Anything else raises `ValueError` whose message contains `name`.
- `require_non_empty` returns the sequence, or raises `ValueError` if it is empty.

Add `tests/test_validate.py` with at least four test cases, including the bool case.

---

## Stage 2, for everybody

On your own branch, and at the same time as the other three:

1. add your import line to the wiring block in `toolbox/__init__.py`,
   and add your exported name to `__all__`;
2. add your command branch to the wiring block in `cli.py`;
3. fill in your row of the module table in `README.md`.

The first pull request to be merged will go in cleanly. The other three will
conflict. That is the point of the stage: resolve them so that **all four**
contributions survive.
