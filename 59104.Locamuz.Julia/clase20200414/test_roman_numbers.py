import unittest
from roman_numbers import roman_to_decimal

# from roman_numbers :necesito q exista archivo py que
# se llame asi
# roman_to_decimal: del archivo que se llama roman_numers
# quiero la funcion roman__to_decimal


class TestRomanNumbers(unittest.TestCase):

    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)

    def test_roman_II_to_decimal(self):
        decimal_number = roman_to_decimal('II')
        self.assertEqual(decimal_number, 2)

# clase en lenguaje d prog. una plantilla
# unico que q se empieza con maysucula las class LaClaseAsi
# class NombreDeClase(unittest.TestCase):  siempre asi
# toda las funciones que estan adentro de una clase por una
# cuestion sintactica deben tener como primer parametro (self)
# despues del self cualq parametro q queramos. si o si self
# this. (java)    =  self. (py)
# assert equal esta dentro de TestCase


if __name__ == '__main__':
    unittest.main()
