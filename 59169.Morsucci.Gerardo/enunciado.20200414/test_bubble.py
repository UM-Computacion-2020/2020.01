import unittest
from sorting import Sort


class BubbleSortTest(unittest.TestCase):
    def testArray1(self):
        array1 = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        bubble1 = Sort().BubbleSort(array1)
        self.assertEqual(insertionSort(array1), bubble1)

    def testArray2(self):
        array2 = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        bubble2 = Sort().BubbleSort(array2)
        self.assertEqual(insertionSort(array2), bubble2)

    def testArray3(self):
        array3 = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
        bubble3 = Sort().BubbleSort(array3)
        self.assertEqual(insertionSort(array3), bubble3)

    def testArray4(self):
        array4 = [1, 1.2, 1.5, 2, 2.4, 3, 3.1, 3.01, 4]
        bubble4 = Sort().BubbleSort(array4)
        self.assertEqual(insertionSort(array4), bubble4)


def insertionSort(array):
    for j in range(1, len(array)):
        value = array[j]
        i = j - 1
        while i >= 0 and array[i] > value:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = value
    return array


if __name__ == "__main__":
    unittest.main()
