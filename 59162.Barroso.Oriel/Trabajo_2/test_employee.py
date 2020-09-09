import unittest
from classes import Employee, Person

class test_classes(unittest.TestCase):
    def test_get_employee(self):
        self.nombre = "Oriel"
        self.age = 23
        self.salary = 32000
        emp1 = Employee.get_employee(self)
        self.assertEqual(emp1, ["Oriel", 23, 32000])

    def test_pay_taxes(self):
        self.age = 48
        self.salary = 50000
        imp1 = Employee.pay_tax(self)
        self.assertEqual(imp1, "Paga impuestos")

    def test_no_pay_taxes(self):
        self.age = 23
        self.salary = 31999
        imp2 = Employee.pay_tax(self)
        self.assertEqual(imp2, "No paga impuestos")


if __name__ == "__main__":
    unittest.main()
