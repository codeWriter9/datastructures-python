# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.RotateImage import RotateImage


class TestStack(unittest.TestCase):

    def test_rotate_image_not_null(self):
        self.assertIsNotNone(RotateImage())

    def test_transpose_image(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        RotateImage.transpose(matrix)
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], matrix)

    def test_reflect_image(self):
        matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        RotateImage.reflect(matrix)
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], matrix)

    def test_rotate_image(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        RotateImage.rotate(matrix)
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], matrix)
