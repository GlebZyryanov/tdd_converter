# файл для тестирования класса конвертер

import unittest
from Converter import Converter

class TestConverterClass(unittest.TestCase):

    def test_converter_class_exists(self):
        self.assertTrue(hasattr(Converter, 'meters_to_feet'))
        self.assertTrue(hasattr(Converter, 'kilograms_to_pounds'))

    def test_meters_to_feet(self):
        self.assertAlmostEqual(Converter.meters_to_feet(1), 3.28084)
        self.assertAlmostEqual(Converter.meters_to_feet(5), 16.4042)
        self.assertAlmostEqual(Converter.meters_to_feet(0), 0)

    def test_kilograms_to_pounds(self):
        self.assertAlmostEqual(Converter.kilograms_to_pounds(1), 2.20462)
        self.assertAlmostEqual(Converter.kilograms_to_pounds(10), 22.0462)
        self.assertAlmostEqual(Converter.kilograms_to_pounds(0), 0)

if __name__ == '__main__':
    unittest.main()