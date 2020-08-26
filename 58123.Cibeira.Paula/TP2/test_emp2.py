import unittest
from emp import Person
from emp import Employee


class TestEmployee(unittest.TestCase):

    def test_get_person(self):
        person = Person("Claudio", 22).get_person()
        self.assertEqual(person, ["Claudio", 22])

    def test_get_employee(self):
        employee = Employee("Claudio", 22, 30000).get_employee()
        self.assertEqual(employee, ["Claudio", 22, 30000])

    def test_pay_tax_pay(self):
        pay = Employee("Nicole", 20, 50000).pay_tax()
        self.assertEqual(pay, "Paga impuestos")

    def test_pay_tax_no_pay(self):
        nopay = Employee("Claudio", 22, 30000).pay_tax()
        self.assertEqual(nopay, "No paga impuestos")


if __name__ == "__main__":
    unittest.main()
