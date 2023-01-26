def plus(number1: float, number2: float):
    return number1 + number2


def min(number1: float, number2: float):
    return number1 -number2



def keer(number1: float, number2: float):
    return number1 * number2


def delen(number1: float, number2: float):
    return number1 / number2

user_input = 0
another_round = True

while another_round:
    choice = input("""wat te doen?
    |     A) getallen optellen
    |     B) getallen aftrekken
    |     C) getallen vermenigvuldigen
    |     D) getallen delen
    |     E) getal ophogen
    |     F) getal verlagen
    |     G) getal verdubbelen
    |     H) getal halveren
    |     Kies: """).upper()

    if user_input:
        num1 = float(input("Welk getal: "))
        num2 = user_input
    elif choice == "A" or choice == "B" or choice == "C" or choice == "D":
        num1 = float(input("Getal 1: "))
        num2 = float(input("Getal 2: "))
    else:
        num1 = float(input("Welk getal: "))

    if choice == "A":
        user_input += float(plus(num1, num2))
    elif choice == "B":
        user_input += min(num1, num2)
    elif choice == "C":
        user_input += keer(num1, num2)
    elif choice == "D":
        user_input += delen(num1, num2)
    elif choice == "E":
        user_input += plus(num1, 1)
    elif choice == "F":
        user_input += min(num1, 1)
    elif choice == "G":
        user_input += keer(num1, 2)
    elif choice == "H":
        user_input += delen(num1, 2)

    another_round = input(f"Do you want to do something with {user_input}? (Y/N): ").upper()
    if another_round == "N":
        another_round = False
    elif another_round == "Y":
        another_round = True
    else:
        print("Invalid answer")