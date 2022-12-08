from random import randint

mm_kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin', 'zwart']
aanntal= int(input('hoeveel m&ms moeten er in de zak?  '))

zak_mm = {}
for i in range(aanntal):
    random = randint(0,len(mm_kleuren)-1)
    if  mm_kleuren[random] not in zak_mm:
        zak_mm.update({mm_kleuren[random]:1})
    else:
        x=zak_mm.get(mm_kleuren[random]) +1
        zak_mm.update({mm_kleuren[random]:x})

print(zak_mm)