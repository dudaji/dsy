import unittest
from chaining import HashTable

class TestHashTable(unittest.TestCase):
  def setUp(self):
    self.ht = HashTable()
    push = self.ht.push
    push("apple", 100) # hashed key: 10
    push("orange", 200) # hashed key: 9
    push("melon", 300) # hashed key: 2
    push("strawberry", 400) # hashed key: 4
    push("banana", 500) # hashed key: 1
    push("watermelon", 600) # hashed key: 10
    push("mango", 550) # hashed key: 4
  
  def tearDown(self):
    del self.ht
  
  def test_01_peek(self):
    self.assertEqual(self.ht.peek("apple"), 100)
    self.assertEqual(self.ht.peek("orange"), 200)
    self.assertEqual(self.ht.peek("melon"), 300)
    self.assertEqual(self.ht.peek("strawberry"), 400)
    self.assertEqual(self.ht.peek("banana"), 500)
    self.assertEqual(self.ht.peek("watermelon"), 600)
    self.assertEqual(self.ht.peek("mango"), 550)

  def test_02_pop(self):
    self.assertEqual(self.ht.pop("apple"), 100)
    self.assertEqual(self.ht.pop("orange"), 200)
    self.assertEqual(self.ht.pop("melon"), 300)
    self.assertEqual(self.ht.pop("strawberry"), 400)
    self.assertEqual(self.ht.pop("banana"), 500)
    self.assertEqual(self.ht.pop("watermelon"), 600)
    self.assertEqual(self.ht.pop("mango"), 550)
    with self.assertRaises(KeyError):
      self.ht.pop("apple")

  def test_03_expand(self):
    push = self.ht.push
    self.assertEqual(self.ht.capacity, 10)
    push("tomato", 101)
    push("pear", 102)
    push("peach", 103)
    push("another", 104)
    push("other", 105)
    push("something", 106)
    self.assertEqual(self.ht.capacity, 15)

  def test_04_modify(self):
    push = self.ht.push
    push("apple", 101)
    push("orange", 201)
    push("melon", 301)
    push("strawberry", 401)
    push("banana", 501)
    push("watermelon", 601)
    push("mango", 551)
    self.assertEqual(self.ht.peek("apple"), 101)
    self.assertEqual(self.ht.peek("orange"), 201)
    self.assertEqual(self.ht.peek("melon"), 301)
    self.assertEqual(self.ht.peek("strawberry"), 401)
    self.assertEqual(self.ht.peek("banana"), 501)
    self.assertEqual(self.ht.peek("watermelon"), 601)
    self.assertEqual(self.ht.peek("mango"), 551)


if __name__ == "__main__":
  unittest.main()
