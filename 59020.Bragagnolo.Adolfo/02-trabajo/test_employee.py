import unittest
from employee import Person
from employee import Employee

class TestPerson(unittest.TestCase):
    def test_get_person(self):
        person = Person("Adolfo", 19).get_person()
        self.assertEqual(person, ["Adolfo",19])

class TestEmployee(unittest.TestCase):
    def test_get_employee(self):
        employe = Employee("Adolfo", 19, 20000).get_employee()
        self.assertEqual(employe, ["Adolfo", 19, 20000])

class TestPayTax(unittest.TestCase):
    def test_get_pay_tax_pay(self):
        señor = Employee("Adolfo", 28, 40000).pay_tax()
        self.assertEqual(señor, "Paga impuestos")


class TestNoPayTax(unittest.TestCase):
    def test_gat_pay_tax_no_pay(self):
        señor = Employee("Francisco", 43, 20000).pay_tax()
        self.assertEqual(señor, "No paga impuestos")


if __name__=="__main__":
    unittest.main()

