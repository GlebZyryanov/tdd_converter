# класс конвертер
class Converter:
    @staticmethod
    def meters_to_feet(meters):
        feet = meters * 3.28084
        return feet

    @staticmethod
    def kilograms_to_pounds(kilograms):
        pounds = kilograms * 2.20462
        return pounds

    @staticmethod
    def celsius_to_reaumur(celsius):
        reaumur = celsius * 0.8
        return reaumur
