import unittest
from employee import Employee

class testEmployee(unittest.TestCase):
    def test_get_employee(self):
        persona = Employee("Claudio",32,3000)
        self.assertEqual(Employee.get_employee(persona),["Claudio",32,3000])

    def test_pay_tax_pay(self):
        persona = Employee("Claudio",30,35000)
        self.assertEqual(Employee.pay_tax(persona),"Paga impuestos")

    def test_pay_tax_no_pay(self):
        persona = Employee("Claudio",33,3000)
        self.assertEqual(Employee.pay_tax(persona),"No paga impuestos")


if __name__ == "__main__":
    unittest.main()





        
