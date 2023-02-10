from  random import randint
from time import sleep
from turtle import clear
from os import system



def talus_fight():
    turn = 0
    weapon_stick = 10
    player_health = 500
    enemy_health = 300
    weapon_bombs = 30
    stap = 'play'

    while stap == 'play':
        battle_ui =  print(f'''
        |
        |   Link  vs  stone talus
        |
        |
        |   {player_health} hp   {enemy_health} hp
        |
        |   A( {weapon_stick} dmg
        |''')

        player_dmg = input('        |   kies een aanval:  ').upper()
        turn+=1
        if player_dmg == 'A':
            enemy_health -= weapon_stick 
        elif player_dmg == 'B' and turn >= 3:
            enemy_health -= weapon_bombs
        else:
            print('you didnt do shit')
        enemy_hit = randint(10,30)
        instakill = randint(1,50)
        if instakill == 20:
            enemy_hit *= 100
        print(f'the stone talus hits for {enemy_hit} dmg')
        player_health -= enemy_hit        
        sleep(0.7)
        system('cls')
        



talus_fight()