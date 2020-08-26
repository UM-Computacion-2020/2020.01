import unittest
from personService import PersonService
from repository import Repository
from person import Person
from parameterized import parameterized


class TestMain(unittest.TestCase):
    @parameterized.expand([
        ("NAHUEL", "SILVA", 19, 0),
        ("CHRISTIAN", "SILVA", 25, 1)
    ])
    def test_add_person(self, name, surname, age, clave):
        person = Person(name, surname, age)
        per2 = PersonService()
        per2.add_person(person)
        self.assertEqual(Repository.dictPerson[clave], person.__dict__)


if __name__ == "__main__":
    unittest.main()
