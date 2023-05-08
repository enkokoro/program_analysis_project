import array
import queue
from queue import Queue
import unittest


class QueueTest(unittest.TestCase):
    def test_dequeue(self):
        self.assertEqual(
            Queue.dequeue(self=<queue.Queue object at 0x7f8059ba3d30>),
            1
        )


    def test_empty(self):
        self.assertEqual(
            Queue.empty(self=<queue.Queue object at 0x7f8059ba3d30>),
            False
        )


    def test_enqueue(self):
        self.assertEqual(
            Queue.enqueue(self=<queue.Queue object at 0x7f8059ba3d30>,x=2),
            True
        )


    def test_full(self):
        self.assertEqual(
            Queue.full(self=<queue.Queue object at 0x7f8059ba3d30>),
            False
        )


if __name__ == "__main__":
    unittest.main()
