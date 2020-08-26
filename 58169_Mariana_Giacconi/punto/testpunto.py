import unittest
from punto import Punto, PuntoMejorado
from parameterized import parameterized

class TestPunto(unittest.TestCase):
    @parameterized.expand([
        (4, 5, "(4, 5)"), 
        (-1, -2, "(-1, -2)"),
        (-3, -1, "(-3, -1)"),
        (8, 5, "(8, 5)"),
        (-5, 5, "(-5, 5)"),
        ])
    def test_str_punto(self, x, y, string):
        punto = Punto(x, y)
        self.assertEqual(punto.__str__(), string)

if __name__ == "__main__":
    unittest.main()