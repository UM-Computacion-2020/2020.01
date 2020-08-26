import unittest
from employee import Person, Employee


class TestPersonEmployeeTax(unittest.TestCase):
    def test_get_person(self):
        person1 = Person("Juan", 22)
        self.assertEqual([person1.name, person1.age], Person.get_person(person1))

    def test_get_employee(self):
        employee1 = Employee("Alicia", 25, 50000)
        self.assertEqual([employee1.name, employee1.age, employee1.salary], Employee.get_employee(employee1))

    def test_pay_tax_pay(self):
        employee2 = Employee("Pedro", 31, 45000)
        self.assertEqual("Paga impuestos", Employee.pay_tax(employee2))

    def test_pay_tax_no_pay(self):
        employee3 = Employee("María", 35, 25000)
        self.assertEqual("No paga impuestos", Employee.pay_tax(employee3))


if __name__ == '__main__':
    unittest.main()
