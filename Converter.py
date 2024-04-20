# класс конвертер
class Converter:
    @staticmethod
    def meters_to_feet(meters):
        feet = meters * 3.28084
        feet = round(feet, 2)
        return feet

    @staticmethod
    def kmeters_to_miles(kmeters):
        feet = kmeters * 1.60934
        feet = round(feet, 2)
        return feet

    @staticmethod
    def kilograms_to_pounds(kilograms):
        pounds = kilograms * 2.20462
        pounds = round(pounds, 2)
        return pounds

    @staticmethod
    def celsius_to_reaumur(celsius):
        reaumur = celsius * 0.8
        reaumur = round(reaumur, 2)
        return reaumur

    @staticmethod
    def meters_to_arshins(meters):
        arshins = meters / 0.7112  # 1 arshin = 0.7112 meters
        arshins = round(arshins, 2)
        return arshins

    @staticmethod
    def meters_to_sajens(meters):
        sajens = meters * 2.13  # 1 sajen = 2.13 meters
        sajens = round(sajens, 2)
        return sajens

