from repositorios import Repositorios
from producto import Producto


class ProductoService:

    def add_producto(self, producto):
        print("\n--Agrgando Productos--\n")
        prodkey = -1
        for key in Repositorios.productosList:
            prodkey = key
        newKey = int(prodkey) + 1
        Repositorios.productosList[newKey] = producto.__dict__
        return newKey

    def delete_producto(self, key):
        print("\n--Eliminando Productos--\n")
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
        else:
            raise ValueError('No existe la key')

    def get_productosList(self):
        print("\n--Listando Productos--\n")
        return Repositorios.productosList

    def update_producto(self, key, producto):
        print("\n--Actualizando Productos--\n")
        if key in Repositorios.productosList:
            Repositorios.productosList[key] = producto.__dict__
        else:
            raise ValueError('No existe legajo')
