class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)


class PuntoMejorado(Punto2D):
    def cuadrante(self):
        if self.x == 0 or self.y == 0:
            return 0
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        return 4


if __name__ == '__main__':
    punto = Punto2D(1, 2)
    otro_punto = PuntoMejorado(2, 4)

    print(punto)
    print(otro_punto, 'esta en el cuadrante', otro_punto.cuadrante())
