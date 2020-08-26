import unittest
from sorting import Sort

#  [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
# [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
# [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]


def selectionSort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


class TestBubbleSort(unittest.TestCase):
    def test_list_order1(self):
        ordered = Sort().BubbleSort([36, 71, 16, 21, 73, 9, 0, 40, 66, 7])
        twin = selectionSort([36, 71, 16, 21, 73, 9, 0, 40, 66, 7])
        self.assertEqual(ordered, twin)

    def test_list_order2(self):
        ordered = Sort().BubbleSort([0, 2, 23, 4, 2, 8, 1, 25, 6, 9])
        twin = selectionSort([0, 2, 23, 4, 2, 8, 1, 25, 6, 9])
        self.assertEqual(ordered, twin)

    def test_list_order3(self):
        ordered = Sort().BubbleSort([5, 0, 15, 25, 21, 35, 40, 25, 6, 9])
        twin = selectionSort([5, 0, 15, 25, 21, 35, 40, 25, 6, 9])
        self.assertEqual(ordered, twin)


if __name__ == '__main__':
    unittest.main()
