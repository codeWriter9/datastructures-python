# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.queue.Queue import Queue


class TestQueue(unittest.TestCase):


    def test_queue(self):
        self.assertIsNotNone(Queue())

    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.front(), None)
        self.assertEqual(queue.back(), None)
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.dequeue(), None)

    def test_enqueue_dequeue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.back(), 2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

    def test_reverseK(self):
        queue = Queue()
        for loop_counter in range(1, 11):
            queue.enqueue(loop_counter)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

