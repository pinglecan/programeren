import random
import os
import time
from turtle import clear

#shit is false



weapon_axe = 0
armor_programming_socks = False
weapon_black_sword = 0
weapon_2swords = 0
weapon_shield = True
armor_royal_guards_armor = False
item_food = False
weapon_sword = 0
weapon_flamesword = 0
repeat_game = True

# function to print with delay
def printDelay(t: str, d=2):
    time.sleep(d)
    print(t)


#os clear
def clear_console():
    os.system('cls')


#the game begining

while repeat_game == True:
    clear_console()
    print('You wake up in a ancient temple you don’t rember anything you walk out into a bright light')
    man_or_forest = input('You hear a voice of a woman telling you you have been sleep for the past 100 years you see a old man in the distence do you go towards him Y/N?  ').lower()
    if man_or_forest == 'yes' or man_or_forest == 'y':
        printDelay('you decide to go to the old man and talk to him you pick up a stick along the way becouse who doesn’t like sticks?')
        printDelay('"hello young one welcome to the great platue a giant fortified piece of land"')
        printDelay('you talk to him for a bit then you walk towards a old building ')
        axe = input('You see a axe in the discence do you pick it up y/n  ').lower()
        if axe == 'yes' or axe == 'y' :
            weapon_axe = 1
        else:
            printDelay('you did not pick up the axe')
        printDelay('You see a button and you press it a big tower emerges from under the building')
        printDelay('You climb down the tower and you see the old man again he tells you to go the shrine towards the east')
        printDelay('You go to the shrine and a old mashine comes to life when it notices you it has a red lazer pointed at you')
        #puzzel and guardian
        run_or_fight_guardian = input('do you run away into the shrine or do you fight it?  ').lower()
        if run_or_fight_guardian == 'run away' or run_or_fight_guardian == 'run':
            printDelay('You run into the shrine and escape from the things lazer there is a puzzel you must do you look around and see 4 stones on the floor')
            printDelay('a camel, elephant, lizard and a bird')
            printDelay('In the center of the room is a map with 4 places to put the stones')
            puzel_camel = input('In the dusty desert you put the …').lower()
            puzel_lizard = input('In the hot volcano you put the...').lower()
            puzel_bird = input('In the cold mountain...').lower()
            puzel_elephant = input('In the raining swamp you put the...').lower()
            if puzel_bird == 'bird' and puzel_camel == 'camel' and puzel_elephant == 'elephant' and puzel_lizard == 'lizard':
                printDelay('the door infront of you opens')
                printDelay('you find yourself in a treasure room with a orb in the middel ')
                printDelay('you take the orb with you')
                printDelay('you walk out of the temple and see the old man again')
                printDelay('Good job young one now go to the temple of time i shall meet you there again and then he disapears')
                printDelay('you make your way to the temple of time to find the old man')
                printDelay('you find a big stone statue with a hole in could fit the glowing ball')
                #chest part
                ball_in_statue = input('do you put it in Y/N?  ').lower()
                if ball_in_statue == 'y' or ball_in_statue == 'yes':
                    printDelay('you put the orb into the statue it opens a trap door behind you')
                    open_chest =input('there is a chest under the trap door do you open it? Y/N  ').lower()
                    if open_chest == 'yes' or 'y':
                        printDelay('you got some programming socks')
                        armor_programming_socks = True
                    elif open_chest == 'no' or open_chest == 'n':
                        printDelay('you did not open the chest')
                elif ball_in_statue == 'no' or ball_in_statue == 'n':
                    printDelay('you did not use the orb')
                printDelay('The old man tells you to come up the later to the roof')
                printDelay('"well young one i think its time for me to tell you who i really am"')
                printDelay('"i was king rhoam bosphoramus hyrule i was the last king of hyrule ')
                printDelay('"you need to kill ganon to save hyrule"')
                printDelay('you head towards the castle ')
                printDelay('you see two posible ways to enter')
                printDelay('you can enter trough the front gate or you could enter via the water')
                #the castle
                how_enter_castle = input('how will you enter?  ').lower()
                if how_enter_castle == 'water' or how_enter_castle == 'via the water' or  how_enter_castle == 'via water' :
                    printDelay('You enter via the water you end up in the secret docking area of the castle you find a black sword')
                    weapon_black_sword = 3
                    printDelay('you sneak your way through the palace')
                    printDelay('you see some guards in the armory you could fight them to get some armor')
                    armory_or_boss = input('do you fight them or do you keep walking?  ').lower()
                    if armory_or_boss == 'fight' or armory_or_boss =='fight them':
                        sneak_or_head_water = input('do you sneak attack or do you fight them head on?  ').lower()
                        if sneak_or_head_water =='sneak' or sneak_or_head_water =='sneak attack':
                            printDelay('you sneak attack the guards and they die ')
                            printDelay('you loot the armory you got 2 swords a shield and some royal guards armor nice')
                            weapon_2swords = 4
                            weapon_shield = True
                            armor_royal_guards_armor = True
                        elif sneak_or_head_water == 'head on' or sneak_or_head_water =='attack head on' or sneak_or_head_water=='fight head on':
                            printDelay('you decide to fight the guard head on')
                            printDelay('sadly enough the guards are way stronger then you so you die')
                            printDelay('ending 6 died to the guards in the armory')
                            points = weapon_2swords + weapon_axe + weapon_black_sword + weapon_flamesword + weapon_sword 
                            printDelay(f'you got {points} points!')
                            play_again = input('do you wanna play again Y/N  ').lower()
                            if input == 'y':
                                continue
                            else:
                                exit()
                        else:
                            printDelay('i gave you the options how did you mess that up')
                            printDelay('ending 9 you put in a un usable comand')
                            play_again = input('do you wanna play again Y/N  ').lower()
                            if input == 'y':
                                continue
                            else:
                                exit()
                        printDelay('then you walk to the boss room')
                        printDelay('you enter the boss room')
                elif how_enter_castle == 'gate' or how_enter_castle == 'front gate' or how_enter_castle == 'via the front gate':
                    printDelay('You quickly run towards the first entrance  into the castle you see you are in the dining room and find some food so you can heal')
                    item_food = True
                    kitchen_sword = input('You also see a sword do take it with you? Y/N  ').lower()
                    if kitchen_sword== 'y' or kitchen_sword =='yes' :
                        weapon_sword = 2
                    else :
                        printDelay('you did not take the sword with you')
                    printDelay('you walk further and see the boss room')
                    printDelay('but to the felt of you you see a strong looking sword but there is a guard')
                    weapon_or_boss=input('do you go for the weapon or do you go to the boss room?  ').lower()
                    if weapon_or_boss == 'boss room' or weapon_or_boss == 'go to boss room':
                        printDelay('you walk to the boss room')
                    elif weapon_or_boss == 'weapon' or weapon_or_boss =='go to weapon':
                        sneak_or_head_gate =input('do you fight him head on or do you sneak attack him?  ').lower()
                        if sneak_or_head_gate == 'fight him head on' or sneak_or_head_gate == 'fight head on' or sneak_or_head_gate == 'head on':
                            printDelay('you decide to fight him head on')
                            printDelay('but he is a lot stronger then you')
                            printDelay('ending 5 you died to a guard')
                            play_again = input('do you wanna play again Y/N  ').lower()
                            if input == 'y':
                                continue
                            else:
                                exit()
                        elif sneak_or_head_gate == 'sneak' or sneak_or_head_gate == 'sneak attack' or sneak_or_head_gate == 'sneak attack him':
                            printDelay('you sneak attack the guard and he dies')
                            printDelay('you pick up the flaming sword')
                            weapon_flamesword = 4
                            printDelay(' now you walk to the boss room')
                        else:
                            printDelay('i gave you the options how did you mess that up')
                            printDelay('ending 9 you put in a un usable comand')
                            play_again = input('do you wanna play again Y/N  ').lower()
                            if input == 'y':
                                continue
                            else:
                                exit()
                else:
                        printDelay('i gave you the options how did you mess that up')
                        printDelay('ending 9 you put in a un usable comand')
                        play_again = input('do you wanna play again Y/N  ').lower()
                        if input == 'y':
                            continue
                        else:
                            exit()
            else:
                printDelay('a trapdoor opens under you and you all to your death')
                printDelay('ending 4 you failed the puzel')
                play_again = input('do you wanna play again Y/N  ').lower()
                if input == 'y':
                    continue
                else:
                    exit()
        elif run_or_fight_guardian == 'fight' or run_or_fight_guardian == 'fight it':
            printDelay('you grab your weapon and run towards it to fight it sadly enough it shoots a lazer killing you before you can even reach it')
            printDelay('ending 3 you died to the guardian lmao')
            play_again = input('do you wanna play again Y/N  ').lower()
            if input == 'y':
                continue
            else:
                exit()
        else:    
            printDelay('i gave you the options how did you mess that up')
            printDelay('ending 9 you put in a un usable comand')
            play_again = input('do you wanna play again Y/N  ').lower()
            if input == 'y':
                continue
            else:
                exit()
    elif man_or_forest == 'n' or man_or_forest == 'no':
        printDelay('you decide to not go to the old man and you go into the forest')
        printDelay('after wandering in the forest for a while you find yourself near a kamp of bokoblins')
        talus_or_boko =input('they spot you and ready there weapons do you fight or flee?  ').lower()
        if talus_or_boko == 'fight' or talus_or_boko == 'fight them':
            printDelay('you ready yourself for a fight sadly enough one of them has a bow and shoots you in the heart')
            printDelay('you fall to the ground and die')
            printDelay('ending 1 boko death')
            play_again = input('do you wanna play again Y/N  ').lower()
            if input == 'y':
                continue
            else:
                exit()
        elif talus_or_boko == 'flee' or talus_or_boko == 'run away':
            printDelay('you run away deeper into the forest')
            printDelay('you eventualy end up in a stony area and sit down on a stone')
            printDelay('but the stone under you starts moving')
            printDelay('it turns out you sat down on a stone stone talus and its not happy')
            printDelay('it smashes you with its giant stone hands and you die')
            printDelay('ending 2 stone talus')
            play_again = input('do you wanna play again Y/N  ').lower()
            if input == 'y':
                continue
            else:
                exit()
        else:
            printDelay('i gave you the options how did you mess that up')
            printDelay('ending 9 you put in a un usable comand')
            play_again = input('do you wanna play again Y/N  ').lower()
            if input == 'y':
                continue
            else:
                exit()
    else:
        printDelay('i gave you the options how did you mess that up')
        printDelay('ending 9 you put in a un usable comand')
        play_again = input('do you wanna play again Y/N  ').lower()
        if input == 'y':
            continue
        else:
            exit()
    #the bossssssssss scarry
    #####################################################
    clear_console()
    print('______________________________________________________________________________________________________________________________________')
    printDelay('you ready your weapon for a fight ganon apears infront of you a giant creepy mess made of pure evil')
    printDelay('lets see of you can beat him')

    if weapon_2swords == 0 and weapon_axe == 0 and weapon_black_sword == 0 and weapon_flamesword == 0 and weapon_sword == 0:
        printDelay('... all you have is a stick a damm stick?')
        printDelay('no way you can beat ganon but you can try')
        hit1 = random.randint(0,101)
        try:
            player_hit1 =int(input('type a number between 1 and 100  '))
        except:
            print('dat is geen numer voer een numer in')
            print('het numer is nu 69')
            player_hit1 = 69
        if hit1 != player_hit1:
            printDelay('you missed and died because you only had a stick')
            printDelay('ending 7 died to the boss')
            play_again = input('do you wanna play again Y/N  ').lower()
            if input == 'y':
                continue
            else:
                exit()

        elif hit1 == player_hit1:
            printDelay('you beat the living shit out of ganon using only a fucking stick')
            printDelay('he was begging you to stop but you didnt you defeated ganon using only a stick congrats')
            printDelay('secret ending stick kill')
            play_again = input('do you wanna play again Y/N  ').lower()
            if input == 'y':
                continue
            else:
                exit()
    else :
        hit_chance = 13 - weapon_2swords - weapon_axe - weapon_black_sword - weapon_flamesword -weapon_sword
        stap = 1
        while stap != 0:
            if stap == 1:
                hit1 = random.randint(1,hit_chance)
                try:
                    player_hit1 = int(input(f'type a number between 1 and {hit_chance}  '))
                except:
                    printDelay('dat is geen nummer')
                    printDelay('het numer is nu 2')
                    player_hit1 = 1
                if hit1 == player_hit1 :
                    printDelay('Hit! he took a lot of damage')
                    stap = 3
                elif hit1 != player_hit1 and weapon_shield == True or item_food == True:
                    stap = 2
                elif hit1 != player_hit1 and weapon_shield == False and item_food == False:
                    stap = 6
            elif stap == 2:
                printDelay('you missed')
                printDelay('But you had some thing to stop yourself from dying')
                stap = 3
            elif stap == 3:
                hit2 = random.randint(1,hit_chance)
                try:
                    player_hit2 = int(input(f'type a number between 1 and {hit_chance}  '))
                except:
                    printDelay('dat is geen nummer')
                    printDelay('het numer is nu 2')
                    player_hit2 = 2
                if hit2 == player_hit2:
                    printDelay('HIT! he took a lot of damage')
                    stap = 5
                elif hit2 != player_hit2 and (armor_programming_socks == True or armor_royal_guards_armor == True):
                    stap = 4
                elif hit2 != player_hit2 and armor_programming_socks == False and armor_royal_guards_armor == False:
                    stap = 6
            elif stap == 4:
                    printDelay('you got hit')
                    printDelay('luckly your armor took the blow')
                    stap = 5
            elif stap == 5:
                hit3 = random.randint(1,hit_chance)
                try:
                    player_hit3 = int(input(f'type a number between 1 and {hit_chance}  '))
                except:
                    printDelay('dat is geen nummer')
                    printDelay('het numer is nu 2')
                    player_hit3 = 2
                if hit3 == player_hit3:
                    stap = 7
                elif hit3 != player_hit3:
                    stap = 6
            elif stap == 6:
                    printDelay('ganon attacks you and you die')
                    printDelay('ending 7 you died to ganon')
                    play_again = input('do you wanna play again Y/N  ').lower()
                    if input == 'y':
                        continue
                    else:
                        exit()
            elif stap == 7:
                printDelay('gannon falls to the ground')
                printDelay('you did it you defeated ganon and saved the princes')
                printDelay('you won congrats!')
                stap = 0