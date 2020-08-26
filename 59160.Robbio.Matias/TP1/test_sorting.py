import unittest
from sorting import Sort


class TestBubbleSort(unittest.TestCase):
    def test1(self):
        lista1 = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        sort_lista = Sort.BubbleSort(self,lista1)
        self.assertEqual(sort_lista,[0,7,9,16,21,36,40,66,71,73])

    def test2(self):
        lista2 = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        sort_lista = Sort.BubbleSort(self,lista2)
        self.assertEqual(sort_lista,[0,1,2,2,4,6,8,9,23,25])

    def test3(self):
        lista3 = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
        sort_lista = Sort.BubbleSort(self,lista3)
        self.assertEqual(sort_lista,[0,5,6,9,15,21,25,25,35,40])

if __name__ == '__main__':
    unittest.main()
