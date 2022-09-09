ticket = 7.45
vrprijs = 0.074
 
vrienden = int(input('hoeveel mensen komen mee?  '))
print(f'{vrienden} mensen komen mee')


minuten = int(input('hoeveel minuten wil je VR gamen?  '))

totaal = (ticket * vrienden) + ((minuten * vrprijs) * vrienden)
print (f'Dit geweldige dagje-uit met {vrienden} mensen in de speelhal ')
print(f'met {minuten} VR kost je maar {totaal} euro')