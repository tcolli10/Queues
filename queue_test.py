import unittest
# from queue_array import Queue
from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
    
    def test_is_empty(self):
        q = Queue(3)
        self.assertTrue(q.is_empty())
    
    def test_is_empty2(self):
        q = Queue(3)
        q.enqueue(2)
        self.assertFalse(q.is_empty())
    
    def test_is_full(self):
        q = Queue(2)
        q.enqueue(1)
        q.enqueue(2)
        self.assertTrue(q.is_full())
    
    def test_is_full2(self):
        q = Queue(3)
        self.assertFalse(q.is_full())

    def test_is_full3(self):
        q = Queue(3)
        q.enqueue(3)
        self.assertFalse(q.is_full())

    def test_enqueue_linked(self):
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.head.data, 1)
        self.assertEqual(q.tail.data, 3)

    def test_enqueue_array(self):
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.items[q.head], 1)
        self.assertEqual(q.items[q.num_items - 1], 3)

    def test_enqueue2(self):
        q = Queue(2)
        q.enqueue(1)
        q.enqueue(2)
        with self.assertRaises(IndexError):
            q.enqueue(3)
        
    def test_dequeue(self):
        q = Queue(4)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)

    def test_dequeue2(self):
        q = Queue(3)
        with self.assertRaises(IndexError):
            q.dequeue()
        
    def test_size(self):
        q = Queue(4)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
    
    def test_size2(self):
        q = Queue(3)
        self.assertEqual(q.size(), 0)

if __name__ == '__main__': 
    unittest.main()
