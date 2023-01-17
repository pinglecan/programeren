def addition(number1: float, number2: float):
    print(f"{number1} + {number2} = {float(number1) + float(number2)}")
    return number1 + number2


def subtraction(number1: float, number2: float):
    print(f"{number1} - {number2} = {float(number1) - float(number2)}")
    return number1 -number2



def multiplication(number1: float, number2: float):
    print(f"{number1} * {number2} = {float(number1) * float(number2)}")
    return number1 * number2


def division(number1: float, number2: float):
    print(f"{number1} / {number2} = {float(number1) / float(number2)}")
    return number1 / number2

user_num = 0
another_round = True

while another_round:
    choice = input("""wat te doen?
    #     A) getallen optellen
    #     B) getallen aftrekken
    #     C) getallen vermenigvuldigen
    #     D) getallen delen
    #     E) getal ophogen
    #     F) getal verlagen
    #     G) getal verdubbelen
    #     H) getal halveren
    #     Kies: """).upper()

    if user_num:
        num1 = float(input("Welk getal: "))
        num2 = user_num
    elif choice == "A" or choice == "B" or choice == "C" or choice == "D":
        num1 = float(input("Getal 1: "))
        num2 = float(input("Getal 2: "))
    else:
        num1 = float(input("Welk getal: "))

    if choice == "A":
        user_num += float(addition(num1, num2))
    elif choice == "B":
        user_num += subtraction(num1, num2)
    elif choice == "C":
        user_num += multiplication(num1, num2)
    elif choice == "D":
        user_num += division(num1, num2)
    elif choice == "E":
        user_num += addition(num1, 1)
    elif choice == "F":
        user_num += subtraction(num1, 1)
    elif choice == "G":
        user_num += multiplication(num1, 2)
    elif choice == "H":
        user_num += division(num1, 2)

    another_round = input(f"Do you want to do something with {user_num}? (Y/N): ").upper()
    if another_round == "N":
        another_round = False
    elif another_round == "Y":
        another_round = True
    else:
        print("Invalid answer")