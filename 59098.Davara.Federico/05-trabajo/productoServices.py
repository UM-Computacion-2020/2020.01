from repositorios import Repositorios

class ProductoService:

    def get_productosList(self):
        return Repositorios.productosList


    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        producto_new = int(lastKey) + 1
        Repositorios.productosList[producto_new] = producto.__dict__
        return producto_new

    def update_producto(self, key, producto):
        if key not in Repositorios.productosList:
            raise ValueError("El producto no existe")
        Repositorios.productosList.update({key: producto.__dict__})

    def delete_producto(self, key):
        if key not in Repositorios.productosList:
            raise ValueError("El producto a elminar no existe")
        del Repositorios.productosList[key]