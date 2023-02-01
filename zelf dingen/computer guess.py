import random

ronde = 1

while ronde > 0:
    ronde += 1
    nummer = random.randint(1,10000)
    print(nummer)
    if nummer == 20:
        print('Goed gedaan!')
        print(f'{ronde} aantal rondes')
        break