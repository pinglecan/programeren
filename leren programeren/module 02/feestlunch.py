croisantprijs = int(input('hoeveel cent kost 1 croisant?  ')) #39 cent        
stokbroodprijs = int(input('hoeveel cent kost 1 stok brood?  ')) #278 cent

xc = int(input('hoeveel croisantjes?  '))  #17
print(f'oke {xc} cr39oisantjes')
totaalcroisant = xc * croisantprijs


xs=int(input('hoeveel stokbrood?  '))   #2
print(f'oke {xs} stokbroden')
totaalstokbrood= stokbroodprijs * xs


ak=int(input ('hoeveel kortings bonnen?  '))   # 3
print(f'oke {ak} kortings bonnen')


wk= int(input('hoeveel cent is elke kortings bon waard?  ')) #50

korting= ak * wk

totaalprijs = (totaalcroisant + totaalstokbrood) - korting

print(f'De feestlunch kost je bij de bakker {totaalprijs} cent voor')     #9.91
print(f'de {xc} croissantjes en de {xs} stokbroden als de {ak} kortingsbonnen')
print(f'nog geldig zijn')