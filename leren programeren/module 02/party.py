gastheer= input('Wat is uw naam?  ').lower()
gasten = 12
drank = True
chips = False

aanwezige = gasten if gastheer == '' else gasten +1 

if gastheer == '' or drank and gastheer!='rudi' and gasten < 12 and (gastheer or gasten >= 5):
    print('start the party')
else:
    print('No party')