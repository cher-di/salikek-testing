import unittest
from main import sum_between_min_max


class TestBlackBox(unittest.TestCase):

    def test_1(self):
        array = (1,)
        right_result = 0
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_2(self):
        array = (1, 2)
        right_result = 0
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_3_straight(self):
        array = (1, 2, 3)
        right_result = 2
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_3_reverse(self):
        array = (3, 2, 1)
        right_result = 2
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_4_straight(self):
        array = (1, 2, 3, 4)
        right_result = 5
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_4_reverse(self):
        array = (4, 3, 2, 1)
        right_result = 5
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_many_min_max_1(self):
        array = (3, 4, 1, 6, 7, 4, 5, 3, 9, 4, 9)
        right_result = 25
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_many_min_max_2(self):
        array = (5, 6, 6, 7, 3, 4, 8, 5, 1, 5, 1, 3, 7)
        right_result = 5
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_all_equal_1(self):
        array = (1, 1, 1, 1, 1, 1)
        right_result = 0
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_all_equal_2(self):
        array = (2, 2, 2, 2, 2)
        right_result = 0
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_all_equal_3(self):
        array = (3, 3)
        right_result = 0
        self.assertEqual(sum_between_min_max(array), right_result)

    def test_float(self):
        array = (1.1, 2.3, 1.0, 1, 2.3, 2.4)
        right_result = 3.3
        self.assertEqual(sum_between_min_max(array), right_result)


if __name__ == '__main__':
    unittest.main()
