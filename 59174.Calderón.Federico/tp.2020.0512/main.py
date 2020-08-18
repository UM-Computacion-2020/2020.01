from person import Person
from personService import PersonService


if __name__ == '__main__':
    personService = PersonService()

    # Agregamos una persona
    p1 = Person()
    p1.name = 'federico'
    p1.surname = 'gonzalez'
    p1.age = '20'
    personService.add_person(p1)
    # Agregamos una persona
    p2 = Person()
    p2.name = 'claudio'
    p2.surname = 'pico'
    p2.age = '33'
    personService.add_person(p2)

    # Agregamos al hermano **********************
    p3 = Person()
    p3.name = 'nicolas'
    p3.surname = 'pico'
    p3.age = 40
    personService.add_person(p3)
    print(personService.get_personList())
    # Update fEDERICO
    p4 = Person()
    p4.name = 'federico'
    p4.surname = 'gonzalez'
    p4.age = '30'
    personService.update_person(0, p4)
    print(personService.get_personList())
    # Elimina persona segun key del dic person
    personService.delete_person(2)
    print(personService.get_personList())
