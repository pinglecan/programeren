import random
import os
def clear_console():
    os.system('cls')
Start = input('LINK START!')
print('Please enter your name.')
naam = input()
print('Please select your age.')
leeftijd = input()
print('Choose your gender.')
gender = input().lower()
if gender != 'male' and gender != 'female':
    raise NameError ('Please choose between male or female.')
################################################################################################
Class = print('Please select one of 3 classes, you have the mage, the swordsman/woman or the archer.')
Mage = input('Would you like to choose the mage class?').lower()
if Mage == 'yes':
    Attacks = ('Cast Fireball, Cast Lightning Strike, Cast Quake.')
    One = random.randint(5,10)                # Cast Fireball
    Two = random.randint(5,15)                # Cast Lightning Strike
    Three = random.randint(0,20)              # Cast Quake
    print('You have chosen the mage class. you get 3 casts. Welcome to the Accel World!')
elif Mage == 'no':
    Swordsman = input('Would you like the swordsman class?').lower()
    if Swordsman == 'yes':
        Attacks = ('Stab, Cross Slash, Vorpal Strike. ')
        One = random.randint(5,10)          # Stab
        Two = random.randint(5,15)          # Cross Slash
        Three = random.randint(0,20)        # Vorpal Strike
        print('You have chosen the swordsman class. You get 3 swordskills. Welcome to the Accel World!')
    elif Swordsman == 'no':
        Archer = input('Would you like the archer class?').lower()
        if Archer == 'yes':
            Attacks = ('Flame arrow, Freeze shot, Multishot.')
            One = random.randint(5,10)               # Flame Arrow
            Two = random.randint(5,15)               # Freeze Shot
            Three = random.randint(0,20)             # Multishot
            print('You have chosen the Archer class. you get 3 boosted shots. Welcome to the Accel World!')
        elif Archer == 'no':
            raise NameError ('Please select a class')
############################################################################################################  
input('You wake up in this weird new world called Accel World.')
input('You take an look around and notice you were spawned in a field next to town')
TownOrField = input('Would you like to enter the town to your right or to the forest on the left? Choose between left or right:').lower()
if TownOrField == 'right':
    print('You go to town and see an Tavern called the Boar Hat')
    input('In this tavern you meet a trader named Meliodas.')
    input('Meliodas asks:"Are you new around here?"')
    input('You say yes and ask him about this world')
    input('He tells you about this world and specifically about dungeons')
    Dungeon = input('Would you like to go to the dungeon? Choose between yes or no:').lower()
    if Dungeon == 'yes':
        input('You say goodbye to Meliodas and go to the dungeon')
        input('You find the entrance of the dungeon and enter the dungeon')
        input('As you wander around the dungeon, you look for enemys to battle')
        input('You encounter goblins! Prepare to attack!')
        GoblinHP = 75
        PlayerHP = 100
    while GoblinHP > 0:
        clear_console()
        EnemyDMG = random.randint(5,10)
        print(f'''
        Fight!
                    {naam} = Je HP = {PlayerHP}            Goblin HP = {GoblinHP}

        
            Choose your attack
            {Attacks}                           ''')

        PickAttack = input(': ').lower()
        if PickAttack == 'one':
            GoblinHP = GoblinHP - One
            PlayerHP = PlayerHP - EnemyDMG
        elif PickAttack == 'two':
            GoblinHP = GoblinHP - Two
            PlayerHP = PlayerHP - EnemyDMG
        elif PickAttack == 'three':
            GoblinHP = GoblinHP - Three
            PlayerHP = PlayerHP - EnemyDMG
        else:
            print('Please choose between: One, Two, or Three.')

        if PlayerHP <= 0:
            print('YOU DIED.')
            exit()

     
    print('You have defeated the monsters on this floor. You may advance to the next floor, I wish you luck.')
    input('Welcome to the second floor, on this floor you will find another dungeon with new monsters.')
    input('You see a road on decide to walk down the road until see an adventurers guild.')
    input('You walk in and meet the guild leader called Kelvin.')
    input('You ask him about this dungeon and the monsters on this dungeon and what kind of species they are.')
    input('He tells you they are called ghouls, and what they can do.')
    input('Kelvin says that they are like humans, but they eat flesh from humans.')
    input('Kelvin offers you a place for tonight.')
    input('You accept, and go to your room and take some well deserved rest.')
    input('You wake up see Kelvin, and tell him you are going to this floors dungeon.')
    input('Kelvin wishes you luck, and you leave the guild, and you are on your way to the dungeon.')
    input('As you wander around the dungeon looking for the Ghouls that Kelvin spoke of.')
    input('You encounter a Ghoul! Prepare to attack!')
######################################################################################################################################
    GhoulHP = 100
    PlayerHP = 100
