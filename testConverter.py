# файл для тестирования класса конвертер
import unittest


class TestConverterClass(unittest.TestCase):
    def test_converter_class_exists(self):
        self.assertTrue(hasattr(Converter, '__init__'), "Converter class should have '__init__' method")
        self.assertTrue(hasattr(Converter, 'convert'), "Converter class should have 'convert' method")

if __name__ == '__main__':
    unittest.main()