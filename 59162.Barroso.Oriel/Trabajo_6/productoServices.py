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
        print('Diccionario sin ordenar', lista1)
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
            print('Diccionario ordenado de menor a mayor', lista1)
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
            print('Diccionario ordenado de mayor a menor', lista1)
        return lista1
