from fruitmand import fruitmand

regenboog_fruit =[]
for i in range(len(fruitmand)):
    if fruitmand[i]['name'] == 'druif':
        del fruitmand[i]
        break

for entry in fruitmand:
    if entry['color'] not in regenboog_fruit:
        regenboog_fruit.append(entry['color'])
print(regenboog_fruit)