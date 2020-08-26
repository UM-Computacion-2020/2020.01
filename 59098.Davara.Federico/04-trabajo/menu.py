from persona import Persona
from serviciopersona import Serviciopersona

class App:
    def menu_persona(self):
        print("\n\n\tMENU - Persona")
        print("\n1.\tListar personas")
        print("2.\tAgregar una persona")
        print("3.\tModificar una persona")
        print("4.\tEliminar una persona")
        print("  \tSalir (otra tecla)")
        return int(input("\n\tElija una opción: "))

if __name__ == '__main__':   
    app = App()
    serviciopersona = Serviciopersona()
    
    while True:
        opcion_persona = app.menu_persona()
        
        if opcion_persona == 1:
            listPerson = serviciopersona.get_personList()
            for key in listPerson:
                print("legajo: %s -> %s" % (key, listPerson[key]))
        
        if opcion_persona == 2:
            p = Persona()
            p.nombre = input("Ingrese Nombre: ")
            p.apellido = input("Ingrese apellido: ")
            p.edad = int(input("Ingrese edad: "))
            serviciopersona.add_person(p)
        
        if opcion_persona == 3:
            key = int(input("Ingreso legajo"))
            p = Persona
            p.nombre = input("Ingrese Nombre: ")
            p._apellido = input("Ingrese Apellido: ")
            p.edad = int(input("Ingrese edad: "))
            serviciopersona.update_person(key, p)
        if opcion_persona == 4:
            p = Persona()
            key = int(input("Ingrese legajo de la persona: "))
            serviciopersona.delete_person(key)    

        if opcion_persona < 1 or opcion_persona > 4:
            break