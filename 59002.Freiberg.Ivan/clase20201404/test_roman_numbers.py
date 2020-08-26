import unittest
from roman_numbers import roman_to_decimal


class TestRomanNumbers(unittest.TestCase):
    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)
       
    def test_roman_II_todecimal(self):
        decimal_number = roman_to_decimal('II')
        self.assertEqual(decimal_number,2)



if __name__ == '_main_':
    unittest.main()
