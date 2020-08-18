class Producto():
    def __init__(self, descripcion=None, precio=0, tipo=None):
        self._descripcion = descripcion
        self._precio = precio
        self._tipo = tipo

    @property
    def descripcion(self, descripcion):
        return (self._descripcion)

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    @property
    def precio(self, precio):
        return (self._precio)

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    @property
    def tipo(self, tipo):
        return (self._tipo)

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor
