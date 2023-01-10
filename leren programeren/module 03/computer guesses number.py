import random
done = False
low = 1
high = 1000
while done == False:
    computer_number = random.randint(low,high)
    print(f'is het {computer_number}? voer in h/l/g')
    H_l = input()

    if H_l == 'h':
        low = computer_number
    elif H_l == 'l':
        high = computer_number
    else:
        print(F'yipee het was:{computer_number}!')
        done = True