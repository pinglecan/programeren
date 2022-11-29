def print_epic(dct):
    for item, amount in dct.items():
        print("{}x {}".format(amount, item))

stop = False

lijstje = {}

while stop !=True:
    userinputkey = input('wat wil je hebben?  ').lower()
    userinputint = int(input('hoeveel wil je hebben?  '))
    lijstje.update({userinputkey: userinputint})
    stopen = input('type stop om te stoppen  ').lower()
    if stopen == 'stop':
        stop = True
    
print('-[bootschappenlijst]-')
print_epic(lijstje)
print('---------------------------------')