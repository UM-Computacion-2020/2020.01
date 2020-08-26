class Punto2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)



if __name__ == "__main__":
    punto = Punto2D(1, 2)
    print(punto)
    otro_punto = Punto2D(3, 4)
    print(otro_punto)
