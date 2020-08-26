from person import Person
from personService import PersonService


if __name__ == "__main__":
    personService = PersonService()
    print("\nMenu")
    print("0: para mostrar menú")
    print("1: para mostrar base de datos")
    print("2: para agregar personas a la base de datos")
    print("3: para modificar datos de las personas")
    print("4: para eliminar datos de una persona\n")
    while True:
        entrada = int(input("Seleccione una opción: "))
        if entrada == 0:
            print("\nMenu")
            print("0: para mostrar menú")
            print("1: para mostrar base de datos")
            print("2: para agregar una persona a la base de datos")
            print("3: para modificar datos de una persona")
            print("4: para eliminar datos de una persona\n")
        if entrada == 1:
            print("\nBase de datos\n")
            print(personService.get_personList())
            print("")
        if entrada == 2:
            nPersons = int(input("\nCuantas personas desea agregar: "))
            for i in range(nPersons):
                pi = Person()
                pi.name = input("Ingrese nombre: ")
                pi.surname = input("Ingrese apellido: ")
                pi.age = input("Ingrese edad: ")
                personService.add_person(pi)
                print("\nPersona agregada correctamente!!\n")
        if entrada == 3:
            nPersons = int(input("Cuantas personas desea modificar: "))
            for i in range(nPersons):
                key = int(input("Inserte clave de datos de persona: \n"))
                pi = Person()
                pi.name = input("Ingrese nombre: ")
                pi.surname = input("Ingrese apellido: ")
                pi.age = input("Ingrese edad: ")
                personService.update_person(key, pi)
                print("\nPersona modificada correctamente!!\n")
        if entrada == 4:
            print("Eliminar datos de persona\n")
            key = int(input("Ingrese la clave de la persona a eliminar: "))
            print(personService.delete_person(key))
            print("\nDatos eliminados correctamente\n")
