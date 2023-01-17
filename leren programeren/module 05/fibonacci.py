def fibonacci(x):
    lijst = [0,1]
    for fib in range(x):
        lijst.append(lijst[-1] + lijst[-2])
    return lijst

user_input = int(input('hoeveel numers in de fibonachi reeks wil je?  '))

print(fibonacci(user_input))