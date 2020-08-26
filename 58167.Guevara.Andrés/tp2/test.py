import unittest
from employee import Person, Employee

class Test_employee(unittest.TestCase):

    def test_1_employee(self):
        self.name = "Andy"
        self.age = 20
        datos = Person.get_person(self)
        self.assertEqual(datos,["Andy", 20])

    def test_2_employee(self):
        self.name = "Andy"
        self.age = 20
        self.salary = 35000
        salario = Employee.get_employee(self)
        self.assertEqual(salario, ["Andy",20,35000])

    def test_3_employee(self):
        self.salary = 35000
        self.age = 25
        impuestos = Employee.pay_tax(self)
        self.assertEqual(impuestos,"Paga impuestos")

    def test_4_employee(self):
        self.salary = 20000
        self.age = 37
        impuestos = Employee.pay_tax(self)
        self.assertEqual(impuestos,"No paga impuestos")


if __name__=="__main__":
    unittest.main() 