def naam_leeftijd(x: list):
    print('als u wilt stoppen type stop om the stoppen')
    userinput_naam = input('wat is uw naam ').lower
    userinput_leeftijd = input('wat is uw leeftijd ').lower
    namen_en_leeftijden.append({
    'naam' : userinput_naam,
    'leeftijd' : userinput_leeftijd
    })
    if userinput_leeftijd or userinput_naam == 'stop':
        return x

namen_en_leeftijden = []

naam_leeftijd(namen_en_leeftijden)


print(namen_en_leeftijden)