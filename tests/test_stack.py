# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.stack.Stack import Stack


class TestStack(unittest.TestCase):


    def test_stack(self):
        self.assertIsNotNone(Stack())

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.top(), None)
        self.assertEqual(stack.pop(), None)

    def test_pop_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.top(), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.top(), None)