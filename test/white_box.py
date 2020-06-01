import unittest

from typing import Tuple as _Tuple

from main import sum_between_min_max
from test import DELTA


class TestWhiteBox(unittest.TestCase):
    def template_test(self, array: _Tuple[float, ...], right_result: float):
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def template_test_wrong_type(self, array: _Tuple[float, ...]):
        with self.assertRaises(TypeError):
            sum_between_min_max(array)

    def test_wrong_type_1(self):
        self.template_test_wrong_type([])

    def test_wrong_type_2(self):
        self.template_test_wrong_type(100)

    def test_wrong_type_3(self):
        self.template_test_wrong_type(('a', 1, 2))

    def test_empty(self):
        array = ()
        with self.assertRaises(ValueError):
            sum_between_min_max(array)

    def test_1(self):
        self.template_test((1, ), 0)

    def test_2(self):
        self.template_test((1, 2), 0)

    def test_all_equal_1(self):
        self.template_test((1, 1), 0)

    def test_all_equal_2(self):
        self.template_test((-2.4, -2.4, -2.4, -2.4, -2.4), 0)

    def test_min_before_max(self):
        self.template_test((-1, 4, 17, 2), 4)

    def test_max_before_min(self):
        self.template_test((3, 90, -1, 100, 15, -64.2, 33, -255), -16.2)

    def test_many_min_max_1(self):
        self.template_test((23.3, 23.353, -100, -34.1, 12, -100, 22, 37, 15), -100.1)

    def test_many_min_max_2(self):
        self.template_test((1, 15, -50, 44, 121, 44, -33, 121, 10), 44)

    def test_many_min_max_3(self):
        self.template_test((100, 100, 10, 23, -100, -100, 14), 133)


if __name__ == '__main__':
    unittest.main()
