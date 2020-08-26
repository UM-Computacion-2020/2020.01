import unittest
from employee import Person, Employee

class PersonTest(unittest.TestCase):
    def test_get_person (self):
        self.name = "Santiago"
        self.age = 19
        person = Person.get_person(self)
        self.assertEqual(person, ["Santiago", 19])

class EmployeeTest (unittest.TestCase):
    def test_get_employee (self):
        self.name = "Santiago"
        self.age = 19
        self.salary = 29000
        employee = Employee.get_employee(self)
        self.assertEqual (employee, ["Santiago", 19, 29000])

    def test_pay_taxes (self):
        self.salary = 40000
        self.age = 19
        taxes = Employee.pay_tax(self)
        self.assertEqual(taxes, "Paga impuestos")

    def test_doesnt_pay_tax (self):
        self.salary = 20000
        self.age = 19
        taxes = Employee.pay_tax(self)
        self.assertEqual (taxes, "No paga impuestos")


if __name__ == "__main__":
    unittest.main()
