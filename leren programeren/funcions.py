def print_epic(dct):
    for item, amount in dct.items():
        print("{}x {}".format(amount, item))


def printDelay(t: str, d=2):
    import time 
    time.sleep(d)
    print(t)

def clear_console():
    import os
    from turtle import clear
    os.system('cls')