import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 2), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Denominator cannot be zero\\."):
            self.calculator.divide(6, 0)

    def test_add_with_negative_numbers(self):
        self.assertEqual(self.calculator.add(-3, -2), -5)
        self.assertEqual(self.calculator.add(-3, 2), -1)

    def test_subtract_with_negative_numbers(self):
        self.assertEqual(self.calculator.subtract(-3, -2), -1)
        self.assertEqual(self.calculator.subtract(3, -2), 5)

    def test_multiply_by_zero_and_negative_number(self):
        self.assertEqual(self.calculator.multiply(7, 0), 0)
        self.assertEqual(self.calculator.multiply(-3, 2), -6)

    def test_divide_zero_and_fractional_result(self):
        self.assertEqual(self.calculator.divide(0, 5), 0)
        self.assertAlmostEqual(self.calculator.divide(1, 3), 1 / 3)

    def test_divide_by_negative_number(self):
        self.assertEqual(self.calculator.divide(6, -2), -3)

    def test_divide_by_negative_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(6, -0.0)

# Test the modulo method with standard and negative numbers
    def test_modulo(self):
        self.assertEqual(self.calculator.modulo(10, 3), 1)
        self.assertEqual(self.calculator.modulo(-10, 3), 2)
        self.assertEqual(self.calculator.modulo(10, -3), -2)
        self.assertEqual(self.calculator.modulo(-10, -3), -1)

if __name__ == "__main__":
    unittest.main()
