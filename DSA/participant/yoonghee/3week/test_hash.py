import unittest
import hash_table

class TestHash(unittest.TestCase):
    def setUp(self):
        self.test_array = [
            [10, 7, 17, 3, 4, 21, 6, 20, 1],
            [10, 7, 17, 3, 4, 21, 6, 20, 1, 9],
            [7, 6, 5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 6, 7],
            [3, 3, 4, 3, 6, 5, 6, 4, 3, 4, 6, 3],
            [1],
            [2, 10],
            [10, 2],
            [],
        ]


    def tearDown(self):
        del self.test_array


    def test_hash(self):
        table = hash_table.HashTable() # hash table 객체 생성

        table.__setitem__("one", 1)
        self.assertEqual(table.size, 1)
        table.push("two", 2)
        self.assertEqual(table.size, 2)
        table.push("three", 3)
        self.assertEqual(table.size, 3)
        table.push("four", 4)
        self.assertEqual(table.size, 4)
        table["four"] = 4
        self.assertEqual(table.size, 4)
        table["five"] = 5
        self.assertEqual(table.size, 5)
        table.push("six", 6)
        self.assertEqual(table.size, 6)
        table.push("seven", 7)
        self.assertEqual(table.size, 7)
        table.push("eight", 8)
        self.assertEqual(table.size, 8)

        self.assertEqual(table.is_empty(), False)
 
        self.assertEqual(table.__getitem__("two"), 2)

        table["one"] = 123
        self.assertEqual(table.size, 8)

        table.pop("three")
        self.assertEqual(table.size, 7)
        table.pop("four")
        self.assertEqual(table.size, 6)
        table.pop("five")
        self.assertEqual(table.size, 5)
	
unittest.main()