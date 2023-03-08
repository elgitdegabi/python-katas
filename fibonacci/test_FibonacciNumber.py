import unittest

from FibonacciNumber import FibonacciNumber


# Unit test cases for FibonacciNumber
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = FibonacciNumber()


param_list = [
    (0, 0),
    (1, 1),
    (2, 1),
    (5, 5),
    (7, 13),
    (9, 34)
]

complex_param_list = param_list + [
    (45, 1134903170),
    (85, 259695496911122585),
    (99, 218922995834555169026)
]


class TestFibonacciNumber(TestInit):
    def test_calculate(self):
        for value, expected in param_list:
            with self.subTest(value):
                self.assertEqual(self.testClass.calculate(value), expected)

    def test_calculate_with_memoization(self):
        for value, expected in complex_param_list:
            with self.subTest(value):
                self.assertEqual(self.testClass.calculate_with_memoization(value, {}), expected)
