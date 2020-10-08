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

    def insertion_sort_precio(self, lista, tipo_orden):
        lista1 = lista.copy()
        if tipo_orden == 'ascendente':
            largo = len(lista1) - 1
            for i in range(0, largo):
                # Pasadas
                for j in range(0, largo):
                    # Comparaciones
                    if lista1[j]['_precio'] > lista1[j+1]['_precio']:
                        temporal = lista1[j]['_precio']
                        temporal1 = lista1[j]['_descripcion']
                        temporal2 = lista1[j]['_tipo']
                        lista1[j]['_precio'] = lista1[j+1]['_precio']
                        lista1[j]['_descripcion'] = lista1[j+1]['_descripcion']
                        lista1[j]['_tipo'] = lista1[j+1]['_tipo']
                        lista1[j+1]['_descripcion'] = temporal1
                        lista1[j+1]['_precio'] = temporal
                        lista1[j+1]['_tipo'] = temporal2
        if tipo_orden == 'descendente':
            largo = len(lista1) - 1
            for i in range(0, largo):
                # Pasadas
                for j in range(0, largo):
                    # Comparaciones
                    if lista1[j]['_precio'] < lista1[j+1]['_precio']:
                        temporal = lista1[j]['_precio']
                        temporal1 = lista1[j]['_descripcion']
                        temporal2 = lista1[j]['_tipo']
                        lista1[j]['_precio'] = lista1[j+1]['_precio']
                        lista1[j]['_descripcion'] = lista1[j+1]['_descripcion']
                        lista1[j]['_tipo'] = lista1[j+1]['_tipo']
                        lista1[j+1]['_descripcion'] = temporal1
                        lista1[j+1]['_precio'] = temporal
                        lista1[j+1]['_tipo'] = temporal2
        return lista1

    def busqueda_binaria(self, producto, precio_buscado):
        self.insertion_sort_precio(producto, 'ascendente')
        izq = 0
        der = len(producto) - 1
        while izq <= der:
            medio = (izq+der)//2
            if producto[medio]['_precio'] == precio_buscado:
                return producto[medio]
            elif producto[medio]['_precio'] > precio_buscado:
                der = medio - 1
            else:
                izq = medio + 1
        return - 1