while GhoulHP > 0:
    clear_console()
    EnemyDMG = random.randint(5,10)   
    print(f'''
    Fight!
                {naam} = Je HP = {PlayerHP}            Ghoul HP = {GhoulHP}

    
          Choose your attack
        {Attacks}                           ''')

    PickAttack = input(': ').lower()
    if PickAttack == 'one':
                GhoulHP = GhoulHP - One
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'two':
                GhoulHP = GhoulHP - Two
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'three':
                GhoulHP = GhoulHP - Three
                PlayerHP = PlayerHP - EnemyDMG
    else:
        print('Please choose between: One, Two, or Three.')

    if PlayerHP <= 0:
                print('YOU DIED.')
                exit()
####################################################################################################################################    
print('You have defeated the monsters on this floor. You may advance to the next floor, I wish you luck')
input('As you walk out of the third dungeon, you see the beautifull green landscape with a beautifull blue sky.')
input('As you walk down the large plain fields, you stare in amazement at the beautifull sky.')
input('You see the main road and decide to walk down the road to look for another adventurers guild.')
input('As you make your way down the road, you see someone play football, but you see him using magic while playing.')
input('This peaks your interest and you make your way to the field.')
input('He sees you walking up to him and he smiles and waves.')
input('You learn that his name is Mark Evans, and that he is the guild leader on this floor.')
input('His guild is called The Knights Of The Blood Oath and you ask him about this floor')
input('Mark Evans asks you if you have armor.')
input('You tell him that you dont have any armor, and he offers you some')
input('But he says that if you want it, that you have to kill a slime to prove your worth.')
input('You accept, because you think that you have no chance of defeating this floors boss')
input('You leave the guild looking for a slime.')
input('As you wander around the field...')
input('You encounter a slime! Prepare for battle.')
SlimeHP = 50
PlayerHP = 100
while SlimeHP > 0:
    clear_console()
    EnemyDMG = random.randint(10,15)   
    print(f'''
    Fight!
                {naam} = Je HP = {PlayerHP}            SLime HP = {SlimeHP}

    
          Choose your attack
        {Attacks}                           ''')

    PickAttack = input(': ').lower()
    if PickAttack == 'one':
                SlimeHP = SlimeHP - One
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'two':
                SlimeHP = SlimeHP - Two
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'three':
                SlimeHP = SlimeHP - Three
                PlayerHP = PlayerHP - EnemyDMG
    else:
        print('Please choose between: One, Two, or Three.')

    if PlayerHP <= 0:
                print('YOU DIED.')
                exit()
input('Congratulations, you won!')
input('It dropped a slime core, you take it with you as proof for Mark')
input('You walk back to town, while enjoying the scenery.')
input('You go back to the field you first met Mark.')
input('And as you guessed, he was playing that magic football again.')
input('You walk up to him and tell him you defeated the slime')
input('Mark asks for proof and you present your slime core.')
input('Mark confirms it, and you walk  back to the guild to pick up your armor')
input('He gives you the armor that raises your HP with 50,')
input('You thank him, and Mark gives you a thumbs up.')
input('You ask Mark about this dungeon')
input('Mark tells you that in this dungeon, the boss is called a Minatour, and that it is known for his massive amount of HP.')
input('Mark wishes you luck, and you leave the guild, and you are on your way to the dungeon.')
input('As you wander around the dungeon looking for the Minotaur that Mark spoke of.')
input('You encounter a Minatour! Prepare to attack!')
Armor = 500
MinotaurHP = 250
PlayerHP = 100 + Armor
while MinotaurHP > 0:
    clear_console()
    EnemyDMG = random.randint(0,5)   
    print(f'''
    Fight!
                {naam} = Je HP = {PlayerHP}            Minotaur HP = {MinotaurHP}

    
          Choose your attack
        {Attacks}                           ''')

    PickAttack = input(': ').lower()
    if PickAttack == 'one':
                MinotaurHP = MinotaurHP - One
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'two':
                MinotaurHP = MinotaurHP - Two
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'three':
                MinotaurHP = MinotaurHP - Three
                PlayerHP = PlayerHP - EnemyDMG
    else:
        print('Please choose between: One, Two, or Three.')

    if PlayerHP <= 0:
                print('YOU DIED.')
                exit()
