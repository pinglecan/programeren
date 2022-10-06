snor_of_haar = False

naam = input('wat is je naam?').lower()
if naam == 'garry' or naam == 'deez nuts':
    raise NameError('Ew cringe')
geslacht = input('bent u een man of een vrouw?  ').lower()

dieren_dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?  '))
jongleren = int(input('hoeveel jaar ervaring jongleren heeft u?  ').lower())
acrobatiek = int(input('hoeveel jaar ervaring acrobatiek heeft u?  ').lower())
diploma = input('heeft u een MBO-4 ondernemings diploma?  ').lower()
rijbewijs= input('heeft u een geldig Vrachtwagen rijbewijs?  ').lower()
discord_mod = input('bent u een discord mod?  ').lower()
if discord_mod == 'ja':
    raise NameError('cringe')
else :
    hoge_hoed= input('heeft u een hoge hoed?  ').lower()
    lengte = int(input('hoe lang bent u in cm?  ').lower())
    dik = int(input('wat is uw lichaamsgewicht?  ').lower())
if geslacht == "vrouw":
    haar_kleur=input('heeft u rood krull haar?  ').lower()
    if haar_kleur =='ja':
        haar_lengte = int(input('hoe lang is uw haar?  ').lower())
        if haar_lengte >=20: snor_of_haar = True 
elif geslacht == "man":
    snor=input('heeft u een snor?  ').lower()
    if snor == 'ja':
        breed_snor = int(input('hoe breed is uw snor in cm?  ').lower())
        if breed_snor >= 10: snor_of_haar = True
Overleven_met_gevaarlijk_personeel = input('Heeft u het Certificaat Overleven met gevaarlijk personeel?  ').lower()
femboy = input('ben je een femboy?')
if femboy == 'ja':
    raise NameError('THERE CAN BE ONLY ONE')
if dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >=3:
    if diploma =='ja' and rijbewijs == 'ja' and hoge_hoed == 'ja' and snor_of_haar == True and lengte > 150 and dik > 90 and Overleven_met_gevaarlijk_personeel == 'ja':
        print ('u bent aan genomen')
    else :
        print('u bent niet aan genomen')
else :
    print('u bent niet aan genomen')