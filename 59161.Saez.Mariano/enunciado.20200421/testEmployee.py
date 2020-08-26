import unittest
from employee import Employee
from parameterized import parameterized


class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ('Mariano', 20, 2000),
        ('Jesus', 999, 300),
        ('Mirtha', 1000, 9999)
    ])
    def test_get_employee(self, name, age, salary):
        empleado = Employee(name, age, salary)
        datosEmpleado = empleado.get_employee()
        self.assertEqual(datosEmpleado, [name, age, salary])

    @parameterized.expand([
        ('Mariano', 20, 32165),
        ('Jesus', 20, 30001),
        ('Mirtha', 15, 50000)
    ])
    def test_tax_pay(self, name, age, salary):
        empleado = Employee(name, age, salary)
        salarioEmpleado = empleado.pay_tax()
        self.assertEqual(salarioEmpleado, "Paga impuestos")

    @parameterized.expand([
        ('Mariano', 33, 32165),
        ('Jesus', 20, 29999),
        ('Mirtha', 99, 29999)
    ])
    def test_tax_no_pay(self, name, age, salary):
        empleado = Employee(name, age, salary)
        salarioEmpleado = empleado.pay_tax()
        self.assertEqual(salarioEmpleado, "No paga impuestos")


if __name__ == '__main__':
    unittest.main()
