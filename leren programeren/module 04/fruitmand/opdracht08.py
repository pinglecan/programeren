from fruitmand import fruitmand
total_weight_fruit = 0

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 3000,
    'color' : 'green',
    'round' : True
})

for entry in fruitmand:
    if entry['weight']:
        total_weight_fruit += entry['weight']

print(entry)