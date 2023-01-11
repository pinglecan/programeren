def tafel(x):
    for keer in range(1,11):
        print(f'{keer} x {x} = {x * keer}')


tafel(int(input('Van welk getal wilt u de tafel zien? ')))