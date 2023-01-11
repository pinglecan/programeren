from fruitmand import fruitmand

for entry in fruitmand:
    if entry['round']:
        print(entry['name'])
        print('is rond')