import unittest
from stack import SimpleStack, ArrayStack, LinkedListStack

class TestSimpleStack(unittest.TestCase):
  def setUp(self):
    self.st = SimpleStack()

  def tearDown(self):
    del self.st

  # default feature test - push, pop, peek
  def test_01(self):
    self.st.push(1)
    self.st.push(2)
    self.st.push(3)
    self.assertEqual(self.st.peek(), 3)
    self.assertEqual(self.st.pop(), 3)
    self.assertEqual(self.st.peek(), 2)
    self.assertEqual(self.st.pop(), 2)
    self.assertEqual(self.st.peek(), 1)
    self.assertEqual(self.st.pop(), 1)

  # raise error when pop with empty stack
  def test_02(self):
    with self.assertRaises(IndexError) as cm:
      self.st.pop()
    self.assertEqual("stack is empty", str(cm.exception))
  
  # test check empty
  def test_03(self):
    self.assertTrue(self.st.is_empty())


class TestArrayStack(unittest.TestCase):
  def setUp(self):
    self.st = ArrayStack()

  def tearDown(self):
    del self.st
  
  # default feature test - push, pop, peek
  def test_01(self):
    self.st.push(1)
    self.st.push(2)
    self.st.push(3)
    self.assertEqual(self.st.peek(), 3)
    self.assertEqual(self.st.pop(), 3)
    self.assertEqual(self.st.peek(), 2)
    self.assertEqual(self.st.pop(), 2)
    self.assertEqual(self.st.peek(), 1)
    self.assertEqual(self.st.pop(), 1)

  # raise error when pop with empty stack
  def test_02(self):
    with self.assertRaises(IndexError) as cm:
      self.st.pop()
    self.assertEqual("stack is empty", str(cm.exception))
  
  # test check empty
  def test_03(self):
    self.assertTrue(self.st.is_empty())

  # test expand
  def test_04(self):
    self.assertEqual(len(self.st._array), 10)
    for i in range(11):
      self.st.push(i)
    self.assertEqual(len(self.st._array), 20)


class TestLinkedListStack(unittest.TestCase):
  def setUp(self):
    self.st = LinkedListStack()

  def tearDown(self):
    del self.st

  # default feature test - push, pop, peek
  def test_01(self):
    self.st.push(1)
    self.st.push(2)
    self.st.push(3)
    self.assertEqual(self.st.peek(), 3)
    self.assertEqual(self.st.pop(), 3)
    self.assertEqual(self.st.peek(), 2)
    self.assertEqual(self.st.pop(), 2)
    self.assertEqual(self.st.peek(), 1)
    self.assertEqual(self.st.pop(), 1)

  # raise error when pop with empty stack
  def test_02(self):
    with self.assertRaises(IndexError) as cm:
      self.st.pop()
    self.assertEqual("stack is empty", str(cm.exception))
  
  # test check empty
  def test_03(self):
    self.assertTrue(self.st.is_empty())
 

if __name__ == "__main__":
  unittest.main()

