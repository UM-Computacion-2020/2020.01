from producto import Producto
from productoServices import ProductoService


class Menu():
    def menu_product(self):
        print("""\n\t1 > Ver productos
        2 > Agregar Producto
        3 > Modificar Producto
        4 > Eliminar Producto
        5 > Salir
        """)
        return int(input("\tElija una opcion: "))


if __name__ == "__main__":
    m = Menu()
    system = ProductoService()
    while True:
        election = m.menu_product()
        if election == 1:
            t = system.get_productosList()
            print("\n\tLos productos son: \n\t{}".format(t))
        if election == 2:
            product = Producto()
            product.descripcion = input("\n\tAgrega una descripcion: ")
            product.precio = int(input("\tAgrega un precio: "))
            product.tipo = input("\tAgrega el tipo: ")
            system.add_producto(product)
        if election == 3:
            product = Producto()
            key = int(input("\n\tProporcione el codigo: "))
            product.descripcion = input("\tAgrega una descripcion: ")
            product.precio = int(input("\tAgrega un precio: "))
            product.tipo = input("\tAgrega el tipo: ")
            system.change_producto(key, product)
        if election == 4:
            product = Producto()
            key = int(input("\n\t¿Que producto desea eliminar?: "))
            system.delete_producto(key)
        if election < 1 or election > 5:
            print("""\t\t>>>Opcion no encontrada
                 intenta con las opciones mostradas en pantalla<<<""")
        if election == 5:
            print("\n\tHasta luego...")
            break
