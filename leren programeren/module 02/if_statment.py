a = int(input('geef een heel nummer '))
b = int(input('geef nog een ander heel nummer  '))



if a > b:
    Max = a
    Min = b
    print(f'a is het grootste getal:{Max}')
elif a < b :
    Min = a
    Max = b
    print(f'a is het kleinste getal:{Min}')
else: 
    print(f'a en b zijn even groot')
    Min = a
    Max = b
print(f'Het minimum is:{Min}')
print(f'het maximum is {Max}')