#import
import Pingle_funcions

#variable
container = ''
stap = 1

#ijssalon programma

print('Welkom bijPapi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
print('')

while stap == 1:
    print('Hoeveelbolletjes wilt u?')
    print('')
    aantal = input('antwoord klant:  ')

    if aantal >=1 and aantal <=4:
        stap = 2
    elif aantal >=5 and aantal <=8:
        stap = 3
    elif aantal > 8:
        print("Sorry, zulke grotebakken hebben we niet")