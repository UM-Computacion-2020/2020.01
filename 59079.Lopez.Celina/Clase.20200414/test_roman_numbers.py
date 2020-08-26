import unittest
from roman_numbers import roman_to_decimal


class TestRomanNumbers(unittest.TestCase):
    def test_roman_I_to_decimal(self):
        decimal_numbers = roman_to_decimal('I')
        self.assertEqual(decimal_numbers, 1)

    def test_roman_II_to_decimal(self):
        decimal_numbers = roman_to_decimal('II')
        self.assertEqual(decimal_numbers, 2)


if __name__ == '__main__':
    unittest.main()
