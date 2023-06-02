#import
import Pingle_funcions
from Pingle_funcions import ep
import ijs_functions

#variable
meer_bestellen = True

#ijssalon programma

print('Welkom bijPapi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
while meer_bestellen == True:
    ijs_functions.bestellen()
    ep()
    print("Wilt u nog meer bestellen?")
    ep()
    meer_bestellen=input("antwoord klant:  ")
    ep()
    if meer_bestellen == 'nee':
        meer_bestellen = False
    elif meer_bestellen == "ja":
        meer_bestellen = True
    else:
        print('Sorry, dat snap ik niet..')
