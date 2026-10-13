"""Student A. Descriptive statistics for a list of numbers.

Standard library only. See docs/TASKS.md, issue 1.
"""
import statistics as st

def describe(values):
    """Return {'n', 'mean', 'median', 'stdev', 'min', 'max'} for a list of numbers.

    stdev is the sample standard deviation (divide by n-1); it is None when n < 2.
    Raise ValueError on an empty list.
    """

    if not values:
        raise ValueError('Empty list')
    
    n = len(values)
    media = st.mean(values)
    mediana = st.median(values)
    
    if n < 2:
        desvio = None
    else:
        desvio = st.stdev(values)
    minimo = min(values)
    maximo = max(values)

    stats = {'n' : n, 
            'mean' : media, 
            'median' : mediana,
            'stdev' : desvio,
            'min' : minimo,
            'max' : maximo}

    return stats

    #raise NotImplementedError("Student A: implement describe()")
