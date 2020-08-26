import unittest
from employee import Person, Employee



class Test_employee(unittest.TestCase):


    def test_1_employee(self):
        self.name = "Enzo"
        self.age = 23
        datos = Person.get_person(self)
        self.assertEqual(datos,["Enzo", 23])
    
    def test_2_employee(self):
        self.name = "Enzo"
        self.age = 23
        self.salary = 50000
        salario = Employee.get_employee(self)
        self.assertEqual(salario, ["Enzo",23,50000])

    def test_3_employee(self):
        self.salary = 35000
        self.age = 30
        impuestos = Employee.pay_tax(self)
        self.assertEqual(impuestos,"Paga impuestos")
    
    def test_4_employee(self):
        self.salary = 25000
        self.age = 35
        impuestos = Employee.pay_tax(self)
        self.assertEqual(impuestos,"No paga impuestos")






if __name__=="__main__":
    unittest.main()