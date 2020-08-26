class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)


class PuntoMejorado():
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return 0
        if self.x > 0 and self.y > 0:
            return 1
        if self.x < 0 and self.y > 0:
            return 2
        if self.x < 0 and self.y < 0:
            return 3
        return 4


class TestPunto(unittest.TestCase):
    @paramerizad.expand([(4, 5, "(4, 5)")])
    def test_str_punto(self):
        punto = Punto(4, 5)
        self.assertEqual(punto.__str___())


if __name__ == "__main__":
    punto = Punto2D(1, 2)
    otro_punto = Punto2D(-3, -4)
    print("%s esta en el cuadrante %d" % (punto, punto.cuadrante()))
    print("%s esta en el cuadrante %d" % (otro_puno)
