from fruitmand import fruitmand

roundtrue = 0
roundfalse = 0
kleur_kiezen = True

while kleur_kiezen == True:
    user_kleur = input('kies een kleur  ')
    for i in fruitmand:
        if user_kleur == i['color']:
            if i['round']:
                roundtrue += 1
            else:
                roundfalse += 1
            kleur_kiezen = False
            
    if kleur_kiezen == True:
        f'De kleur {user_kleur} zit er niet in de fruitmand'




if roundtrue > roundfalse:
    print(f'Er zijn {roundtrue - roundfalse} meer ronde vruchten dan niet ronde vruchten in de kleur {user_kleur}')
elif roundtrue < roundfalse:
    print(f'Er zijn {abs(roundtrue - roundfalse)} minder ronde vruchten dan niet ronde vruchten in de kleur {user_kleur}')

print(f'Er zijn {roundtrue} ronde vruchten en {roundfalse} niet ronde vruchten in de kleur {user_kleur}')