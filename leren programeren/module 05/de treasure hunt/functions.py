import time
from termcolor import colored
from data import *
import math

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return round(amount / 10, 2)

def silver2gold(amount:int) -> float:
    return round(amount / 5, 2)

def copper2gold(amount:int) -> float:
    return round(silver2gold(copper2silver(amount)), 2)

def platinum2gold(amount:int) -> float:
    return round(amount * 25, 2)

def getPersonCashInGold(personCash:dict) -> float:
    gold = 0
    gold += platinum2gold(personCash['platinum'])
    gold += personCash['gold']
    gold += silver2gold(personCash['silver'])
    gold += copper2gold(personCash['copper'])
    return gold

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    return round(copper2gold(((people*4) + (horses *3)) * JOURNEY_IN_DAYS),2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    returnlist = []
    for entry in range (0,len(list)):
        if list[entry][key] == value: 
                returnlist.append(list[entry])
    return returnlist

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people,'adventuring',True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends,'shareWith',True)

def getAdventuringFriends(friends:list) -> list:
    returnlist= []
    for entry in range (0,len(friends)):
        if friends[entry]['adventuring'] and friends[entry]['shareWith']: 
            returnlist.append(friends[entry])
    return returnlist 

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people/2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people/3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return math.ceil((tents)) * math.ceil((COST_TENT_GOLD_PER_WEEK * math.ceil((JOURNEY_IN_DAYS/ 7)))) + silver2gold( horses *COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS 

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    listy =[]
    for entry in items:
        iets = ''
        iets += str(entry['amount'])
        iets += entry['unit']
        iets +=' '
        iets += entry['name']
        listy.append(iets)
    return ', '.join(listy)


def getItemsValueInGold(items:list) -> float:
    price_in_gold = 0
    for entry_price in items:
        unit = entry_price['price']["type"]
        amount = entry_price['price']['amount']
        if unit == 'copper':
            price_in_gold += copper2gold(amount) * entry_price['amount']
        elif  unit == 'silver':
            price_in_gold += silver2gold(amount) * entry_price['amount']
        elif unit == 'gold':
            price_in_gold += amount * entry_price['amount']
        elif unit == 'platinum':
            price_in_gold += platinum2gold(amount) * entry_price['amount']
    return price_in_gold

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    money_in_gold = 0
    for entry in people:
        money_in_gold += platinum2gold(entry['cash']['platinum'])
        money_in_gold += entry['cash']['gold']
        money_in_gold += silver2gold(entry['cash']['silver'])
        money_in_gold += copper2gold(entry['cash']['copper'])
    return money_in_gold

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    candadates = []
    for entry in investors:
        if entry['profitReturn'] <= 10:
            candadates.append(entry)
    return candadates

def getAdventuringInvestors(investors:list) -> list:
   return getFromListByKeyIs(investors,'adventuring',True)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    people =  getAdventuringInvestors(getInterestingInvestors(investors))
    rentalCost = getTotalRentalCost(1,1)
    foodCost = getJourneyFoodCostsInGold(1,1)
    total = (getItemsValueInGold(gear)  + rentalCost + foodCost) * len(people)
    return total

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    people_cost = silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT)
    horse_cost = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)
    if leftoverGold == 0:
        return 0
    else:
        return round(leftoverGold //(people_cost + horse_cost))

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    return round((silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT) + copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)) *nightsInInn,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    cuts = []
    for enrty in getInterestingInvestors(investors):
      cuts.append(round(profitGold / 100 * enrty['profitReturn'],2))
    return cuts

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    for entry in investorsCuts:
          profitGold -= entry
    return round(profitGold / fellowship,2)

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    time.sleep(0.5)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()