# файл для тестирования класса конвертер

import unittest
from Converter import Converter

class TestConverterClass(unittest.TestCase):

    def test_converter_class_exists(self):
        self.assertTrue(hasattr(Converter, 'meters_to_feet'))
        self.assertTrue(hasattr(Converter, 'kilograms_to_pounds'))

    def test_meters_to_feet(self):
        self.assertAlmostEqual(Converter.meters_to_feet(1), 3.28)
        self.assertAlmostEqual(Converter.meters_to_feet(5), 16.40)
        self.assertAlmostEqual(Converter.meters_to_feet(0), 0)

    def test_kmeters_to_miles(self):
        self.assertAlmostEqual(Converter.kmeters_to_miles(1), 1.61)
        self.assertAlmostEqual(Converter.kmeters_to_miles(10), 16.09)
        self.assertAlmostEqual(Converter.kmeters_to_miles(0), 0)

    def test_kilograms_to_pounds(self):
        self.assertAlmostEqual(Converter.kilograms_to_pounds(1), 2.20)
        self.assertAlmostEqual(Converter.kilograms_to_pounds(10), 22.05)
        self.assertAlmostEqual(Converter.kilograms_to_pounds(0), 0)

    def test_celsius_to_reaumur(self):
        self.assertAlmostEqual(Converter.celsius_to_reaumur(1), 0.8)
        self.assertAlmostEqual(Converter.celsius_to_reaumur(10), 8.0)
        self.assertAlmostEqual(Converter.celsius_to_reaumur(0), 0)

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(Converter.celcius_to_fahrenheit(10), 50)
        self.assertAlmostEqual(Converter.celcius_to_fahrenheit(38), 100.40)
        self.assertAlmostEqual(Converter.celcius_to_fahrenheit(0), 32.00)

    def test_meters_to_arshins(self):
        self.assertAlmostEqual(Converter.meters_to_arshins(1), 1.41)
        self.assertAlmostEqual(Converter.meters_to_arshins(10), 14.06)
        self.assertAlmostEqual(Converter.meters_to_arshins(0), 0)
    def test_meters_to_sajens(self):
        self.assertAlmostEqual(Converter.meters_to_sajens(1), 2.13)
        self.assertAlmostEqual(Converter.meters_to_sajens(10), 21.3)
        self.assertAlmostEqual(Converter.meters_to_sajens(0), 0)
if __name__ == '__main__':
    unittest.main()