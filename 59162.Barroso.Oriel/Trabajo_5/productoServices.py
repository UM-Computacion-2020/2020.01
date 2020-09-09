from repositorios import Repositorios


class ProductoService():
    def get_productosList(self):
        return Repositorios.productosList

    def add_producto(self, producto):
        lk = -1
        for k in Repositorios.productosList:
            lk = k
        productoKey = lk + 1
        Repositorios.productosList[productoKey] = producto.__dict__
        return productoKey

    def change_producto(self, key, producto):
        if key not in Repositorios.productosList:
            raise ValueError
        Repositorios.productosList.update({key: producto.__dict__})

    def delete_producto(self, key):
        if key not in Repositorios.productosList:
            raise ValueError
        del Repositorios.productosList[key]
