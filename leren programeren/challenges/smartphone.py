iphone_prijs = int(input('hoe duur is de iphone?  '))
samsung_prijs = int(input('hoe duur is de samsung?  '))
if iphone_prijs < samsung_prijs:
    print(f'de samsung is het duurst, de telefoon kost: {samsung_prijs} euro ')
    print(f'de iphone is het goedkoopst, de telefoon kost: {iphone_prijs} euro ') 
    prijsverschil = samsung_prijs - iphone_prijs
    print(f'Het advies is dus de iphone te kopen. Deze is namelijk {prijsverschil} euro goedkoper dan de samsung')
elif  iphone_prijs > samsung_prijs:
    print(f'de iphone is het duurst, de telefoon kost: {iphone_prijs} euro ')
    print(f'de samsung is het goedkoopst, de telefoon kost: {samsung_prijs} euro ')
    if iphone_prijs <= samsung_prijs + 50 :
        prijsverschil = iphone_prijs - samsung_prijs
        print(f'Het advies is dus de iphone te kopen. Deze is namelijk {prijsverschil} euro duurder dan de samsung')