import unittest
from my_sorting_library.sorter import sort_alphabetically

class TestSorter(unittest.TestCase):
    def test_sort_alphabetically(self):
        data = ["banana", "apple", "orange"]
        expected_result = ["apple", "banana", "orange"]
        self.assertEqual(sort_alphabetically(data), expected_result)

if __name__ == "__main__":
    unittest.main()
