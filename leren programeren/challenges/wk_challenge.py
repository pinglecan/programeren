punten_land_1 = 0
punten_land_2 = 0
punten_land_3 = 0
doelsaldo_land3 = 0


land_1 = input('wat is het eerste land uit groep A? ')
land_2 = input('wat is het tweede land uit groep A? ')
land_3 = input('wat is het derde  land uit groep A? ')

print(f'''
wedstrijd | thuis | uit | doelpunten land 1 | doelpunten land 2| winnaar
1         |{land_1} |{land_2} |             |                  | 
2         |{land_2} |{land_3}|              |                  |
3         |{land_1} |{land_3}|              |                  |
''')
print('')
print(f'wat is de uitslag van wedstrijd 1 {land_1} vs {land_2}')
w1_doel_punten_land_1 = int(input(f'hoeveel goals heeft {land_1} geschoord? '))
w1_doel_punten_land_2 = int(input(f'hoeveel goals heeft {land_2} geschoord? '))

if w1_doel_punten_land_1 > w1_doel_punten_land_2:
    winnaar_1 = land_1
    punten_land_1 += 3
    punten_land_2 += 0
else:
    winnaar_1 = land_2
    punten_land_1+= 0
    punten_land_2 += 3

doelsaldo_land1 = w1_doel_punten_land_1 - w1_doel_punten_land_2
doelsaldo_land2 = w1_doel_punten_land_2 - w1_doel_punten_land_1

print(f'''
Wedstrijd {land_1} - {land_2} eindigde in {w1_doel_punten_land_1} - {w1_doel_punten_land_2} 
{land_1}: punten:   {punten_land_1}  doelsaldo:  {doelsaldo_land1}
{land_2}: punten:   {punten_land_2}  doelsaldo:  {doelsaldo_land2}
{land_3}: punten:   {punten_land_3}  doelsaldo:  {doelsaldo_land3}
''')

w2_doel_punten_land_2 = int(input(f'hoeveel goals heeft {land_2} geschoord? '))
w2_doel_punten_land_3 = int(input(f'hoeveel goals heeft {land_3} geschoord? '))

if w2_doel_punten_land_2 > w2_doel_punten_land_3:
    winnaar_2 = land_2
    punten_land_2 += 3
    punten_land_3 += 0
else:
    winnaar_2 = land_3
    punten_land_2+= 0
    punten_land_3 += 3

doelsaldo_land2 += w2_doel_punten_land_2 - w2_doel_punten_land_3
doelsaldo_land3 += w2_doel_punten_land_3 - w2_doel_punten_land_3

print(f'''
Wedstrijd {land_2} - {land_3} eindigde in {w2_doel_punten_land_2} - {w2_doel_punten_land_3} 
{land_1}: punten:   {punten_land_1}  doelsaldo:  {doelsaldo_land1}
{land_2}: punten:   {punten_land_2}  doelsaldo:  {doelsaldo_land2}
{land_3}: punten:   {punten_land_3}  doelsaldo:  {doelsaldo_land3}
''')







# print(f'''
# wedstrijd | thuis | uit | doelpunten land 1 | doelpunten land 2| winnaar
# 1         |{land_1} |{land_2} |        {w1_doel_punten_land_1}     |    {w1_doel_punten_land_2}    |          {winnaar_1} 
# 2         |{land_2} |{land_3}|              |                  |
# 3         |{land_1} |{land_3}|              |                  |
# ''')
# print('')