import unittest

from FibonacciElements import FibonacciElements


# Unit test cases for FibonacciElements
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = FibonacciElements()


param_list = [
    (0, []),
    (1, [1]),
    (2, [1, 1]),
    (85, []),
    (5, [1, 1, 2, 3, 5]),
    (7, [1, 1, 2, 3, 5, 8, 13]),
    (9, [1, 1, 2, 3, 5, 8, 13, 21, 34])
]


class TestFibonacciElements(TestInit):
    def test_get_elements(self):
        for value, expected in param_list:
            with self.subTest(value):
                self.assertEqual(self.testClass.get_elements(value), expected)
