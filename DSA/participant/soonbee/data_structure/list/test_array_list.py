import unittest
from array_list import ArrayList

class TestArrayList(unittest.TestCase):
  def setUp(self):
    self.li = ArrayList()
  
  def tearDown(self):
    pass

  # default feature test - push, pop, peek
  def test_01(self):
    self.li.push(0, 1)
    self.li.push(0, 2)
    self.li.push(2, 3)
    self.li.push(0, 5)
    self.li.push(1, 7)
    self.li.push(2, 6)
    self.assertEqual(str(self.li), "[5, 7, 6, 2, 1, 3]")
    self.assertEqual(self.li.peek(0), 5)
    self.assertEqual(self.li.peek(5), 3)
    self.assertEqual(self.li.pop(0), 5)
    self.assertEqual(self.li.peek(4), 3)
    self.assertEqual(self.li.peek(2), 2)
  
  # index out of range test
  def test_02(self):
    with self.assertRaises(IndexError) as cm:
      self.li.pop(-1)
    self.assertEqual(str(cm.exception), "index out of range")

    with self.assertRaises(IndexError) as cm:
      self.li.peek(-1)
    self.assertEqual(str(cm.exception), "index out of range")

    with self.assertRaises(IndexError) as cm:
      self.li.pop(0)
    self.assertEqual(str(cm.exception), "index out of range")

    with self.assertRaises(IndexError) as cm:
      self.li.peek(0)
    self.assertEqual(str(cm.exception), "index out of range")
    
    with self.assertRaises(IndexError) as cm:
      self.li.push(-1, 1)
    self.assertEqual(str(cm.exception), "index out of range")

    with self.assertRaises(IndexError) as cm:
      self.li.push(2, 1)
    self.assertEqual(str(cm.exception), "index out of range")
  
  # expand test
  def test_03(self):
    for _ in range(10):
      self.li.push(0, 0)
    self.assertEqual(len(self.li._array), 10)
    self.li.push(0, 1)
    self.assertEqual(len(self.li._array), 20)
    self.assertEqual(str(self.li), "[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]")
  
  # expand test 2
  def test_04(self):
    for _ in range(10):
      self.li.push(0, 0)
    self.assertEqual(len(self.li._array), 10)
    self.li.push(10, 1)
    self.assertEqual(len(self.li._array), 20)
    self.assertEqual(str(self.li), "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]")


if __name__ == "__main__":
  unittest.main()