import unittest
from sorting import Sort


class BubbleSortTest(unittest.TestCase):
    def testArr1(self):
        arr1 = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        bubble1 = Sort().BubbleSort(arr1)
        self.assertEqual(insertionSort(arr1), bubble1)

        def testArr2(self):
            arr2 = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
            bubble2 = Sort().BubbleSort(arr2)
            self.assertEqual(insertionSort(arr2), bubble2)

        def testArr3(self):
            arr3 = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
            bubble3 = Sort().BubbleSort(arr3)
            self.assertEqual(insertionSort(arr3), bubble3)


def insertionSort(arr):
    for j in range(1, len(arr)):
        value = arr[j]
        i = j-1
        while i >= 0 and arr[i] > value:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = value
    return arr


if __name__ == "__main__":
    unittest.main()
