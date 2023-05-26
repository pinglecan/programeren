#import
import Pingle_funcions
from Pingle_funcions import ep

#variable
container = ''
stap = 1
meer_bestellen = False

#ijssalon programma

print('Welkom bijPapi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

while stap == 1:
    ep()
    print('Hoeveelbolletjes wilt u?')
    ep()
    aantal = int(input('antwoord klant:  '))

    if aantal >=1 and aantal <=4:
        stap = 2
    elif aantal >=5 and aantal <=8:
        stap = 3
        container = 'bakje'
    elif aantal > 8:
        print("Sorry, zulke grotebakken hebben we niet")
    else :
        print( "Sorry dat snap ik niet...")

while stap == 2:
    ep()
    print(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?')
    ep()
    container= input("antwoord klant:  ")
    if container == 'bakje' or container == 'hoorntje':
        stap = 3
    else:
        print('Sorry, dat snap ik niet..')

while stap == 3:
    ep()
    print(f"Hier is uw {container} met {aantal} bolletje(s).")
    ep()
    print("Wilt u nog meer bestellen?")
    ep()
    meer_bestellen=input("antwoord klant")