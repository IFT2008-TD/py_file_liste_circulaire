import unittest

from Queue import Queue


class QueueTestCase(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()
        initial = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for e in initial:
            q.enqueue(e)

        final = []
        while not q.est_vide():
            final.append(q.dequeue())

        self.assertEqual(len(final), len(initial))
        for i in range(len(initial)):
            self.assertEqual(final[i], initial[i])


if __name__ == '__main__':
    unittest.main()
