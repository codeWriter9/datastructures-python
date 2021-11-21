# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.BuySellStock import BuySellStock


class TestStack(unittest.TestCase):

    def test_buy_sell_not_null(self):
        self.assertIsNotNone(BuySellStock())

    def test_buy_sell_stock(self):
        self.assertEqual(7, BuySellStock.max_profit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, BuySellStock.max_profit([1, 2, 3, 4, 5]))
        self.assertEqual(0, BuySellStock.max_profit([7, 6, 4, 3, 1]))
