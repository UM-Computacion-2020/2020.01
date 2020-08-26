import unittest
from sort import Sort


class TestSort(unittest.TestCase):
    def testBubble_1(self):
        lOrdenada = Sort().BubbleSort([36, 71, 16, 21, 73, 9, 0, 40, 66, 7])
        self.assertEqual(lOrdenada, [0, 7, 9, 16, 21, 36, 40, 66, 71, 73])

    def testBubble_2(self):
        lOrdenada = Sort().BubbleSort([0, 2, 23, 4, 2, 8, 1, 25, 6, 9])
        self.assertEqual(lOrdenada, [0, 1, 2, 2, 4, 6, 8, 9, 23, 25])

    def testBubble_3(self):
        lOrdenada = Sort().BubbleSort([5, 0, 15, 25, 21, 35, 40, 25, 6, 9])
        self.assertEqual(lOrdenada, [0, 5, 6, 9, 15, 21, 25, 25, 35, 40])

    def testBubble_4(self):
        lOrdenada = Sort().BubbleSort([1, 4, 0, 2, 50, 49])
        self.assertEqual(lOrdenada, [0, 1, 2, 4, 49, 50])


if __name__ == "__main__":
    unittest.main()
