from random import randint
import os 
from turtle import clear
from time import sleep

punt = 0
for i in range (20):
    computer_numer = randint(1,1000)
    rounds = 0  
    while rounds <= 10:
        player_number = int(input('type een nummer tussen 1 en 1000 of type quit om te stoppen  '))
        if player_number < computer_numer:
            print('>')
        elif player_number > computer_numer:
            print('<')
        elif player_number == computer_numer:
            print('correct +1 point')
            sleep(3)
            punt += 1
            break
        rounds += 1
        verschil = computer_numer - player_number
        if verschil < 0 :
            verschil *= -1
        if verschil <= 20:
            print('je bent erg warm')
        elif verschil <= 50:
            print('je bent warm')
        if rounds == 10:
            print('you lost')
    os.system('cls')
    nog_een_keer = input('wil je nog een keer?  ').lower()
    if nog_een_keer == 'nee':
            print(f'{punt} aantal punten')
            exit()
    print(f'{punt} aantal punten')
    print('volgende ronde')         
    