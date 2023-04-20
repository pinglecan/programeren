import os
from turtle import clear
import time 
import random

def print_epic(dct):
    for item, amount in dct.items():
        print("{}x {}".format(amount, item))


def printDelay(t: str, d=2):
    time.sleep(d)
    print(t)

def clear_console():
    os.system('cls')

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    returnlist = []
    for entry in range (0,len(list)):
        if list[entry][key] == value: 
                returnlist.append(list[entry])
    return returnlist

def loading_screen():
    loop = False
    precent = 0
    while loop ==False:
        precent_plus = random.randint(1, 10)
        precent = precent + precent_plus
        if precent > 100:
            precent = 100
        print(f'loading {precent}%')
        time.sleep(1)
        os.system('cls')
        if precent == 100:
            return 0 