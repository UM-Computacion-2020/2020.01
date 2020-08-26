import unittest
from punto import Punto2D, PuntoMejorado
from parameterized import parameterized


class TestPunto(unittest.TestCase):
    @parameterized.expand([(1, 2, "(1, 2)"),
                           (-1, -2, "(-1, -2)")])
    def test_str_punto(self, x, y, string):
        p1 = Punto2D(x, y)
        self.assertEqual(p1.__str__(), string)


if __name__ == "__main__":
    unittest.main()


