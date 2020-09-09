from person import Person
from personService import PersonService

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