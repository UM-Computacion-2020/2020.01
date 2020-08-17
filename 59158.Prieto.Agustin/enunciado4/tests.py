import unittest
from personService import PersonService
from parameterized import parameterized
from person import Person


class TestAddperson(unittest.TestCase):
    personService = PersonService()

    @parameterized.expand([
        ('Agustin', 'Prieto', 19, 0, {'_name': 'AGUSTIN', '_surname': 'PRIETO', '_age': 19}),
        ('Lebron', 'James', 39, 1, {'_name': 'LEBRON', '_surname': 'JAMES', '_age': 39}),

    ])
    def test_addperson(self, name, surname, age, key, pers):
        personService = PersonService()
        pers1 = Person(name, surname, age)
        pers1 = Person.get_person(pers1)
        personService.add_person(pers1)
        self.assertEqual(personService.lista[key], pers)

    @parameterized.expand([
        (0, ),
        (1, )
    ])
    def test_bupdate_name(self, key):
        personService = PersonService()
        personService.update_person_name(key, 'Juan')
        self.assertEqual(personService.lista[key]['_name'], 'JUAN')

    @parameterized.expand([
        (0, ),
        (1, )
    ])
    def test_ba_update_surname(self, key):
        personService = PersonService()
        personService.update_person_surname(key, 'rodriguez')
        self.assertEqual(personService.lista[key]['_surname'], 'RODRIGUEZ')

    @parameterized.expand([
        (0, ),
        (1, )
    ])
    def test_bab_update_age(self, key):
        personService = PersonService()
        personService.update_person_age(key, 15)
        self.assertEqual(personService.lista[key]['_age'], 15)

    @parameterized.expand([
        (0, ),
        (1, )
    ])
    def test_del_person(self, key):
        personService = PersonService()
        personService.delete_person(key)
        self.assertNotIn(key, personService.lista.keys())


if __name__ == '__main__':
    unittest.main()
