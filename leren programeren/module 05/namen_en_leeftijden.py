def naam_leeftijd(x: list):
    ghk = {}
    userimput_naam = input('wat is uw naam ')
    userimput_leeftijd = int(input('wat is uw leeftijd '))
    ghk.update('naam' : userimput_naam, 'leeftijd' : userimput_leeftijd)
    return x

namen_en_leeftijden = []

print(naam_leeftijd(namen_en_leeftijden))