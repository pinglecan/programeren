a = int(input('geef een heel nummer '))
b = int(input('geef nog een ander heel nummer  '))



if a > b:
    max = a
    min = b
    print(f'a is het grootste getal:{max}')
    print(f'Het minimum is:{min}')
    print(f'het maximum is {max}')
elif a < b :
    min = a
    max = b
    print(f'a is het kleinste getal:{min}')
    print(f'Het minimum is:{min}')
    print(f'het maximum is {max}')
else: 
    print(f'a en b zijn even groot')
    min = a
    print(f'Het minimum en het maximum zijn:{min}')