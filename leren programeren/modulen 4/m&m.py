from random import randint
m_en_m =[]
M_M=['oranje', 'blauw','groen','bruin']
aantal_m_m= int(input('hoeveel M&Ms  '))

for i in range(0, aantal_m_m):
    random_MMMM = randint(0,3)
    m_en_m.append(M_M[random_MMMM])

print(m_en_m)