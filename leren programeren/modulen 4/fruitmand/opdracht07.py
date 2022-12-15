from fruitmand import fruitmand

for entry in fruitmand:
    if entry['round'] == True:
        print(entry['name'])
        print('is rond')