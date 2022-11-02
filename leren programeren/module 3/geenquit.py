import os
from turtle import clear
os.system('cls')
vraagteken = 1
aantal_keer = 0
while vraagteken != 'quit':
    vraagteken = input('?  ')
    aantal_keer += 1
    print(aantal_keer)