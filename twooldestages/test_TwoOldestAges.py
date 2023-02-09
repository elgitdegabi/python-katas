import unittest

from TwoOldestAges import TwoOldestAges


# Unit test cases for TwoOldestAges
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = TwoOldestAges()


param_list = [
    (None, []),
    ([], []),
    ([1], []),
    ([0, 0], [0, 0]),
    ([5, 10], [5, 10]),
    ([1, 3, 10, 0], [3, 10]),
    ([1, 2, 10, 8], [8, 10]),
    ([1, 5, 87, 45, 8, 8], [45, 87]),
    ([2, 5, 87, 45, 8, 8], [45, 87]),
    ([6, 5, 83, 5, 3, 18], [18, 83]),
    ([6, 5, 83, 5, 3, 18], [18, 83])
]


class TestTwoOldestAges(TestInit):
    def test_two_oldest_ages(self):
        for array, expected in param_list:
            with self.subTest():
                self.assertEqual(self.testClass.two_oldest_ages(array), expected)
