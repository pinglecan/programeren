import random 
witte_socken = 0
zwarte_socken = 0
stop = False
while stop == False:
    sokken = random.randint(0,20)
    if sokken <= 10:
        print("witte sock")
        witte_socken += 1
    elif sokken > 10:
        print('zwarte sock')
        zwarte_socken += 1
    if witte_socken == 2 or zwarte_socken == 2:
        stop = True


print(f"{witte_socken} witte socken {zwarte_socken} zwarte socken")