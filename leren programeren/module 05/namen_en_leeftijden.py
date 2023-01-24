def naam_leeftijd(x: list):
    userinput_naam = input('wat is uw naam ').lower()
    userinput_leeftijd = input('wat is uw leeftijd ').lower()
    namen_en_leeftijden.append({
    'naam' : userinput_naam,
    'leeftijd' : userinput_leeftijd
    })
    return x

namen_en_leeftijden = []


stop = False

while not stop:
    naam_leeftijd(namen_en_leeftijden)
    stoppen =input('Toets enter om door te gaan of stop om te printen  ').lower()
    if stoppen == 'stop':
        stop = True
print(namen_en_leeftijden)

for naam in namen_en_leeftijden:
    print(naam['naam'])