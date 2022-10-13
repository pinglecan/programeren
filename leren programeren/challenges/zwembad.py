lengte = float(input('hoe lang is het zwembad?  '))
breedte = float(input('you breed is het zwembad?  '))
diepte = float(input('hoe diep is het zwembad?  '))
tegel_kleur = input('wilt u rode tegels? J/N  ').lower
if tegel_kleur == 'ja' or tegel_kleur =='j':
    tegel_prijs = 20
elif tegel_kleur == 'nee' or tegel_kleur == 'n':
    tegel_prijs = 125
else:
    print('geen goede waarde tegel prijs is nu 69')
    tegel_prijs = 69
vierkante_meter = (lengte * diepte * 2) + (breedte * diepte * 2) +(lengte * breedte)
beton_tegel = (vierkante_meter * 200) + (vierkante_meter * tegel_prijs)
zwembad_grond = lengte * breedte * diepte
kosten_uitgraven = zwembad_grond * 25
kosten_afvoer_grond = zwembad_grond * 32.50
voorrijkosten = 250 + (2.05 * 60)
totaal = kosten_afvoer_grond + kosten_uitgraven + voorrijkosten  + beton_tegel

print(f'Offerte vaan een zwembad van 8 bij 3 bij 1,5 meter (inhoud:{zwembad_grond} m3)')
print(f'Uitgraven: €{kosten_uitgraven} ')
print(f'Afvoeren grond: €{kosten_afvoer_grond}')
print(f'voorrijkkosten: €{voorrijkosten}')
print(f'beton + tegel ({vierkante_meter} m²) €{beton_tegel}')
print(f'Totaal €{totaal}')