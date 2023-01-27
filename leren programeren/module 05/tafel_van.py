def tafel(tafel_van):
    som = ''
    for keer in range(1,10):
        som += f'{keer} x {tafel_van} = {tafel_van * keer}\n'
    return som

print(tafel(int(input('Van welk getal wilt u de tafel zien? '))))