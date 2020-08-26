import unittest
from employee import Person, Employee

class TestEmployee(unittest.TestCase):
    def test_empleado_1(self):
        self.name = "Federico"
        self.age = 19
        datos = Person.get_person(self)
        self.assertEquals(datos,["Federico", 19])
    
    def test_empleado_2(self):
        self.name = "Federico"
        self.age = 19
        self.salary= 30000
        salario = Employee.get_employee(self)
        self.assertEquals(salario,["Federico", 19, 30000])
    
    def test_pay_tax_employee(self):
        self.salary = 35000
        self.age = 30
        tax = Employee.pay_tax(self)
        self.assertEqual(tax,"Paga impuestos")
    
    def test_pay_tax_employee_1(self):
        self.salary = 25000
        self.age = 35
        tax = Employee.pay_tax(self)
        self.assertEqual(tax,"No paga impuestos") 

if __name__ == "__main__":
    unittest.main()