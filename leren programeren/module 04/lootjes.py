from random import shuffle
list_met_namen_1 = []
list_met_namen_2 = []
stop = False
test = False

while not stop:
    userinput =input('geef een naam voor op het lootje  ')
    if userinput not in list_met_namen_1:
        list_met_namen_1.append(userinput)
        list_met_namen_2.append(userinput)
    else :
        print('deze naam is al een lootje')

    if len(list_met_namen_1) >= 3:
        nog_een_naam = input('wil je nog een naam toevoegen?  ').lower()
        if nog_een_naam == 'nee':
           stop = True

shuffle(list_met_namen_1)


while not test:
    shuffle(list_met_namen_1)
    test = True
    for x in range(0,len(list_met_namen_2)):
        if list_met_namen_1[x] == list_met_namen_2[x]:
            test = False
for x in range(0,len(list_met_namen_2)):
    print(f'{list_met_namen_1[x]} heeft {list_met_namen_2[x]} getrtestken')