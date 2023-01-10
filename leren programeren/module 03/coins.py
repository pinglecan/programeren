# name of student: Jelle
# number of student: 99071834
# purpose of program: wissel geld berekenen
# function of program: wissel geld
# structure of program: bad


toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #
returned = {}

if change > 0: # als de change hoger is dan 0 print je dit
  coinValue = 500  # dit is hoeveel geld je eerst terug geeft dus 5 euro/ 500 cent
  
  while change > 0 and coinValue > 0: #als coin value en chance boven 0 is dan loopt hij dit voor eeuwig
    nrCoins = change // coinValue # change delen noor coin vallue

    if nrCoins > 0: # als nr boven nul is doet het dit
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
      returned[coinValue] = nrCoinsReturned

# comment on code below: verandert de coin value voor andere soort munt


    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:    
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
print (returned)
if change > 0: # als je het fout heb gedaan print hij dit
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')