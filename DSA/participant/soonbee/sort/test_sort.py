import unittest
import bubble_sort
import insertion_sort
import selection_sort
import merge_sort
import quick_sort

class TestSort(unittest.TestCase):
    def setUp(self):
        self.test_arr = [
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
        del self.test_arr

    def test_bubble(self):
        for arr in self.test_arr:
            bubble_sort.sort(arr)
            self.assertEqual(arr, sorted(arr))

    def test_insertion(self):
        for arr in self.test_arr:
            insertion_sort.sort(arr)
            self.assertEqual(arr, sorted(arr))

    def test_selection(self):
        for arr in self.test_arr:
            selection_sort.sort(arr)
            self.assertEqual(arr, sorted(arr))

    def test_merge(self):
        for arr in self.test_arr:
            self.assertEqual(merge_sort.sort(arr), sorted(arr))

    def test_quick_type_a(self):
        for arr in self.test_arr:
            quick_sort.type_a(arr, 0, len(arr)-1)
            self.assertEqual(arr, sorted(arr))
    
    def test_quick_type_b(self):
        for arr in self.test_arr:
            self.assertEqual(quick_sort.type_b(arr), sorted(arr))
    
    def test_quick_type_c(self):
        for arr in self.test_arr:
            quick_sort.type_c(arr, 0, len(arr)-1)
            self.assertEqual(arr, sorted(arr))


if __name__ == "__main__":
    unittest.main()