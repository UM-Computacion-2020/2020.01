from repositorio import Repositorio
from persona import Persona


class Serviciopersona:
    def get_personList(self):
        print("\n----> \tLista de personas:\n")
        return Repositorio.persona

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, persona):
        print("\n----> \tAgregando persona...")
        lastKey = -1
        for key in Repositorio.persona:
            lastKey = key
        lastKey = lastKey + 1
        Repositorio.persona[lastKey] = persona.__dict__
        print("\n----> \tAgregado.")

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_person(self, key, persona):
        Repositorio.persona[key]['_nombre'] = persona.nombre
        Repositorio.persona[key]['_apellido'] = persona.apellido
        Repositorio.persona[key]['_edad']= persona.edad
    
    # Elimina persona segun key del dic person
    def delete_person(self, key):
        del Repositorio.persona[key]