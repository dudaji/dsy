import unittest
import bubble_sort
import insertion_sort
import selection_sort
import merge_sort
import quick_sort

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
            self.assertEqual(bubble_sort.sort(array), sorted(array))


    def test_insertion(self):
        for array in self.test_array:
            self.assertEqual(insertion_sort.sort(array), sorted(array))


    def test_selection(self):
        for array in self.test_array:
            self.assertEqual(selection_sort.sort(array), sorted(array))


    def test_merge(self):
        for array in self.test_array:
            self.assertEqual(merge_sort.sort(array), sorted(array))


    def test_quick(self):
        for array in self.test_array:
            self.assertEqual(quick_sort.sort(array), sorted(array))

unittest.main()