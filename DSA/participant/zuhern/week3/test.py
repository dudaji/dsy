import unittest
import hash_chaining

class TestHash(unittest.TestCase):

  def test_hash_chaining(self):

    hash_chaining.hash_set(1, 'value1')
    hash_chaining.hash_set(2, 'value2')
    hash_chaining.hash_set(3, 'value3')
    hash_chaining.hash_set(4, 'value4')
    hash_chaining.hash_set(5, 'value5')
    hash_chaining.hash_set(6, 'value6')
    hash_chaining.hash_set(7, 'value7')
    hash_chaining.hash_set(8, 'value8')
    hash_chaining.hash_set(9, 'value9')
    hash_chaining.hash_set(10, 'value10')
    hash_chaining.hash_set(1, 'value1-1')

    self.assertEqual(hash_chaining.hash_get(1), 'value1')
    self.assertEqual(hash_chaining.hash_get(9), 'value9')
    self.assertEqual(hash_chaining.hash_delete(9), 'value9')
    self.assertEqual(hash_chaining.hash_get(9), None)
    self.assertEqual(hash_chaining.hash_get(2), 'value2')

unittest.main()