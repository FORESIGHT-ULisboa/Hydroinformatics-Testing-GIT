"""The one test that exists before you start. It must never fail on main."""
import unittest

import toolbox


class TestPackage(unittest.TestCase):
    def test_importable(self):
        self.assertTrue(hasattr(toolbox, "__version__"))


if __name__ == "__main__":
    unittest.main()
