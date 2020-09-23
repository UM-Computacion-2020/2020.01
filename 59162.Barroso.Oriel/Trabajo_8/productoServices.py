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
        lista_ordenada = lista.copy()
        for i in range(1, len(lista_ordenada)):
            actual = lista_ordenada[i]
            j = i
            if tipo_orden == 'ascendente':
                while j > 0 and \
                        lista_ordenada[j-1]["_precio"] > actual["_precio"]:
                    lista_ordenada[j] = lista_ordenada[j-1]
                    j = j-1
            if tipo_orden == 'descendente':
                while j > 0 and \
                        lista_ordenada[j-1]["_precio"] < actual["_precio"]:
                    lista_ordenada[j] = lista_ordenada[j-1]
                    j = j-1
            lista_ordenada[j] = actual
        return lista_ordenada

    def busqueda_binaria(self, producto, precio_buscado):
        producto = self.insertion_sort_precio(producto, 'ascendente')
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

    def get_lista_estado(self, producto, estado):
        lista = producto.copy()
        print('\n\n\nLista sin filtrar', lista)
        if estado == 'disponible':
            for k, v in producto.items():
                v = lista[k]['_estado']
                print("""Chequeando estado...
                      Estado actual > """, v)
                if v == 'vendido':
                    print('Filtrando listado...')
                    del lista[k]
                    print('Estado actual de la lista >>', lista)
        if estado == 'vendido':
            for k, v in producto.items():
                v = lista[k]['_estado']
                print("""Chequeando estado...
                      Estado actual > """, v)
                if v == 'disponible':
                    print('Filtrando listado...')
                    del lista[k]
                    print('Estado actual de la lista >>', lista)
        return lista
