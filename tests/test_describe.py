import unittest

from toolbox import describe

class TestDescribe(unittest.TestCase):
    def test_basic(self):
        pass
        # r = describe([1, 2, 3, 4])
        # self.assertEqual(r["n"], 4)
        # self.assertEqual(r["mean"], 2.5)

    def test_single_value_stdev_none(self):
        self.assertIsNone(describe([5])["stdev"])

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            describe([])
