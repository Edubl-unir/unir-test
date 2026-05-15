import unittest
from unittest.mock import patch
import pytest
from app.calc import Calculator, InvalidPermissions


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(2.5, 0.5), 3.0)

    def test_add_error(self):
        with self.assertRaises(TypeError):
            self.calc.add(2, "3")

    def test_substract(self):
        self.assertEqual(self.calc.substract(5, 3), 2)
        self.assertEqual(self.calc.substract(5.5, 3.0), 2.5)

    def test_substract_error(self):
        with self.assertRaises(TypeError):
            self.calc.substract(5, "3")

    @patch('app.util.validate_permissions', return_value=True)
    def test_multiply(self, mock_validate):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(2.5, 2.0), 5.0)

    @patch('app.util.validate_permissions', return_value=False)
    def test_multiply_error_permission(self, mock_validate):
        with self.assertRaises(InvalidPermissions):
            self.calc.multiply(2, 3)

    @patch('app.util.validate_permissions', return_value=True)
    def test_multiply_error_type(self, mock_validate):
        with self.assertRaises(TypeError):
            self.calc.multiply(2, "3")

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)

    def test_divide_error_zero(self):
        with self.assertRaises(TypeError):
            self.calc.divide(6, 0)

    def test_divide_error_type(self):
        with self.assertRaises(TypeError):
            self.calc.divide(6, "2")

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8.0)
        self.assertEqual(self.calc.power(2.5, 2), 6.25)

    def test_power_error(self):
        with self.assertRaises(TypeError):
            self.calc.power(2, "3")

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(9), 3.0)

    def test_square_root_error_negative(self):
        with self.assertRaises(TypeError):
            self.calc.square_root(-9)

    def test_square_root_error_type(self):
        with self.assertRaises(TypeError):
            self.calc.square_root("9")

    def test_log10(self):
        self.assertEqual(self.calc.log10(100), 2.0)

    def test_log10_error_zero(self):
        with self.assertRaises(TypeError):
            self.calc.log10(0)

    def test_log10_error_negative(self):
        with self.assertRaises(TypeError):
            self.calc.log10(-1)

    def test_log10_error_type(self):
        with self.assertRaises(TypeError):
            self.calc.log10("100")