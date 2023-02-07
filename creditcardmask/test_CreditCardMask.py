import unittest

from CreditCardMask import CreditCardMask


# Unit test cases for CreditCardMask
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = CreditCardMask()


param_list = [
    (None, None),
    ("", ""),
    ("abc", "abc"),
    ("abcd", "abcd"),
    ("4556364607935616", "############5616"),
    ("64607935616", "#######5616"),
    ("Skippy", "##ippy"),
    ("Nananananananananananananananana Batman!", "####################################man!")
]


class TestCreditCardMask(TestInit):
    def test_consecutive_string(self):
        for value, expected in param_list:
            with self.subTest():
                self.assertEqual(self.testClass.maskify(value), expected)
