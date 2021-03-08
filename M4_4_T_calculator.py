"""Simple powerful calculator."""

import sys
import logging
calc_logger = logging.getLogger(__name__)
calc_logger.setLevel(logging.DEBUG)

output_handler = logging.FileHandler("calculator_logs.log")

calc_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
output_handler.setFormatter(calc_format)

calc_logger.addHandler(output_handler)


add = []
subtract = []
multiply = []
divide = []


def add_numbers():
    """Can add as many numbers as you wish."""
    get_add_numbers()
    return f'Wynik dodawania: {sum(add)}'


def subtract_numbers():
    """Can subtract from minuend as many subtrahends as you wish."""
    get_subtract_numbers()
    x = subtract[0]
    for i in range(len(subtract)-1):
        x = x - subtract[i+1]
    return f'Wynik odejmowania: {x}'

def multiply_numbers():
    """Can multiply as many numbers as you wish."""
    get_multiply_numbers()
    x = multiply[0]
    for i in range(len(multiply)-1):
        x = x * multiply[i+1]
    return f'Wynik mnożenia: {x}'


def divide_numbers():
    """Can divide dividend by as many dividers as you wish."""
    get_divide_numbers()
    x = divide[0]
    for i in range(len(divide)-1):
        x = x / divide[i+1]
    return f'Wynik dzielenia: {x}'

if __name__ == "__main__":
    def get_add_numbers():
        """Get as many numbers as you wish to add to each other."""
        text = ["pierwszy", "następny"]
        while True:
            try:
                a = float(input(f"Podaj {text[0]} składnik: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                add.append(float(a))
                calc_logger.info(f'{text[0].capitalize()} składnik: = {a} .')
                break
        while True:
            try:
                b = float(input(f"Podaj {text[1]} składnik: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                add.append(float(b))
                calc_logger.info(f'{text[1].capitalize()} składnik: = {b} .')
                break
        while True:
            if input(f"UWAGA: Czy chcesz zakończyć dodawanie? t/n: ") == 't':
                break
            else:
                try:
                    c = float(input(f"Podaj {text[1]} składnik: "))
                except ValueError:
                    calc_logger.error("To nie jest liczba!")
                    print("To nie jest liczba!")
                else:
                    add.append(float(c))
                    calc_logger.info(f'{text[1].capitalize()} składnik: = {c} .')
        return f'Wynik dodawania: {sum(add)}'


    def get_subtract_numbers():
        """Get as many subtrahends as you wish to subtract from minuend."""    
        text = ["odjemną", "odjemnik"]
        while True:
            try:
                a = float(input(f"Podaj {text[0]}: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                subtract.append(float(a))
                calc_logger.info(f'{text[0].capitalize()} jest: = {a} .')
                break
        while True:
            try:
                b = float(input(f"Podaj {text[1]}: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                subtract.append(float(b))
                calc_logger.info(f'{text[1].capitalize()} to: = {b} .')
                break
        while True:
            if input(f"UWAGA: Czy chcesz zakończyć odejmowanie? t/n: ") == 't':
                break
            else:
                try:
                    c = float(input(f"Podaj {text[1]}: "))
                except ValueError:
                    calc_logger.error("To nie jest liczba!")
                    print("To nie jest liczba!")
                else:
                    subtract.append(float(c))
                    calc_logger.info(f'Następny {text[1]} to: = {c} .')
        return subtract


    def get_multiply_numbers():
        """Get as many numbers as you wish to multiply."""
        text = ["pierwszy", "następny"]
        while True:
            try:
                a = float(input(f"Podaj {text[0]} czynnik: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                multiply.append(float(a))
                calc_logger.info(f'{text[0].capitalize()} czynnik: = {a} .')
                break
        while True:
            try:
                b = float(input(f"Podaj {text[1]} czynnik: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                multiply.append(float(b))
                calc_logger.info(f'{text[1].capitalize()} czynnik: = {b} .')
                break
        while True:
            if input(f"UWAGA: Czy chcesz zakończyć mnożenie? t/n: ") == 't':
                break
            else:
                try:
                    c = float(input(f"Podaj {text[1]} czynnik: "))
                except ValueError:
                    calc_logger.error("To nie jest liczba!")
                    print("To nie jest liczba!")
                else:
                    multiply.append(float(c))
                    calc_logger.info(f'{text[1].capitalize()} czynnik: = {c} .')
        return multiply


    def get_divide_numbers():
        """Get as many dividers as you wish to divide dividend by them."""
        text = ["dzielną", "dzielnik"]
        while True:
            try:
                a = float(input(f"Podaj {text[0]}: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                divide.append(float(a))
                calc_logger.info(f'{text[0].capitalize()} jest: = {a} .')
                break
        while True:
            try:
                b = float(input(f"Podaj {text[1]}: "))
            except ValueError:
                calc_logger.error("To nie jest liczba!")
                print("To nie jest liczba!")
            else:
                divide.append(float(b))
                calc_logger.info(f'{text[1].capitalize()} to: = {b} .')
                break
        while True:
            if input(f"UWAGA: Czy chcesz zakończyć dzielenie? t/n: ") == 't':
                break
            else:
                try:
                    c = float(input(f"Podaj {text[1]}: "))
                except ValueError:
                    calc_logger.error("To nie jest liczba!")
                    print("To nie jest liczba!")
                else:
                    divide.append(float(c))
                    calc_logger.info(f'{text[1].capitalize()} to: = {c} .')
        return divide
    

    def calculator():
        """."""
        actions = {1: add_numbers,
                2: subtract_numbers,
                3: multiply_numbers,
                4: divide_numbers
        }
        while True:
            operator = int(input("Wybierz działanie:\nDodawanie - 1,\nOdejmowanie - 2,\nMnożenie - 3,\nDzielenie - 4\nPodaj swój wybór (nr): "))
            try:
                operation = actions[operator]
            except KeyError:
                calc_logger.error(f"To nie jest liczba z przedziału od 1 do {list(actions.keys())[-1]}")
                print(f"To nie jest liczba z przedziału od 1 do {list(actions.keys())[-1]}")
            else:
                calc_logger.info(operation())
                break
        choice = input('Czy chcesz wykonać inne działanie? t/n: ')
        if choice == 't':
            calculator()
        else:
            exit(1)
        return

    calculator()
