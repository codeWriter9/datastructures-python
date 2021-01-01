# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.queue.NewQueue import NewQueue
from datastructures.queue.Queue import Queue
from datastructures.queue.QueueUtil import QueueUtil
from datastructures.stack.Stack import Stack


class TestQueueUtil(unittest.TestCase):


    def queue_initialize(self, number_of_elements):
        queue = Queue()
        for counter in range(1, number_of_elements):
            queue.enqueue(counter)
        return queue;

    def test_queue(self):
        self.assertIsNotNone(Queue())
        self.assertIsNotNone(QueueUtil())
        self.assertIsNotNone(NewQueue())

    def test_reverseK(self):
        queueUtil = QueueUtil()
        queue = self.queue_initialize(11)
        anotherQueue = queueUtil.reverseK(queue, 5)
        print([x for x in anotherQueue.queue_list ])

    def test_reverseK_empty(self):
        queueUtil = QueueUtil()
        queue = Queue()
        anotherQueue = queueUtil.reverseK(queue, 5)
        self.assertEqual(anotherQueue, None)
        queue = self.queue_initialize(11)
        anotherQueue = queueUtil.reverseK(queue, 22)
        self.assertEqual(anotherQueue, None)
        queue = self.queue_initialize(11)
        anotherQueue = queueUtil.reverseK(queue, -4)
        self.assertEqual(anotherQueue, None)

    def test_new_queue_empty(self):
        self.assertIsNotNone(NewQueue())
        self.assertEqual(NewQueue().dequeue(), None)

    def test_new_queue_singleton_element(self):
        nq = NewQueue()
        self.assertIsNotNone(nq)
        nq.enqueue(1)
        self.assertEqual(nq.dequeue(), 1)

    def test_new_queue(self):
        nq = NewQueue()
        self.assertIsNotNone(nq)
        for counter in range(1, 11):
            nq.enqueue(counter)
        for counter in range(1, 11):
            self.assertEqual(nq.dequeue(), counter)