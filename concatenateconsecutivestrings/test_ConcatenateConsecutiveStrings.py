import unittest

from ConcatenateConsecutiveStrings import ConcatenateConsecutiveStrings


# Unit test cases for ConcatenateConsecutiveStrings
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = ConcatenateConsecutiveStrings()


param_list = [
    (["a", "b", "cd", "efg"], 2, "cdefg"),
    (["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2, "folingtrashy"),
    (["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2, "abigailtheta"),
    (["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1,
     "oocccffuucccjjjkkkjyyyeehh"),
    ([], 3, ""),
    (["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2,
     "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"),
    (["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2, "wlwsasphmxxowiaxujylentrklctozmymu"),
    (["zone", "abigail", "theta", "form", "libe", "zas"], -2, ""),
    (["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3, "ixoyx3452zzzzzzzzzzzz"),
    (["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15, ""),
    (["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0, "")
]


class TestConcatenateConsecutiveStrings(TestInit):
    def test_consecutive_string(self):
        for array, k, expected in param_list:
            with self.subTest():
                self.assertEqual(self.testClass.consecutive_string(array, k), expected)
