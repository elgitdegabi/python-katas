import unittest

from SplitStringIntoPair import SplitStringIntoPair


# Unit test cases for SplitStringIntoPair
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = SplitStringIntoPair()


param_list = [
    (None, []),
    ("", []),
    ("a", ["a_"]),
    ("ab", ["ab"]),
    ("abc", ["ab", "c_"]),
    ("abcd", ["ab", "cd"]),
]


class TestSplitStringIntoPair(TestInit):
    def test_split(self):
        for value, expected in param_list:
            with self.subTest():
                self.assertEqual(self.testClass.split(value), expected)
