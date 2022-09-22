iphone_prijs = int(input('hoe duur is de iphone?  '))
samsung_prijs = int(input('hoe duur is de samsung?  '))
buget = int(input('wat is je buget?  '))
if iphone_prijs < buget or samsung_prijs < buget:
    if iphone_prijs < samsung_prijs:
        print(f'de samsung is het duurst, de telefoon kost: {samsung_prijs} euro ')
        print(f'de iphone is het goedkoopst, de telefoon kost: {iphone_prijs} euro ') 
        prijsverschil = samsung_prijs - iphone_prijs
        print(f'Het advies is dus de iphone te kopen. Deze is namelijk {prijsverschil} euro goedkoper dan de samsung')
    elif  iphone_prijs > samsung_prijs:
        prijsverschil = iphone_prijs - samsung_prijs
        print(f'de iphone is het duurst, de telefoon kost: {iphone_prijs} euro ')
        print(f'de samsung is het goedkoopst, de telefoon kost: {samsung_prijs} euro ')
        if iphone_prijs <= samsung_prijs + 50 :
            print(f'Het advies is dus de iphone te kopen. Deze is namelijk {prijsverschil} euro duurder dan de samsung')
        else:
            print(f'Het advies is dus de samsung te kopen. Deze is namelijk {prijsverschil} euro goedkoper dan de iphone')
    elif iphone_prijs == samsung_prijs:
        print(f'bijde telefoons kosten {iphone_prijs} dus het advies is ga voor de iphone')
elif iphone_prijs > buget and samsung_prijs > buget:
    if iphone_prijs > samsung_prijs:
        print(f'de iphone is het duurst, de telefoon kost: {iphone_prijs} euro ')
        print(f'de samsung is het goedkoopst, de telefoon kost: {samsung_prijs} euro ')
        print ('het advies is koop geen telefoon ze zijn allemaal te duur.')
    elif samsung_prijs<iphone_prijs:
        print(f'de samsung is het duurst, de telefoon kost: {samsung_prijs} euro ')
        print(f'de iphone is het goedkoopst, de telefoon kost: {iphone_prijs} euro ')
        print ('het advies is koop geen telefoon ze zijn allemaal te duur.')
    else :
        print(f'bijde telefoons kosten {iphone_prijs} dus het advies is koop geen telefoon')