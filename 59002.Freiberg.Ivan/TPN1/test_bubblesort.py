import unittest
from sorting import Sort

class TestBubbleSort(unittest.TestCase):
    
    def test_BubbleSort1(self):
        listaOrdenada = Sort().BubbleSort([36, 71, 16, 21, 73, 9, 0, 40, 66, 7])
        self.assertEqual(listaOrdenada, [0,7,9,16,21,36,40,66,71,73])
    
    def test_BubbleSort2(self):
        listaOrdenada = Sort().BubbleSort([0, 2, 23, 4, 8, 1, 25, 6, 9])
        self.assertEqual(listaOrdenada, [0,1,2,4,6,8,9,23, 25])

    def test_BubbleSort3(self):
        listaOrdenada = Sort().BubbleSort([5, 0, 15, 25, 21, 35, 40, 6, 9])
        self.assertEqual(listaOrdenada, [0,5,6,9,15,21,25,35,40])

if __name__ == "__main__":
    unittest.main()