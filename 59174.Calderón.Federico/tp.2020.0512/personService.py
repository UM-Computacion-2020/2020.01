from repository import Repository


class PersonService:

    def get_personList(self):
        return Repository().person

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person_parameter):
        key = -1
        for lastkey in Repository.person:
            key = lastkey
        key = key + 1
        Repository.person[key] = person_parameter.get_person()

    def update_person(self, key, person_parameter):
        Repository.person[key] = person_parameter.get_person()

    def delete_person(self, key):
        del(Repository.person[key])
