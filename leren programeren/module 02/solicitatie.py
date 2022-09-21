geslacht = input('bent u een man of een vrouw?  ')


dieren_dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?  '))
jongleren = int(input('hoeveel jaar ervaring jongleren heeft u?  '))
acrobatiek = int(input('hoeveel jaar ervaring acrobatiek heeft u?  '))
diploma = input('heeft u een MBO-4 ondernemings diploma?  ')
rijbewijs= input('heeft u een geldig Vrachtwagen rijbewijs?  ')
input('heeft u een extreem grote lepel?  ')
hoge_hoed= input('heeft u een hoge hoed?  ')
input('heeft u teken of schilder kunsten?  ')
input('heeft u een criminele achtergrond?  ')
lengte = int(input('hoe lang bent u in cm?  '))
dik = int(input('wat is uw lichaamsgewicht?  '))
if geslacht == "vrouw":
    haar_kleur=input('heeft u rood krull haar?  ')
    haar_lengte = int(input('hoe lang is uw haar?  '))
elif geslacht == "man":
    snor=input('heeft u een snor?  ')
    breed_snor = int(input('hoe breed is uw snor in cm?  '))
Overleven_met_gevaarlijk_personeel = input('Heeft u het Certificaat Overleven met gevaarlijk personeel?  ')
input('heeft u redit?  ')
if dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >=3:
    if geslacht == "man":
         if diploma ==('JA') or ('ja') or ('Ja') and rijbewijs == ('JA') or ('ja') or ('Ja') and hoge_hoed == ('JA') or ('ja') or ('Ja') and snor == ('JA') or ('ja') or ('Ja') and breed_snor >= 10 and lengte > 150 and dik > 90 and Overleven_met_gevaarlijk_personeel == ('JA') or ('ja') or ('Ja'):
            print ('u bent aan genomen')
         else :
            print('u bent niet aan genomen')
    elif geslacht == "vrouw":
            if diploma ==('JA') or ('ja') or ('Ja') and rijbewijs == ('JA') or ('ja') or ('Ja') and hoge_hoed == ('JA') or ('ja') or ('Ja') and haar_kleur == ('JA') or ('ja') or ('Ja') and haar_lengte >= 20 and lengte > 150 and dik > 90 and Overleven_met_gevaarlijk_personeel == ('JA') or ('ja') or ('Ja'):
                print('u bent aan genomen')
            else :
                print( "u bent niet aan genomen")
else:
    print('u bent niet aan genomen')