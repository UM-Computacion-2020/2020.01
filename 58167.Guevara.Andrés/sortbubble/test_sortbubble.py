import unittest
from sorting import Sort

class TestBubbleSorting(unittest.TestCase):
    def test_BubbleSort(self):
        arr = Sort().BubbleSort([36, 71, 16, 21, 73, 9, 0, 40, 66, 7])
        self.assertEqual(arr, [0, 7, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_1_BubbleSort(self):
        arr1 = Sort().BubbleSort([0, 2, 23, 4, 2, 8, 1, 25, 6, 9])
        self.assertEqual(arr1, [0, 1, 2, 2, 4, 6, 8, 9, 23, 25])

    def test_2_BubbleSort(self):
        arr2 = Sort().BubbleSort([5, 0, 15, 25, 21, 35, 40, 25, 6, 9]) 
        self.assertEqual(arr2, [0, 5, 6, 9, 15, 21, 25, 25, 35, 40])



if __name__ == "__main__":
    unittest.main() 