class Person():
    def __init__(self, key=0, nombre="", apellido="", edad=0):
        self.key = key
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return "%d %s %s %d" % (self.key, self.nombre, self.apellido,
                                self.edad)

    def ingresar(self, key):
        print("Ingresando Person")
        self.key = key
        self.nombre = input("Ingrese nombre: ").upper()
        self.apellido = input("Ingrese apellido : ").upper()
        self.edad = int(input("Ingrese edad: "))

    def modificar(self, modificar):
        print("modificando Person")
        if modificar == 1:
            self.nombre = input("Ingrese nombre: ").upper()
        elif modificar == 2:
            self.apellido = input("Ingrese apellido : ").upper()
        elif modificar == 3:
            self.edad = int(input("Ingrese edad: "))

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value.upper()

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value.upper()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value
