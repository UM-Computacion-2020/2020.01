def cuadrante(x, y):
    if x > 0 and y > 0:
        print("cuadrante 1")
    elif x < 0 and y > 0:
        print("cuadrante 2")
    elif x < 0 and y < 0:
        print("cuadrante 3")
    return print("cuadrante 4")


x = input(int("ingrese una cordenada x"))
y = input(int("ingrese una cordenada y"))
