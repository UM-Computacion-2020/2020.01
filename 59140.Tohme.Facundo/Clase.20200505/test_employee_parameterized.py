import unittest 
from employee import Employee
from employee import Person
from parameterized import parameterized


class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ("Facundo", 19, "Tohme", 234565478, {"name": "Facundo", "age": 19, "surname": "Tohme", "phone": 234565478})
    ])

    def test_get_person(self, name, surname, age, phone, result):
        person1 = Person(name, surname, age, phone)
        dictPerson = person1.get_person()
        self.assertEqual(dictPerson, result)


class TestEmployee(unittest.TestCase):
    @parameterized.expand ([
        ("Facundo", 19, "Tohme, 234565478, 50000, {"name": "Facundo", "age": 19, "surname": "Tohme", "phone": 234565478, "salary": 50000})
    ])

    def test_get_employee(self, name, age, surname, phone, salary, result):
        employee = Employee(name, age, surname, phone, salary)
        dictEmployee = employee.get_employee()
        self.assertEqual(dictEmployee, result)

    @parameterized.expand([
        ("Facundo", 19, "Tohme", 234565478, 50000, "Paga impuestos"),
        ("Ivan", 20, "Freiberg", 120837432, 20000, "No paga impuestos")
    ])

    def test_pay_tax_pay(self, name, age, surname, phone, salary, result):
        employee = Employee(name, age, surname, phone, salary)
        tax = employee.pay_tax()
        self.assertEqual(tax, result)


if __name__ == "__main__":
    unittest.main()
