"""Student C. Integer sequences.

Standard library only. See docs/TASKS.md, issue 3.
"""


def fibonacci(n):
    """Return the first n Fibonacci numbers as a list, starting [0, 1, 1, 2, ...].

    n == 0 returns an empty list. Raise ValueError for negative n.
    """
    if n < 0:
        raise ValueError('n must be positive')
    elif not isinstance(n,int):
        raise Exception('n must be an int')
    
    fib_sequence = []
    a = 0
    b = 1

    for element in range(n):
        fib_sequence.append(a)
        a,b = b, a + b

    else:
        return fib_sequence

   # raise NotImplementedError("Student C: implement fibonacci()")

fibonacci(3)

def primes_below(limit):
    """Return every prime strictly below limit, as a sorted list."""

    if limit < 0:
        raise Exception('Limit must be positive.')
    elif not isinstance(limit,int):
        raise Exception('Limit must be an int')

    primes = []

    for num in range(2, limit):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes
                
#raise NotImplementedError("Student C: implement primes_below()")

fibonacci(3)

