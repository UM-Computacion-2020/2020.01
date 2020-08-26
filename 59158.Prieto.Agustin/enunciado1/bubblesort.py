import unittest
from sorting import Sort


class TestBubbleSort(unittest.TestCase):
    def test_array(self):
        array1 = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        sortArray = Sort.BubbleSort(self, array1)
        self.assertEqual(sortArray, [0, 7, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_array2(self):
        array2 = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        sortArray = Sort.BubbleSort(self, array2)
        self.assertEqual(sortArray, [0, 1, 2, 2, 4, 6, 8, 9, 23, 25])
     
    def test_array3(self):
        array3 = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
        sortArray = Sort.BubbleSort(self, array3)
        self.assertEqual(sortArray, [0, 5, 6, 9, 15, 21, 25, 25, 35, 40])


if __name__ == '__main__':
    unittest.main()
