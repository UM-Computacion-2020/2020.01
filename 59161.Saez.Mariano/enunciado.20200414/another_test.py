import unittest
from sorting import Sort

# Casos:
# [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
# [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
# [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]

# En este ejemplo se ultiliza un metodo que comprueba
# si un objeto es mayor o igual que otro


class TestBubbleSort(unittest.TestCase):
    def test_list_order1(self):
        unordered = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7, 7]
        ordered = Sort().BubbleSort(unordered)
        for i in range(len(unordered)-1):
            self.assertGreaterEqual(ordered[i+1], ordered[i])


if __name__ == '__main__':
    unittest.main()
