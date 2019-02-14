import unittest
import sort

class TestSort(unittest.TestCase):
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


    def test_bubble(self):
        for array in self.test_array:
            self.assertEqual(sort.sort_bubble_start(array), sorted(array))


    def test_insertion(self):
        for array in self.test_array:
            self.assertEqual(sort.sort_insert(array), sorted(array))


    def test_selection(self):
        for array in self.test_array:
            self.assertEqual(sort.sort_select(array), sorted(array))


unittest.main()