import unittest
from toolbox import fibonacci
from toolbox import primes_below

class TestSequences (unittest.TestCase):
    def test_fibonacci(self):

        value = 3 
        assert(fibonacci(value),[0,1,1])

        value = 10
        assert(primes_below(10), [[2, 3, 5, 7]])



            
    