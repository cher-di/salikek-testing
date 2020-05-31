import unittest
from main import sum_between_min_max
from test import DELTA


class TestWhiteBox(unittest.TestCase):
    def test_wrong_type_1(self):
        array = []
        with self.assertRaises(TypeError):
            sum_between_min_max(array)

    def test_wrong_type_2(self):
        array = 100
        with self.assertRaises(TypeError):
            sum_between_min_max(array)

    def test_wrong_type_3(self):
        array = ('a', 1, 2)
        with self.assertRaises(TypeError):
            sum_between_min_max(array)

    def test_empty(self):
        array = ()
        with self.assertRaises(ValueError):
            sum_between_min_max(array)

    def test_1(self):
        array = (1, )
        right_result = 0
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_2(self):
        array = (1, 2)
        right_result = 0
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_all_equal_1(self):
        array = (1, 1)
        right_result = 0
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_all_equal_2(self):
        array = (-2.4, -2.4, -2.4, -2.4, -2.4)
        right_result = 0
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_min_before_max(self):
        array = (-1, 4, 17, 2)
        right_result = 4
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_max_before_min(self):
        array = (3, 90, -1, 100, 15, -64.2, 33, -255)
        right_result = -16.2
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_many_min_max_1(self):
        array = (23.3, 23.353, -100, -34.1, 12, -100, 22, 37, 15)
        right_result = -100.1
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_many_min_max_2(self):
        array = (1, 15, -50, 44, 121, 44, -33, 121, 10)
        right_result = 44
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)

    def test_many_min_max_3(self):
        array = (100, 100, 10, 23, -100, -100, 14)
        right_result = 133
        self.assertAlmostEqual(sum_between_min_max(array), right_result, delta=DELTA)


if __name__ == '__main__':
    unittest.main()
