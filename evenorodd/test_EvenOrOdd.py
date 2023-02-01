import unittest
from EvenOrOdd import EvenOrOdd


# Unit test cases for EvenOrOdd
class TestInit(unittest.TestCase):
    def setUp(self):
        self.evenOrOdd = EvenOrOdd()


class TestEvenOrOdd(TestInit):
    def test_even_or_odd_when_value_is_negative_and_odd(self):
        self.assertEqual(self.evenOrOdd.even_or_odd(-1), "Odd")

    def test_even_or_odd_when_value_is_negative_and_even(self):
        self.assertEqual(self.evenOrOdd.even_or_odd(-2), "Even")

    def test_even_or_odd_when_value_is_zero(self):
        self.assertEqual(self.evenOrOdd.even_or_odd(0), "Even")

    def test_even_or_odd_when_value_is_positive_and_odd(self):
        self.assertEqual(self.evenOrOdd.even_or_odd(1), "Odd")

    def test_even_or_odd_when_value_is_positive_and_even(self):
        self.assertEqual(self.evenOrOdd.even_or_odd(2), "Even")
