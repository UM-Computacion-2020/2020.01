import unittest
from person import Person, Employee

class TestPerson(unittest.TestCase):

    def test_get_person(self):
        self.name = 'Federico'
        self.age = 20
        p1 = Person.get_person(self)
        self.assertEqual(p1,['Federico',20])

class TestEmployee(unittest.TestCase):

    def test_get_employee(self):    
        self.name = 'Federico'
        self.age = 20
        self.salary = 3000
        employee = Employee.get_employee(self)
        self.assertEqual(employee, ['Federico',20,3000])

    def test_get_pay_tax(self):
        self.name = 'Federico'
        self.age = 20
        self.salary = 4500
        t = Employee.get_pay_tax(self)
        self.assertEqual(t,'Paga impuestos')

    def test_get_no_pay_tax(self):
        self.name = 'Federico'
        self.age = 40
        self.salary = 2500
        t = Employee.get_pay_tax(self)
        self.assertEqual(t,'No paga impuestos')
    

         

if __name__ == "__main__":
    unittest.main()
 