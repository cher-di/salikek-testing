import unittest

from typing import Tuple as _Tuple

from main import sum_between_min_max
from test import DELTA


class TestBlackBox(unittest.TestCase):
    def template_test(self, array: _Tuple[float, ...], right_result: float):
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_1(self):
        self.template_test((1, ), 0)

    def test_2(self):
        self.template_test((1, 2), 0)

    def test_3_straight(self):
        self.template_test((1, 2, 3), 2)

    def test_3_reverse(self):
        self.template_test((3, 2, 1), 2)

    def test_4_straight(self):
        self.template_test((1, 2, 3, 4), 5)

    def test_4_reverse(self):
        self.template_test((4, 3, 2, 1), 5)

    def test_many_min_max_1(self):
        self.template_test((3, 4, 1, 6, 7, 4, 5, 3, 9, 4, 9), 25)

    def test_many_min_max_2(self):
        self.template_test((5, 6, 6, 7, 3, 4, 8, 5, 1, 5, 1, 3, 7), 5)

    def test_all_equal_1(self):
        self.template_test((1, 1, 1, 1, 1, 1), 0)

    def test_all_equal_2(self):
        self.template_test((2, 2, 2, 2, 2), 0)

    def test_all_equal_3(self):
        self.template_test((3, 3), 0)

    def test_float(self):
        self.template_test((1.1, 2.3, 1.0, 1, 2.3, 2.4), 3.3)


if __name__ == '__main__':
    unittest.main()
