class Clase():
    def __init__(self, edad=17): #constructor (siempre una funcion se arranca con self)
        self.edad = edad 
        #si no especifico self no aparecera en el diccionario

    #getter y setter con property
    @property #'disfraza' el atributo con el nombre de una funcion
    def edad(self):
        return self.__edad
                                #las funciones deben llamares igual
    @edad.setter
    def edad(self, value): #value significa q ahi va a ir un valor (se puede llamar de otra forma. Por ejemplo: valor)
        if value < 15:
            raise ValueError("Edad no permitida")
        self.__edad = value #la palabra edad deja de ser un atributo; el atributo va a ser __edad
        #el doble _ es la forma especial para q python tome el atributo como si fuera oculto

if __name__ == "__main__":
    objeto1 = Clase()
    infinito = True
    while infinito:
        try:
            objeto1.edad = int(input("Ingrese edad: "))
            infinito = False
        except ValueError as e:
            print(e)