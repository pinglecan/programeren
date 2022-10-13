lengte = float(input('hoe lang is het zwembad?  '))
breedte = float(input('you breed is het zwembad?  '))
diepte = float(input('hoe diep is het zwembad?  '))
zwembad_grond = lengte * breedte * diepte
kosten_uitgraven = zwembad_grond * 25
kosten_afvoer_grond = zwembad_grond * 32.50
voorrijkosten = 250 + (2.05 * 60)
totaal = kosten_afvoer_grond + kosten_uitgraven + voorrijkosten
print(f'Offerte vaan een zwembad van 8 bij 3 bij 1,5 meter (inhoud:{zwembad_grond} m3')
print(f'Uitgraven: €{kosten_uitgraven} ')
print(f'Afvoeren grond: €{kosten_afvoer_grond}')
print(f'voorrijkkosten: €{voorrijkosten}')
print(f'Totaal €{totaal}')