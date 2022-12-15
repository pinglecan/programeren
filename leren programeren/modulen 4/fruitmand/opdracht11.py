from fruitmand import fruitmand


kleur_kiezen = True
while kleur_kiezen == True:
    user_kleur = input('kies een kleur  ')
    if user_kleur not in fruitmand['color']:
        f'De kleur {user_kleur} zit er niet in de fruitmand'
    else:
        kleur_kiezen == False