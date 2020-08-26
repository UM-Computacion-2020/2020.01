import unittest
from personService import PersonService
from person import Person
from repository import Repository
from parameterized import parameterized


class TestPersonService (unittest.TestCase):
    @parameterized.expand([
        ('Federico', 'Gonzales', 20, 0),
        ("Claudio", "Pico", 33, 1)
    ])
    def test_add_person(self, name, surname, age, key):
        person = Person(name, surname, age, key)
        personservice = PersonService()
        personservice.add_person(person)
        self.assertEqual(Repository.person[key], person.__dict__)


if __name__ == "__main__":
    unittest.main()
