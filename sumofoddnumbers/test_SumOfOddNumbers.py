import unittest

from SumOfOddNumbers import SumOfOddNumbers


# Unit test cases for SumOfOddNumbers
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = SumOfOddNumbers()


class TestSumOfOddNumbers(TestInit):
    def test_sum_odd_numbers_triangle_when_row_is_0(self):
        self.assertEqual(self.testClass.sum_odd_numbers_triangle(0), 0)

    def test_sum_odd_numbers_triangle_when_row_is_1(self):
        self.assertEqual(self.testClass.sum_odd_numbers_triangle(1), 1)

    def test_sum_odd_numbers_triangle_when_row_is_2(self):
        self.assertEqual(self.testClass.sum_odd_numbers_triangle(2), 8)

    def test_sum_odd_numbers_triangle_when_row_is_3(self):
        self.assertEqual(self.testClass.sum_odd_numbers_triangle(3), 27)

    def test_sum_odd_numbers_triangle_when_row_is_4(self):
        self.assertEqual(self.testClass.sum_odd_numbers_triangle(4), 64)

    def test_sum_odd_numbers_triangle_when_row_is_5(self):
        self.assertEqual(self.testClass.sum_odd_numbers_triangle(5), 125)
