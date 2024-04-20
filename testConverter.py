# файл для тестирования класса конвертер

import unittest


class TestConverterClass(unittest.TestCase):

    def test_converter_class_exists(self):
        self.assertTrue(hasattr(Converter, 'meters_to_feet'))
        self.assertTrue(hasattr(Converter, 'kilograms_to_pounds'))

if __name__ == '__main__':
    unittest.main()