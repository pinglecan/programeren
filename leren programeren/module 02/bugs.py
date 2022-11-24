import random

name = input('Wat is jouw naam? ')
print(f'Hallo, {name}')

favoriteSeason = input(f'Wat is jouw favorite seizoen {name}? A) Lente, B) Zomer, C) Herfst of D) Winter ').lower()

if favoriteSeason == 'a':
    print("Ik hou ook van de lente!")
elif favoriteSeason == 'b':
    print("De zomer is voor mij te warm.")
elif favoriteSeason == 'c':
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif favoriteSeason == 'd':
    print("Is de winter niet erg koud?")
else:
    print("Die ken ik niet...")

favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = random.randint(0,70)
if trueOrFalse >= 51:
    print('Ik vind dat ook een mooie kleur!')
elif trueOrFalse <= 50:
    print(f'TBH, ik hou niet zo van {favoriteColor}...')

num1 = random.randint(1,10)
num2 = random.randint(5,15)
uitkomst = num1 + num2
try:
    number = (input(f'En weet jij wat {num1}+{num2} is? ')) 
    if number == uitkomst:
        print(f'dat klopt {name} het is {number}!')
    else :
        print(f'nee dat klopt niet {name} het is {number}')
except:
    print('Dat is geen nummer!')