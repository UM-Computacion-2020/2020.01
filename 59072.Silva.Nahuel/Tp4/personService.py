from repository import Repository
from person import Person


class PersonService():

    def get_personList(self):
        print(Repository.dictPerson)

    def crearPersona(self):
        print("\n----Agregar persona----")
        name = input('Ingrese un nombre: ')
        surname = input('Ingrese un apellido: ')
        age = int(input('Ingrese una edad: '))
        return Person(name, surname, age)

    "#Agrega una persona en el diccionario person con una clave"
    def add_person(self, person=None):
        if person is None:
            person.crearPesona()
        ultimaclave = -1
        for clave in Repository.dictPerson:
            ultimaclave = clave
        ultimaclave = ultimaclave + 1
        Repository.dictPerson[ultimaclave] = person.__dict__

    "#Actualiza datos de una person del diccionario person"
    "#key clave diccionario"
    "#object Person"
    def update_person(self, clave):
        num = 1
        while num != 0:
            num2 = 1
            if num2 == 1:
                print("-----Modificando-----")

                nombre = input('Introduzca el nuevo nombre: ')
                Repository.dictPerson[clave]["_name"] = nombre.upper()
                print(Repository.dictPerson)

                apellido = input('Introduzca el nuevo apellido: ')
                Repository.dictPerson[clave]["_surname"] = apellido.upper()
                print(Repository.dictPerson)

                edad = int(input('Introduzca la nueva edad: '))
                Repository.dictPerson[clave]["_age"] = edad
                print(Repository.dictPerson)
            terminar = str(input("Quiere volver a corregirlo: "))
            if terminar == "no":
                break
    "#Elimina persona segun key del dic person"
    def delete_person(self, clave):
        del Repository.dictPerson[clave]
