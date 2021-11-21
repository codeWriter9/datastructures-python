# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.MoveZeroes import MoveZeroes


class TestStack(unittest.TestCase):

    def test_move_zeroes_not_null(self):
        self.assertIsNotNone(MoveZeroes())

    def test_move_zeroes(self):
        nums = [0, 1, 0, 3, 12]
        MoveZeroes.move_zeroes(nums)
        self.assertEqual([1, 3, 12, 0, 0], nums)
        nums = [0]
        MoveZeroes.move_zeroes(nums)
        self.assertEqual([0], nums)
