import unittest
from administracion import administracion
from employee import Employee, Person
from parametized import parametized

class TestAdministracion(unittest.TestCase):
    @parametized.expand([
    ({"name": "Franco", "surname": "Trifiro", "age": 20, "phone": 2615870558, salary:30000}),
    ({"name": "Franco", "surname": "Trifiro", "age": 20, "phone": 2615870558, salary:20000}),
    ])

    def test_add_employee(self, name, surname, age, phone, legajo):
        employee = Employee (name, surname, age, phone, salary, legajo)
        adm = administracion()
        adm.test_add_employee(employee.get_employee())
        self.assertEqual(adm, employee)

if __name__ == "__main__":
    unittest.main()