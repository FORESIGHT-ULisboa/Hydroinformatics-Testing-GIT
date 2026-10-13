"""The one test that exists before you start. It must never fail on main."""
import unittest
import toolbox
class TestPackage(unittest.TestCase):
    def test_importable(self):
        self.assertTrue(toolbox.word_counts("Aha! Even after Sarah's 'ultimate' checklist (which, let's be honest, was 100% overkill), did we actually forget: the keys, the maps & the snacks... at 4:00 A.M.?!",3),[('the', 3)])
        self.assertTrue(toolbox.word_counts("Wait, wait, wait! Did she really, really say: 'No, no, NO! Do not, under any circumstances, touch that—er, I mean, *that*—button (the red, shiny one!), okay?!'",2),[('really', 2)])
        self.assertTrue(toolbox.word_counts("Wait did you actually say, 'Bring the snacks (chips, dip, and soda!), water cold, not warm! and, oh, don't forget the ice!'?"),[('wait', 1), ('did', 1), ('you', 1), ('actually', 1), ('say', 1), ('bring', 1), ('the', 2), ('snacks', 1), ('chips', 1), ('dip', 1), ('and', 2), ('soda', 1), ('water', 1), ('cold', 1), ('not', 1), ('warm', 1), ('and', 2), ('oh', 1), ('dont', 1), ('forget', 1), ('the', 2), ('ice', 1)])

if __name__ == "__main__":
    unittest.main()