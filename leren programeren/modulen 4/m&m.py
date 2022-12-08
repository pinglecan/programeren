from random import randint
zak_met_mm =[]
kleuren=['oranje', 'blauw','groen','bruin']
aantal_m_m= int(input('hoeveel M&Ms  '))

for i in range(0, aantal_m_m):
    random_MM = randint(0,3)
    zak_met_mm.append(kleuren[random_MM]) #je kan ook random.choice gebruiken

print(zak_met_mm)