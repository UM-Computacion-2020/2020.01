from repository import Repository
from person import Person
class PersonService:

    def get_personList(self):
        print("\n--Listando Personas--\n")
        return Repository.dictionaryPerson

    def crear_Persona(self):
        name = input("Ingrese el nombre: ")
        surname = input("Ingrese el apellido: ")
        age = int(input("Ingrese la edad: "))
        return Person(name, surname, age)

    #Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person=None):
        print("\n--Agregar Persona--\n")
        if person is None:
            person = self.crear_Persona()
        key = len(Repository.dictionaryPerson)
        Repository.dictionaryPerson[key] = person.__dict__

    
    #Actualiza datos de una person del diccionario person
    #key clave diccionario 
    #object Person
    def update_person(self ,key=None , person=None):
        print("\n--Modificar Persona--\n") 
        if key is None:
            key = int(input("Ingrese una llave: "))
        if person is None:
            person = self.crear_Persona()
        Repository.dictionaryPerson[key] = person.__dict__
   
   
    #Elimina persona segun key del dic person
    def delete_person(self ,key=None):
        print("\n--Eliminar Persona--\n")
        if key is None:
            key = int(input("Ingrese una llave: "))
        del Repository.dictionaryPerson[key]

       

