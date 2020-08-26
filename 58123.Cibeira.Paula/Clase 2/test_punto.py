import unittest
from punto import Punto, PuntoMejorado
from parameterized import parameterized


class TestPunto(unittest.TestCase):
    @parameterized.expand([
        (4, 5, "(4, 5)"),
        (-1, -2, "(-1, -2)"),
        ])

    def test_str_punto(self):
        punto = Punto(4, 5)
        self.assertEqual(punto.__str__(), "(4, 5")

  if __name__ == "__main__":
    unittest.main()