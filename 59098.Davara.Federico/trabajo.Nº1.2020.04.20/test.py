import unittest
from sorting import sort

class BubbleSortTest(unittest.TestCase):
    def testArray1(self):
        array1 = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        bubble1 = sort().BubbleSort(array1)
        self.assertEqual(array1, bubble1)

    def testArray2(self):
        array2 = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        bubble2 = sort().BubbleSort(array2)
        self.assertEqual(array2, bubble2)

    def testArray3(self):
        array3 = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
        bubble3 = sort().BubbleSort(array3)
        self.assertEqual(array3, bubble3)

if __name__ == "__main__":
    unittest.main()