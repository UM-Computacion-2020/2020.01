
import unittest
from sorting import Sort

class BubbleSortTest(unittest.TestCase):
    def test_primer_arr(self):
        primer_arr = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        bubble1 =  Sort().BubbleSort(primer_arr)
        self.assertEqual(sorted(primer_arr), bubble1)
        print(sorted(primer_arr))

    def test_segundo_arr(self):
        segundo_arr = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        bubble2 =  Sort().BubbleSort(segundo_arr)
        self.assertEqual(sorted(segundo_arr), bubble2)

    def test_tercer_arr(self):
        tercer_arr = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
        bubble3 =  Sort().BubbleSort(tercer_arr)
        self.assertEqual(sorted(tercer_arr), bubble3)

if __name__ == "__main__":
    unittest.main()
    