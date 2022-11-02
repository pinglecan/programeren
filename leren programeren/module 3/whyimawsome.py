import random
naam = input('hoe heet je  ')
numer = int(input('geef een numer  '))
niet_reapeat = 0
for x in range(numer):
    compiment_random = random.randint(1,4)
    while niet_reapeat == compiment_random:
        compiment_random = random.randint(1,4)
    if compiment_random == 1:
        print(f'Je bent geweldig {naam}')
    elif compiment_random == 2:
        print(f'je bent heel cool {naam}')
    elif compiment_random == 3:
        print(f'je bent epic {naam}')
    elif compiment_random == 4:
        print(f'je bent erg aardig {naam}')
    niet_reapeat = compiment_random