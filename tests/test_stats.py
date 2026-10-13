import unittest

from toolbox import describe

class test_stats(unittest.TestCase):
    def test_basic(self):
        result = describe([1, 2, 3, 4])
        assert(result["n"] == 4)
        assert(result["mean"] == 2.5)
        assert(result["median"] == 2.5)
        assert(result["min"] == 1)
        assert(result["max"] == 4)
        print(result) 


#class test_stats(unittest.TestCase):

    