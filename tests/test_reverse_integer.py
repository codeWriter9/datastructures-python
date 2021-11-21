# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.strings.ReverseInteger import ReverseInteger


class TestStack(unittest.TestCase):

    def test_reverse_integer_not_null(self):
        self.assertIsNotNone(ReverseInteger())

    def test_reverse_integer(self):
        self.assertEqual(321, ReverseInteger.reverse(123))
        self.assertEqual(-321, ReverseInteger.reverse(-123))
        self.assertEqual(21, ReverseInteger.reverse(120))
        self.assertEqual(0, ReverseInteger.reverse(0))