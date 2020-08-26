import unittest
from Roman_numbers import roman_to_decimal

class TestRomanNumbers(unittest.TestCase):
    def test_I_roman_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)

if __name__== 'main__':
    unittest.main()