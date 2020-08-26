class Punto2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

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


if __name__ == "__main__":
    punto = Punto2D(1, 2)
    otro_punto = Punto2D(3, 4)

    print("%s está en el cuadrante %d" % (punto, punto.cuadrante()))
    print("%s está en el cuadrante %d" % (otro_punto, otro_punto.cuadrante()))
