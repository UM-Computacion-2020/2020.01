class Producto():
    def __init__(self, descripcion=None, precio=0,
                 tipo=None, estado='disponible'):
        self._descripcion = descripcion
        self._precio = precio
        self._tipo = tipo
        self._estado = estado
        if self._estado == 'disponible':
            self._estado = estado
        else:
            self._estado == 'vendido'

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if self._precio >= 0:
            self._precio = valor
        else:
            raise ValueError

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor
