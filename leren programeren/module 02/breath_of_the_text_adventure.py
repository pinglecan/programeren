from pickle import FALSE
import random
from this import d
import time
#shit is false lmao
weapon_axe = False
armor_programming_socks = False
weapon_black_sword = False
weapon_2swords = False
weapon_shield = False
armor_royal_guards_armor = False

# function to print with delay
def printDelay(t: str, d=2):
    time.sleep(d)
    print(t)
#the game real
printDelay('You wake up in a ancient temple you don’t rember anything you walk out into a bright light')
man_or_forest = input('You hear a voice of a woman telling you you have been sleep for the past 100 years you see a old man in the distence do you go towards him Y/N?  ').lower()
if man_or_forest == 'yes' or man_or_forest == 'y':
    printDelay('you decide to go to the old man and talk to him you pick up a stick along the way becouse who doesn’t like sticks?')
    printDelay('"hello young one welcome to the great platue a giant fortified piece of land"')
    printDelay('you talk to him for a bit then you walk towards a old building ')
    axe = input('You see a axe in the discence do you pick it up y/n  ').lower()
    if axe == 'yes' or axe == 'y' :
        weapon_axe = True
    printDelay('You see a button and you press it a big tower emerges from under the building')
    printDelay('You climb down the tower and you see the old man again he tells you to go the shrine towards the east')
    printDelay('You go to the shrine and a old mashine comes to life when it notices you it has a red lazer pointed at you')
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
            printDelay('you find yourself in a treasure room witha orb in the middel ')
            printDelay('you take the orb with you')
            printDelay('you walk out of the temple and see the old man again')
            printDelay('Good job young one now go to the temple of time i shall meet you there again and then he disapears')
            printDelay('you make your way to the temple of time to find the old man')
            printDelay('you find a big stone statue with a hole in could fit the glowing ball')
            ball_in_statue = input('do you put it in Y/N?  ').lower()
            if ball_in_statue == 'y' or ball_in_statue == 'yes':
                printDelay('you put the orb into the statue it opens a trap door behind you')
                open_chest =input('there is a chest under the trap door do you open it? Y/N  ').lower()
                if open_chest == 'yes' or 'y':
                    print('you got some programming socks')
                    armor_programming_socks = True
            printDelay('The old man tells you to come up the later to the roof')
            printDelay('"well young one i think its time for me to tell you who i really am"')
            printDelay('"i was king rhoam bosphoramus hyrule i was the last king of hyrule ')
            printDelay('"you need to kill ganon to save hyrule"')
            printDelay('you head towards the castle ')
            printDelay('you see two posible ways to enter')
            printDelay('you can enter trough the front gate or you could enter via the water')
            how_enter_castle = input('how will you enter?  ').lower
            if how_enter_castle == 'water' or 'via the water' or 'via water' :
                printDelay('You enter via the water you end up in the secret docking area of the castle you find a black sword')
                weapon_black_sword = True
                printDelay('you sneak your way through the palace')
                printDelay('you see some guards in the armory you could fight them to get some armor')
                armory_or_boss = input('do you fight them or do you keep walking?  ')
                if armory_or_boss == 'fight' or 'fight them':
                    sneak_or_head_water = input('do you sneak attack or do you fight them head on?  ')
                    if sneak_or_head_water =='sneak' or 'sneak attack':
                        printDelay('you sneak attack the guards and they die ')
                        printDelay('you loot the armory you got 2 swords a shield and some royal guards armor nice')
                        weapon_2swords = True
                        weapon_shield = True
                        armor_royal_guards_armor = True
                    printDelay('then you walk to the boss room')
                    printDelay('you enter the boss room')