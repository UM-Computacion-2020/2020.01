from producto import Producto
from productoServices import ProductoService


class App():
    def menuApp(self):
        print("1. Agregar producto")
        print("2. Listar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        return int(input("Elija una opcion: "))


if __name__ == '__main__':
    app = App()
    productoService = ProductoService()

    while True:
        opcionElegida = app.menuApp()
        if opcionElegida == 1:
            productoService.add_producto()

        if opcionElegida == 2:
            print(productoService.get_productosList())

        if opcionElegida == 3:
            productoService.update_producto()

        if opcionElegida == 4:
            productoService.delete_producto()