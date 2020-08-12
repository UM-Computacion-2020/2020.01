import unittest
from personService import PersonService
from person import Person
from repository import Repository
from parameterized import parameterized


class TestPersonService(unittest.TestCase):
    @parameterized.expand([
        ("Guadalupe", "Méndez", 19, 0),
        ("Cecilia", "Gattari", 51, 1),
        ("Mariano", "Saez", 20, 2)
                            ])
    def test_add_person(self, name, surname, age, key):
        person = Person(name, surname, age)
        service = PersonService()
        service.add_person(person)
        self.assertEqual(Repository.diccionarioPerson[key], person.__dict__)


if __name__ == "__main__":
    unittest.main()
