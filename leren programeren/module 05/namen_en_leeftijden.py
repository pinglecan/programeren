def naam_leeftijd(dictionairy: list):
    userinput_naam = input('wat is uw naam ').lower()
    userinput_leeftijd = input('wat is uw leeftijd ').lower()
    dictionairy ={
    'naam' : userinput_naam,
    'leeftijd' : userinput_leeftijd
    }
    return dictionairy

namen_en_leeftijden = []



stop = False

while not stop:
    naam_leeftijd(namen_en_leeftijden)
    stoppen =input('Toets enter om door te gaan of stop om te printen  ').lower()
    if stoppen == 'stop':
        stop = True

for naam in namen_en_leeftijden:
    print(f'{naam["naam"]} is {naam["leeftijd"]}')
