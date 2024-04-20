from Converter import Converter

def print_help():
    print("Доступные команды:")
    print(" - длина: Конвертировать между различными единицами длины\n    - m - метры\n    - km - километры\n   - ft - футы\n    - sj - сажени\n    - ah - аршины\n    - mi - мили")
    print(" - масса: Конвертировать между различными единицами массы\n    - kg - kilogram\n - lb - pound")
    print(" - температура: Конвертировать между различными единицами температуры\n    - C - Celsius\n    - F Fahrenheit\n - R - Reaumur - reaumur")
    print(" - выход: покинуть программу")
while True:
    command = input("Ввести команду ('length', 'weight', 'temperature', 'help', or 'quit'): ")

    if command == 'quit':
        print("Выход...")
        break

    if command == 'help':
        print_help()
        continue

    if command == 'length':
        value = float(input("Введите значение: "))
        from_unit = input("Исходная система счисления: ")
        to_unit = input("Конечная система счисления: ")

        if from_unit == to_unit:
            print("Исходная и конечная система счисления совпадают. Невозможно конвертировать.")
            continue
        elif from_unit == 'm' and to_unit == 'ah':
            result = Converter.meters_to_arshins(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'm' and to_unit == 'ft':
            result = Converter.meters_to_feet(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'm' and to_unit == 'sj':
            result = Converter.meters_to_sajens(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'km' and to_unit == 'mi':
            result = Converter.kmeters_to_miles(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'mi' and to_unit == 'km':
            result = Converter.miles_to_kmeters(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'ft' and to_unit == 'm':
            result = Converter.feet_to_meters(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'sj' and to_unit == 'm':
            result = Converter.sajens_to_meters(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'ah' and to_unit == 'm':
            result = Converter.arshins_to_meters(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'sj' and to_unit == 'mi':
            result = Converter.sajens_to_miles(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'mi' and to_unit == 'sj':
            result = Converter.miles_to_sajens(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'ft' and to_unit == 'ah':
            result = Converter.feet_to_arshins(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'ah' and to_unit == 'ft':
            result = Converter.arshins_to_feet(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        else:
            print("Что то вы неправильно ввели, попробуйте снова.")

    elif command == 'weight':
        value = float(input("Введите значение: "))
        from_unit = input("Исходная система счисления: ")
        to_unit = input("Конечная система счисления: ")

        if from_unit == to_unit:
            print("Исходная и конечная система счисления совпадают. Невозможно конвертировать.")
            continue
        elif from_unit == 'kg' and to_unit == 'lb':
            result = Converter.kilograms_to_pounds(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'lb' and to_unit == 'kg':
            result = Converter.pounds_to_kilograms(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        else:
            print("Что то вы неправильно ввели, попробуйте снова.")
    elif command == 'temperature':
        value = float(input("Введите значение: "))
        from_unit = input("Исходная система счисления: ")
        to_unit = input("Конечная система счисления: ")

        if from_unit == to_unit:
            print("Исходная и конечная система счисления совпадают. Невозможно конвертировать.")
            continue

        if from_unit == to_unit:
            print("Source and target units are the same. No conversion needed.")
            continue
        elif from_unit == 'C' and to_unit == 'F':
            result = Converter.celsius_to_fahrenheit(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        elif from_unit == 'C' and to_unit == 'R':
            result = Converter.celsius_to_reaumur(value)
            print(f"{value} {from_unit} ==> {result} {to_unit}")
        else:
            print("Что то вы неправильно ввели, попробуйте снова.")
    else:
        print("Вы неправильно ввели команду. Попробуйте снова.")

if __name__ == '__main__':
    print_help()


