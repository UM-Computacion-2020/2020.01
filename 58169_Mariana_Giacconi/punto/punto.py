class Punto():
    def __init__(self, a=0, b=0):
        self.a= a
        self.b= b
    def __str__(self):
        return "(%d, %d)" % (self.a, self.b)
    

class PuntoMejorado(Punto):
    def cuadrante(self):
        print(a)
    
        if a > 0 and b > 0:
            print("cuadrante 1")
        elif a < 0 and b > 0:
            print("cuadrante 2")
        elif a < 0 and b < 0:
            print("cuadrante 3")
        else:
            print("cuadrante 4")



if __name__ == "__main__":
    a = int(input("ingrese coordenada a"))
    b = int(input("ingrese coordenada b"))
    punto = PuntoMejorado(a, b)
    print(punto)
    print(punto.cuadrante())