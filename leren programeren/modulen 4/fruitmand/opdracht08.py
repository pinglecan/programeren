from fruitmand import fruitmand
total_weight_fruit = 0

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 3000,
    'color' : 'green',
    'round' : True
})

for entry in fruitmand:
    if entry['weight'] > 0:
        total_weight_fruit += entry['weight']

print(total_weight_fruit)