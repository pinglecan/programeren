croisantprijs = 0.39
stokbroodprijs = 2.78

xc = int(input('hoeveel croisantjes?  '))
print(f'oke {xc} croisantjes')
totaalcroisant = xc * croisantprijs


xs=int(input('hoeveel stokbrood?  '))
print(f'oke {xs} stokbroden')
totaalstokbrood= stokbroodprijs * xs


ak=int(input ('hoeveel kortings bonnen?  '))
print(f'oke {ak} kortings bonnen')


wk=0.517

korting= ak * wk

totaalprijs = (totaalcroisant + totaalstokbrood) - korting

print(f'De feestlunch kost je bij de bakker {totaalprijs} euro voor')
print(f'de {xc} croissantjes en de {xs} stokbroden als de {ak} kortingsbonnen')
print(f'nog geldig zijn')