import unittest
for roman_numbers import roman_to_decimal


class TestRomanNumbers(unittest.Testcase):
    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)


if __name__ == '__main__':
    unittest.main()