# класс конвертер
class Converter:
    @staticmethod
    def meters_to_feet(meters):
        feet = meters * 3.28084
        feet = round(feet, 2)
        return feet

    @staticmethod
    def kmeters_to_miles(kmeters):
        miles = kmeters * 0.621371
        miles = round(miles, 2)
        return miles

    @staticmethod
    def celcius_to_fahrenheit(celcius):
        f = celcius * 1.80000 + 32.00
        f = round(f, 2)
        return f

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

    @staticmethod
    def feet_to_meters(feet):
        meters = feet / 3.28084
        meters = round(meters, 2)
        return meters

    @staticmethod
    def miles_to_kmeters(miles):
        kmeters = miles * 1.60934
        kmeters = round(kmeters, 2)
        return kmeters

    @staticmethod
    def arshins_to_meters(arshins):
        meters = arshins * 0.7112
        meters = round(meters, 2)
        return meters

    @staticmethod
    def sajens_to_meters(sajens):
        meters = sajens / 2.13
        meters = round(meters, 2)
        return meters

    @staticmethod
    def feet_to_arshins(feet):
        arshins = feet * 2.33
        arshins = round(arshins, 2)
        return arshins

    @staticmethod
    def arshins_to_feet(arshins):
        feet = arshins * 0.428
        feet = round(feet, 2)
        return feet