# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.linkedlist.Node import Node


class TestNode(unittest.TestCase):

    def test_node(self):
        self.assertIsNotNone(Node('data'))


if __name__ == '__main__':
    unittest.main()
