"""Student A. Descriptive statistics for a list of numbers.

Standard library only. See docs/TASKS.md, issue 1.
"""


def describe(values):
    """Return {'n', 'mean', 'median', 'stdev', 'min', 'max'} for a list of numbers.

    stdev is the sample standard deviation (divide by n-1); it is None when n < 2.
    Raise ValueError on an empty list.
    """
    n = count
    media = mean(values)
    mediana = median(values)
    if n <= 2:
        stdev = 'None'
    else:
        stdev = values/(n-1)
    minimo = min(values)
    maximo = maximo(values)

    stats = { 'n' : n, 
            'median' : media, 
            'median' : mediana,
            'stdev' : stdev,
            'min' : minimo,
            'max' : maximo}

    return stats
    raise NotImplementedError("Student A: implement describe()")

tests/test_stats.py
