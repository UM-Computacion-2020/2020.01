import unittest
from roman_numbers import roman_to_decimal


class TestRomanNumbers(unittest.TestCase):
    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)

    def test_roman_II_to_decimal(self):
        decimal_number = roman_to_decimal('II')
        self.assertEqual(decimal_number, 2)

    def test_roman_III_to_decimal(self):
        decimal_number = roman_to_decimal('III')
        self.assertEqual(decimal_number, 3)

    def test_roman_IV_to_decimal(self):
        decimal_number = roman_to_decimal('IV')
        self.assertEqual(decimal_number, 4)

    def test_roman_V_to_decimal(self):
        decimal_number = roman_to_decimal('V')
        self.assertEqual(decimal_number, 5)

    def test_roman_VI_to_decimal(self):
        decimal_number = roman_to_decimal('VI')
        self.assertEqual(decimal_number, 6)

    def test_roman_VII_to_decimal(self):
        decimal_number = roman_to_decimal('VII')
        self.assertEqual(decimal_number, 7)

    def test_roman_VIII_to_decimal(self):
        decimal_number = roman_to_decimal('VIII')
        self.assertEqual(decimal_number, 8)

    def test_roman_IX_to_decimal(self):
        decimal_number = roman_to_decimal('IX')
        self.assertEqual(decimal_number, 9)

    def test_roman_X_to_decimal(self):
        decimal_number = roman_to_decimal('X')
        self.assertEqual(decimal_number, 10)

if __name__ == '__main__':
    unittest.main()
