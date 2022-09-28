# Jelle Fiere pizza calculator
small = 2.50
medium = 3.99
large = 5.99
try:
    smallaantal=int(input('hoe veel small pizzas wilt u?  '))
    smallprijs = small * smallaantal
except :
    print('Voer een getal in als nummer')
    exit()
try:
    mediumaantal=int(input('hoe veel medium pizzas wilt u?  '))
    mediumprijs = medium * mediumaantal
except:
    print('voer een getal in als numer')
    exit()
try:
    largeaantal=int(input('hoe veel large pizzas wilt u?  '))
    largeprijs = large * largeaantal
except:
    print('voer een getal in als numer')
    exit()

print('')
print('')
print('')
print('')


totaal = smallprijs + mediumprijs + largeprijs
print(f'_______________________')
print(f'|small x {smallaantal} = {smallprijs}          ')
print(f'|                                 ')
print(f'| medium x {mediumaantal} = {mediumprijs}    ')
print(f'|                               ')
print(f'| large x {largeaantal} = {mediumprijs}     ')
print(f'|                               ')
print(f'|totaal = {totaal}')