input('Congratulations, you won!')
input('It dropped an everlasting attack potion!')
input('it increases your attack damage by 5!')
input('You walk onto the next floor, and its a snow biome.')
input('Fortunatly, the armor that Mark gave u has cold resistance.')
input('You look around, and see the snow peacufully falling down, it looks absolutely stunning.')
input('You look for the main road, in hopes of finding a tavern or guild.')
input('After about 5 minutes of walking you stumble upon a guild.')
input('The guild is called Fairy Tail, a guild that specializes in magic.')
input('You look around the guild and find the guild master caled Natsu')
input('Natsu seems to be a very energetic person, since when you found him, he was fighting gray, a mage from that guild.')
input('Natsu is a mage that specializes in fire, while gray specializes on ice, hence the rivalry.')
input('You ask Natsu why he is in this snow biome. He says that he likes this guild very much and doesnt mind the cold, despite being a fire mage')
Quest = input('Natsu asks if you want to do a quest for him? Choose between yes or no:')
if Quest == 'yes':
    input('You chose yes, he tells you the quest is in the forest of this floor.')
    input('You make your way to the forest, but you lost your way and...')
    input('Oh no, you were attacked by a Player Killer!')
    print('YOU DIED')
    exit()
elif Quest == 'no':
    input('Natsu understands, and offers to tell you about the dungeon on this floor.')
    input('You tell Natsu that you would love to hear more about the monster on this dungeons floor.')
    input('Natsu says that the boss on this floor is Called the Red Dragon Emperor.')
    input('He says that the boss is known for its high damage, with for a boss, reasonibly low HP.')
    input('Gray pops up out of nowhere, and he overheard your conversation with Natsu.')
    input('Gray says that the boss is also a Humanoid, so you should watch out.')
    input('Natsu gets angry and says: I WAS JUST ABOUT TO SAY THAT GRAY, and they start fighting again')
    input('You laugh, say goodbye, and make your way to the dungeon')
    input('You go to the dungeon, and enter.')
    input('As you look around, you see another human.')
    input('You want to approach him, but remember Grays words, that the boss is a Humanoid.')
    input('The thing turns around, and you see his arm, the arm of a dragon!')
    input('You encountered the Red Dragon Emperor! Prepare to attack!') 

    Attacks = ('Cast Fireball+, Cast Lightning Strike+, Cast Quake+.')
    One = random.randint(10,15)                # Cast Fireball+
    Two = random.randint(10,20)                # Cast Lightning Strike+
    Three = random.randint(5,25)              # Cast Quake+

    Attacks = ('Stab+, Cross Slash+, Vorpal Strike+. ')
    One = random.randint(10,15)          # Stab+
    Two = random.randint(10,20)           # Cross Slash+
    Three = random.randint(5,25)        # Vorpal Strike+

    Attacks = ('Flame arrow+, Freeze shot+, Multishot+.')
    One = random.randint(10,15)               # Flame Arrow+
    Two = random.randint(10,20)                # Freeze Shot+
    Three = random.randint(5,250)             # Multishot+
Armor = 500
DragonHP = 150
PlayerHP = 100 + Armor
while DragonHP > 0:
    clear_console()
    EnemyDMG = random.randint(10,20)   
    print(f'''
    Fight!
                {naam} = Je HP = {PlayerHP}            Red Dragon Emperor HP = {DragonHP}

    
          Choose your attack
        {Attacks}                           ''')

    PickAttack = input(': ').lower()
    if PickAttack == 'one':
                DragonHP = DragonHP - One
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'two':
                DragonHP = DragonHP - Two
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'three':
                DragonHP = DragonHP - Three
                PlayerHP = PlayerHP - EnemyDMG
    else:
        print('Please choose between: One, Two, or Three.')

    if PlayerHP <= 0:
                print('YOU DIED.')
                exit() 
input('Congratulations, you won!')
input('This floors biome is a jungle.')
input('You look around hoping to find the main route the the guild on this floor.')
input('After 15 minutes of walking, you find the road, and the guild is not much further.')
input('This guild is called The Black Bulls, with its leader called Asta.')
input('You look around the guild, and you notice someone working out as if their life depends on it.')
input('You ask him about the whereabouts of Asta, and he tells you that your looking right at him.')
input('You ask him why he was working out so hard.')
input('He says that he was born without magic, so if he wants to stand a chance against others, he will have to train his body to his limits')
Asta = input('Do you respect him or laugh at him? Choose between respect or laugh')
if Asta == 'laugh':
    input('He gets mad, and attacks you')
    input('You lose, he isnt a guild leader for nothing!')
    print('YOU DIED')
    exit()

