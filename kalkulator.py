import logging
logging.basicConfig(level=logging.DEBUG)
def calc():
    choice = input("Wybierz działanie:\nDodawanie - wpisz 1,\nOdejmowanie - wpisz 2,\nMnożenie - wpisz 3,\nDzielenie - wpisz 4\n")
    if int(choice) == 1:
        a = input("Wpisz pierwszy składnik: ")
        b = input("Wpisz drugi składnik: ")
        return print(f"Wynik dodawania",float(a),"+",float(b),"=",float(a)+float(b))
    if int(choice) == 2:
        a = input("Wpisz odjemną: ")
        b = input("Wpisz odjemnik: ")
        return print("Wynik odejmowania",float(a),"-",float(b),"=",float(a)-float(b))
    if int(choice) == 3:
        a = input("Wpisz pierwszy czynnik: ")
        b = input("Wpisz drugi czynnik: ")
        return print("Wynik mnożenia",float(a),"\u2022",float(b),"=",float(a)*float(b))
    if int(choice) == 4:
        a = input("Wpisz dzielną: ")
        b = input("Wpisz dzielnik: ")
        return print("Wynik dzielenia",float(a),":",float(b),"=",float(a)/float(b))
    else:
        print("Wybrałeś nieistniejące działanie")
        exit(1)

calc()