from Pingle_funcions import ep

def bestellen():
    #################
    container = ''
    stap = 1
    ##variable#######

    while stap == 1:
        ep()
        print('Hoeveelbolletjes wilt u?')
        ep()
        aantal = int(input('antwoord klant:  '))

        if aantal >=1 and aantal <=4:
            stap = 2
        elif aantal >=5 and aantal <=8:
            stap = 3
            container = 'bakje'
        elif aantal > 8:
            print("Sorry, zulke grotebakken hebben we niet")
        else :
            print( "Sorry dat snap ik niet...")

    while stap == 2:
        ep()
        print(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?')
        ep()
        container= input("antwoord klant:  ")
        if container == 'bakje' or container == 'hoorntje':
            stap = 3
        else:
            print('Sorry, dat snap ik niet..')

    while stap == 3:
        ep()
        print(f"Hier is uw {container} met {aantal} bolletje(s).")
        stap = 'stop'