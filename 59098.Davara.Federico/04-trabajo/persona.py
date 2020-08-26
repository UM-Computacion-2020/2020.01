class Persona:
    def __init__(self, nombre=None, apellido=None, edad=None):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre.upper()

    # deleting
    @nombre.deleter 
    def nombre(self):
        del self._nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido.upper()

    # deleting
    @apellido.deleter 
    def apellido(self):
        del self._apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @edad.deleter 
    def edad(self):
        del self._edad