elif Asta == 'respect':
    input('He thanks you and offers to tell you about this floors dungeon.')
    input('He tells you that the monster on this floor is called Hollow.')
    input('Asta says that they are known for their balanced but higher stats than average.')
    input('Asta wishes you luck, and you leave the guild, and you are on your way to the dungeon.')
    input('As you wander around the dungeon looking for the Hollow that Asta spoke of...')
    input('You encounter a Hollow! Prepare to attack!')
    Armor = 50
    HollowHP = 175
    PlayerHP = 100 + Armor
    while HollowHP > 0:
        clear_console()
    EnemyDMG = random.randint(10,20)   
    print(f'''
    Fight!
                {naam} = Je HP = {PlayerHP}            Hollow HP = {HollowHP}

    
          Choose your attack
        {Attacks}                           ''')

    PickAttack = input(': ').lower()
    if PickAttack == 'one':
                HollowHP = HollowHP - One
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'two':
                HollowHP = HollowHP - Two
                PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'three':
                HollowHP = HollowHP - Three
                PlayerHP = PlayerHP - EnemyDMG
    else:
        print('Please choose between: One, Two, or Three.')

    if PlayerHP <= 0:
                print('YOU DIED.')
                exit() 
    input('Congratulations, you won!')
    input('You are now on the last floor.')
    input('This floor is a lot like the second, beautifull plains but instead of a sunny, a cloudy sky.')
    input('This floor is a lot easier to navigate than the former jungle one, so you find this guild pretty easily.')
    input('The guild is called The Black Knights, with its well known leader called Lelouch.')
    input('You have heard that Lelouch is quite hard to find, so you try your luck at the guild.')
    input('Fortunatly, people have heard of you, because of your quick progression on the floors.')
    input('Therefore, Lelouch notices you walking inside his guild and meets you in the guild hall.')
    input('Lelouch greets you, you greet him back and ask him about this floors dungeon.')
    input('Lelouch reveals that this boss is a hybrid from a demon and human, a Demonoid to be exact.')
    input('The name of the Demonoid is Zeldris, and is known for overall very high stats.')
    input('Lelouch notices your armor, and says that the armor that you are wearing currently, will not be strong enough.')
    input('Lelouch offers you the newest of new armor, he calls it Incursio, which boosts your HP by 150.')
    input('You are greatfull for his help, so you thank him, and say goodbye te Lelouch')
    input('Lelouch wishes you the best of luck, and you make your way to the last dungeon.')
    input('You walk to the last dungeon entrance. The entrance is a huge door made of gold. You cant help but take a long look at it.')
    input('As you wander around the dungeon looking for the Demonoid called Zeldris that Lelouch spoke of...')
    input('You encounter the Final Boss Zeldris! Prepare to fight!')
    Armor = 150
    ZeldrisHP = 250
    PlayerHP = 100 + Armor
    while ZeldrisHP > 0:
        clear_console()
    EnemyDMG = random.randint(15,25)   
    print(f'''
        Fight!
                    {naam} = Je HP = {PlayerHP}           Zeldris HP = {ZeldrisHP}

        
            Choose your attack
            {Attacks}                           ''')

    PickAttack = input(': ').lower()
    if PickAttack == 'one':
                    ZeldrisHP = ZeldrisHP - One
                    PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'two':
                    ZeldrisHP = ZeldrisHP - Two
                    PlayerHP = PlayerHP - EnemyDMG
    elif PickAttack == 'three':
                    ZeldrisHP = ZeldrisHP - Three
                    PlayerHP = PlayerHP - EnemyDMG
    else:
            print('Please choose between: One, Two, or Three.')

    if PlayerHP <= 0:
                    print('YOU DIED.')
                    exit()
    input('CONGRATULATIONS YOU HAVE BEAT THE GAME ')
    exit()
  
if Dungeon == 'no':
        input('You ask Meliodas if you can stick around and sleep in this tavern')
        input('Meliodas says "If you can pay you can stay for as long as you want."')
        input('You agree to pay Meliodas, and stay the night')
        food = input('The next day Meliodas asks you if you slept well and would like some breakfast.')
        if food == 'yes':
            input('You thank Meliodas for your food, take a bite and spit it out because it tastes like dirt')
            input('Meliodas says,"I just offered you food, I never said that it tastes good" with a grin on his face ')
            input('You laugh and say your goodbyes to Meliodas.')
            DungeonOrForest = input('Would you like to go to the forest now?')
            if DungeonOrForest == 'yes' or DungeonOrForest == 'no':
                print('You walk to the forest looking around and enjoying you surroundings')
                input('But you got lost and its getting dark....')
                input('Oh no, you got sneak attacked by a player killer that hid in the bushes!')
                print('YOU DIED.')
                exit()                

            if food == 'no':
                input('Meliodas says"You got lucky, I have never met someone that did not spit out my terrible food."with a grin on his face')
                input('You laugh and say your goodbyes to Meliodas.')
                
    
if TownOrField =='left':
    print('You walk to the forest looking around and enjoying you surroundings')
    input('But you got lost and its getting dark....')
    input('Oh no, you got sneak attacked by a player killer that hid in the bushes!')
    print('YOU DIED.')
    exit()
