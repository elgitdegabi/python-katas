import unittest

from LocalMinMax import LocalMinMax


# Unit test cases for LocalMinMax
class TestInit(unittest.TestCase):
    def setUp(self):
        self.testClass = LocalMinMax()


param_list = [
    (None, [0, 0]),
    ([], [0, 0]),
    ([1], [1, 1]),
    ([1, 1], [1, 1]),
    ([1, 2, 3, 4], [1, 4]),
    ([4, 3, 2, 1], [1, 4])
]


class TestLocalMinMax(TestInit):
    def test_get_local_min_max(self):
        for value, expected in param_list:
            with self.subTest():
                self.assertEqual(self.testClass.get_local_min_max(value), expected)

    def test_get_local_min_max_alternative(self):
        for value, expected in param_list:
            with self.subTest():
                self.assertEqual(self.testClass.get_local_min_max_alternative(value), expected)
