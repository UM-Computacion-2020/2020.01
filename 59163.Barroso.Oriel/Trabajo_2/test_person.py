import unittest
from classes import Person


class test_classes(unittest.TestCase):
    def test_get_person(self):
        self.name = "Oriel"
        self.age = "23"
        persona1 = Person.get_person(self)
        self.assertEqual(["Oriel", "23"], persona1)


if __name__ == "__main__":
    unittest.main()
