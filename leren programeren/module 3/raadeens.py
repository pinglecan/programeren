from random import randint
import os 
from turtle import clear
from time import sleep
game = 0
punt = 0
stop = False
while game != 20 and stop == False:
    computer_numer = randint(1,1000)
    rounds = 0  
    while rounds <= 10:
        player_number = int(input('type een nummer tussen 1 en 1000  '))
        if player_number < computer_numer:
            print('>')
        elif player_number > computer_numer:
            print('<')
        elif player_number == computer_numer:
            print('correct +1 point')
            sleep(3)
            punt += 1
        if rounds == 10:
            print('you lost')
        rounds += 1
        verschil = computer_numer - player_number
        if verschil < 0 :
            verschil *= -1
        if verschil <= 20:
            print('je bent erg warm')
        elif verschil <= 50:
            print('je bent warm')
    os.system('cls')
    game+=1
    if game < 20:
        nog_een_keer = input('wil je nog een keer?  ').lower()
        if nog_een_keer == 'nee':
                print(f'{punt} aantal punten')
                stop = True
        else :
            print(f'{punt} aantal punten')
            print('volgende ronde')         
    else:
        print('bedankt')