from repository import Repository
from person import Person


class PersonService:

    def get_personList(self):
        return Repository.person

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person):
        print("Agregando...")
        key = len(Repository.person)
        Repository.person[key] = (person._name, person._surname,
                                  person._age)

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_person(self, key, person):
        print("Modificando...")
        key = len(Repository.person)
        key = 0
        Repository.person[key] = (person._name, person._surname,
                                  person._age)

    # Elimina persona segun key del dic person
    def delete_person(self, key):
        print("Eliminando...")
        key = 2
        del Repository.person[key]


if __name__ == '__main__':

    personService = PersonService()
    p1 = Person()
    p1._name = 'federico'.upper()
    p1._surname = 'gonzalez'.upper()
    p1._age = '20'.upper()
    personService.add_person(p1)

    p2 = Person()
    p2._name = 'claudio'.upper()
    p2._surname = 'pico'.upper()
    p2._age = '30'.upper()
    personService.add_person(p2)

    p3 = Person()
    p3._name = 'nicolas'.upper()
    p3._surname = 'pico'.upper()
    p3._age = '40'.upper()
    personService.add_person(p3)

    print(personService.get_personList())

    # ACTUALIZAR
    #
    #
    personService = PersonService()
    p4 = Person()
    p4._name = 'federico'.upper()
    p4._surname = 'gonzalez'.upper()
    p4._age = '30'.upper()
    key = 0
    personService.update_person(0, p4)

    print(personService.get_personList())

    personService.delete_person(2)

    print(personService.get_personList())
