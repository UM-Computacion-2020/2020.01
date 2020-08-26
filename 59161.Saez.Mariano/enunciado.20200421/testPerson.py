import unittest
from employee import Person
from parameterized import parameterized


class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ('Mariano', 20),
        ('Jesus', 999),
        ('Mirtha', 1000)
    ])
    def test_get_person(self, name, age):
        persona = Person(name, age)
        datosPersona = persona.get_person()
        self.assertEqual(datosPersona, [name, age])


if __name__ == '__main__':
    unittest.main()
