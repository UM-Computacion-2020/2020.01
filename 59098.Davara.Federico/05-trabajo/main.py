from producto import Producto
from productoServices import ProductoService


class Menu():
    def menu_productos(self):
        print("""\n\t1 > Ver productos
        2 > Agregar un Producto
        3 > Modificar un Producto
        4 > Eliminar un Producto
        5 > Salir
        """)
        return int(input("\tSeleccionar una opción: "))


if __name__ == "__main__":
    main = Menu()
    sistema = ProductoService()
    while True:
        seleccion = main.menu_productos()
        if seleccion == 1:
            t = sistema.get_productosList()
            print("\n\tLos productos son: \n\t{}".format(t))
        if seleccion == 2:
            productos = Producto()
            productos.descripcion = input("\n\tAgregar una descripcion del producto: ")
            productos.precio = int(input("\tAgregar un precio del producto: "))
            productos.tipo = input("\tAgregar el tipo de producto: ")
            sistema.add_producto(productos)
        if seleccion == 3:
            productos = Producto()
            key = int(input("\n\tProporcione el codigo del producto: "))
            productos.descripcion = input("\tAgregar una descripcion sobre el producto: ")
            productos.precio = int(input("\tAgregar un precio para el producto: "))
            productos.tipo = input("\tAgregar el tipo de producto: ")
            sistema.update_producto(key, productos)
        if seleccion == 4:
            productos = Producto()
            key = int(input("\n\t¿Cual es el producto que se desea eliminar?: "))
            sistema.delete_producto(key)
        if seleccion < 1 or seleccion > 5:
            print("""\t\t>>>Esta opción no es valida 
                por favor utilise una de las opciones que se encuentran en pantalla<<<""")
        if seleccion == 5:
            print("\n\tFinalizando programa...")
            break