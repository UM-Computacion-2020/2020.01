from persona import Persona
from serviciopersona import Serviciopersona

if __name__ == '__main__':
    serviciopersona = Serviciopersona()

    # Agregamos una persona
    p1 = Persona()
    p1.nombre = 'federico'
    p1.apellido = 'gonzalez'
    p1.edad = '20'
    serviciopersona.add_person(p1)

    # Agregamos una persona
    p1 = Persona()
    p1.nombre = 'claudio'
    p1.apellido = 'pico'
    p1.edad = '33'
    serviciopersona.add_person(p1)

    # Agregamos al hermano
    p2 = p1
    p1.nombre = 'nicolas'
    p1.apellido = 'pico'
    p1.edad = '30'
    serviciopersona.add_person(p2)

    print(serviciopersona.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}, 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30}}

    # Actualizacion de FEDERICO
    p2.edad = 41
    serviciopersona.add_person(p2)
    
    print(serviciopersona.get_personList)
    # borrar persona
    serviciopersona.delete_person(2)

    print(serviciopersona.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}}
