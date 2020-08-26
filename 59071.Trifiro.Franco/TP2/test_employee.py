import unittest
from employee import Person
from employee import Employee

class TestPerson(unittest.TestCase):
    def test_get_person(self):
        self.name = "Franco"
        self.age = 20
        datosperson = Person.get_person(self)
        self.assertEqual(datosperson, ["Franco", 20])

class TestEmployee(unittest.TestCase):
    def test_get_employee(self):
        self.name = "Franco"
        self.age = 20
        self.salary = 3000
        employee = Employee.get_employee(self)
        self.assertEqual(employee, ["Franco", 20, 3000])

    def test_pay_tax_pay(self):
        self.age = 20
        self.salary = 4000
        taxpay = Employee.pay_tax(self)
        self.assertEqual(taxpay, "Paga impuestos")

    def test_pay_tax_no_pay(self):
        self.age = 20
        self.salary = 2000
        taxnopay = Employee.pay_tax(self)
        self.assertEqual(taxnopay, "No paga impuestos")
    

if __name__ == "_main_":
    unittest.main()

