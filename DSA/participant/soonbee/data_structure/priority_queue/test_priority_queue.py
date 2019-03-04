import unittest
from priority_queue import PriorityQueue

class TestClass(unittest.TestCase):
  def setUp(self):
    self.pq = PriorityQueue()
  
  def tearDown(self):
    del self.pq

  # default feature test - push, pop, peek
  def test_01(self):
    self.pq.push(3) 
    self.pq.push(5) 
    self.pq.push(4) 
    self.pq.push(8) 
    self.pq.push(2) 
    self.pq.push(1) 
    self.pq.push(6) 
    self.assertEqual(str(self.pq), '[1, 3, 2, 8, 5, 4, 6]')
    self.assertEqual(self.pq.peek(), 1)
    self.assertEqual(self.pq.pop(), 1)
    self.assertEqual(str(self.pq), '[2, 3, 4, 8, 5, 6]')
    self.assertEqual(self.pq.peek(), 2)
    self.assertEqual(self.pq.pop(), 2)
    self.assertEqual(str(self.pq), '[3, 5, 4, 8, 6]')
  
  # empty test
  def test_02(self):
    self.assertTrue(self.pq.is_empty)
    with self.assertRaises(IndexError) as cm:
      self.pq.pop()
    self.assertEqual(str(cm.exception), "pop from empty priority queue")

    with self.assertRaises(IndexError) as cm:
      self.pq.peek()
    self.assertEqual(str(cm.exception), "peek from empty priority queue")


if __name__ == "__main__":
  unittest.main()