import random
import os
from turtle import clear
import time
reapear = True
dumb = False
os.system
while reapear == True:
    bitches = input('do you curently have any bitches?  ').lower()
    if bitches == 'no':
        bitch_precent = 0
        while bitches =='no':
            bitch_precent_plus = random.randint(1, 10)
            bitch_precent = bitch_precent + bitch_precent_plus
            if bitch_precent > 100:
                bitch_precent = 100
            print(f'locating bitches {bitch_precent}%')
            time.sleep(1)
            os.system('cls')
            if bitch_precent == 100:
                yes_or_no_bitches = random.randint(1,6)
                if yes_or_no_bitches == 1:
                    print('''
        @@@@@@&&&&&&&%%%%%%%%%%######%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%#%##%#%%#%#%##########%%
        &@@@&&&&&&%%%%%####%%######%%%%#########%%%%%%%%%%%%%%%%%%%%%%%%###%%%##%%%%####%#%%#%%############%
        @@@%%%@&@%%@%%%%*,*%&#####%%%%%%&@%##&%%%&&%%%%%%%&##&(,,/&%%#%%%%&&%%%&&%%%%%%&#&%*,*#&####&/,,#&##
        &&@   .&%  &%#   &*  ,####%   *&   &#&   @#/*   **%&   &&   &%*  .%/   %@   ***&#  .&*  (#&   %%  .%
        &&@    /%  &%,  .#/   %#(#%   /%,  %#&   @##&   @##@   &&   (%*  .&/   %@   &#%##   %%####%%&%#&   &
        &&@   , (  &%,  .%/   %((#%       ,&#&   @##&   @##&   &#####%*        %&     .%#%(    .&(&...&(   &
        &&@   @    &#,  .%/   %((#%   /%,  .%&   @##@   @##&   &%   ##*  .%/   %&   &%##%,.*%#   %&   &../%#
        &&@   @&   &##   &,  *#(##%   *#   ,#&   @##@   @##&   %@   &#*  .%/   %&      &&   &(   %&   %#####
        &&&@@@@@@@@&###&%(#&#(####%@@@@@@&%##&@@@&##&@@@&####&&((%&###@@@@%@@@@%&@@@@@@&##&%(#&%(#&@&@%#####
        @&&@&&&&@&%##((((((#############(((((((################################################(((((#######(
        @@@&&&&&&&#((((((###############((((((((((############(((((#(######################(((((((((######((
        @@@&&&&&&%(((###################((((((((((((((##(#(((((((((((((((((###############((((((((((##((((((
        @@&&&&&&##########################((((((((((((##########(((((((((((((((#########(((((((((((((#(((((#
        &&&&&&&%#############%%%%&&&%######((((((((#(#(((########(((((((((((((((((((((((((((((((((((((((((#%
        &&&&&&&%%%###%%%%%&&&&&&&&&%######%&###(((((################((((((((((((((((((((((((((((((#((((((#%%
        &&&&&&&@&&&&&&&&&&&@@&&&%%#########%&&%##########################((((((((((((((((((((((((#((((((#%%%
        &&&@@&&&@@@@@@@&&&&&%%%##############%&&&&%%#########################((((((((((((((((((###(((((%%%%%
        &&&&&&&&&@@@&%%%########################%&&&&&&&&&&&&&&&&&&&&%%%#######((((((((((((((####((((#%%%%%%
        &&&&&&&&&&&&&%#############################%&&&@&&&&&&&&&&&&&&&&&%%####(((((////((((#####(((%&&%%%&@
        &&&&&&&&&&&&&&%#################################%%%&&@@@@@@@@&&&&&&&%###((((///(((######((%&&&&&@@&&
        &&&&&&&&&&&&&&&&&&#######################################%%&@@@@&&&&&%##((((///((######(%&&&&@@&&%%%
        &&&&&&&&&&&&&&&&&&&&%##%%%%%%%%%##############################%%&&&&&&%##((///((######&&&&@@@&&&&%%%
        &&&&&&&&&&&&&&&&@@@@@@@%##%@@@&%%#############%%###################%%&&%#((//((###%@@&@@@@@&&&&&&&&&
        &&&&&&&&&@@@@@@@@@@@@@(/(%&&@@@@@%#######%%%%%%%%%%%%%%%%%%##########%%%#((/((##&@@&##&@&&&&&&&&&&&&
        &&&&&&&@@@@@@@@@@@@@@%*/(%@@@&#(&@#######%%%%&&@@@@@@@@@@&%%############((/((##%%%###%&&&&&&&&&&&&&&
        &&&&@@@@@@@@@@@@@@@@&%//#&&@@@@@@@######%%%&&%#((%&&@@@@@@@@&%%%########(//(#%%%%%%%&@@@@&&&&&&&&&&&
        &@@@@@@@@@@@@@&&@@@%(%%%#(%@@@@@&%(######%%&%((/#&@@@%%@@@@&@@&%%#%%%##(//#%%%##&%&@@@@@@@@&&&&&&&&&
        @@@@@@@@@@&@@@@@@@@#(##%%%%%&%&%#((#####%%%&#(/(&@@@&%%@@@&#%&&%#####((/(#%%%%%%@@@@@@@@@@@@&&&&&&&&
        @@@@@@&&@@@@@@@@@@@%((####%%###(((######%%%&%(((%&&&@@@@@@#((%%#((//////(####&@@@@@@@@@@@@@@&@&&&&&&
        @@&&%&@@@@@@@@@@@@@&(######((((((##%%%%%%%%%%&%#((%&&&&@%%%&&%((///////(#&@@@@@@@@@@@@@@@@@@@@@&&&&&
        @@@@@&%&&&&&&&&&&&&&######(((((###%%####%%%%%%%%%%%%%%%%%%###((///////#@@@@@@@@@@@@@@@@@@@@@@@@@@@&&
        @@@@@@@@&&&&&&&&&%&&&###((((((####%%########%%%%%%%%%%%%###((((/////#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@&&&@@@@&#((((((#################################((((((%&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@&&&&&&&&%((((((#####################################((%&&&&%&&&&@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@&&&&&&%((((((((((((((((((#########################((##&@&%&&&&&&&&&@@@&&%/&@@@@@@@@@@@@
        @@@@@@@@@@@@@&&&&&%(((((((((////////((((((##%%###############(((&&###%&%%%&&&&&&&&&@&(%@@@@@@@@@@@@@
        @@@@@@@@@@@@@&&&&%#((((((/////***///((((((#%%%%%############(((&@@%#&&%%%%%&&&&&&@@@%&&@@@@@@@@@@@@@
        @@@@@@@@@@@@@@&@%((////////*****///((((((#%%%%%%##########((((@@@@@&@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@
        @@@@@@@@@@@@@&&(((///////*****////(((####%%%%%%%#######(((((#@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&@&@@@@@@
        @@@@@@@@@@@@@@%#(((////////////((###(((((####%%%######(((((%@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&@&@@@
        @@@@@@@@@@@@@@&%####(((((((((###((///////(((###%####((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&@@&
        @@@@@@@@@@&&@@&&&%%%#####%%###(((//////////((##%####((((#&@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@&&&&&&@@@
        @@@@@@@@@&&@@@@@@@@@@%##%%%%%%%%%##(((##%%(/((##%###(((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@
        @@@@@@@@&&@@@@@@@@@&&%##%&&&&&%%%####((((((%#(#%%##((#&&@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        ''')
                elif yes_or_no_bitches == 2:
                    print('You have no game get better at pulling some bitches.')
                elif yes_or_no_bitches == 3 :
                    print('You liar you do have some bitches.')
                elif yes_or_no_bitches == 4 :
                    print ('You dont only have some bitches you also have no dick no balls')
                    time.sleep(1)
                    print('and worst of all you also have no BINOCULUS!')
                elif yes_or_no_bitches == 5 :
                    print('lmao no bitches')
                elif yes_or_no_bitches == 6:
                    print('With your charisma even a rock would say no.')
                bitches = 'done'
                reapear = False
    elif bitches == 'yes':
        print('congratts man you have some bitches')
        print('no need to do this then')
        print('''
        warior 20000 x 20000 pixels
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?!!!7P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&57777~~!B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5??7?J?7?G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#?JYYYJJYYB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#B5Y5GJ7Y5PP5Y5P5G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BGGPYJ5557J5PPP55PPPPB#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#P5GBGYJYB55JJJYYJYPPPGBBBBB###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BY?JPBBGJ?5BP5?!77!!5PGBBBBBBBBBBGGPG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5?JJYBBBGJ?JPGG5?!!7YGBBBBBBBBBBBPYJJJ?JB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?JJJYGBGB5?7JY55PPPGBBBBBBBBBBBBPYJJJJJ??YB@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@5!?JYYY5BBGGPYJ??7?Y5BBBBBBBBBBBBG5YYYYJJ?7?YG@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@Y~~~7J555PB#BBPPP5Y????YPGBBBBBBBGP55Y?!~~~~!!?&@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@#?~~~~~~?GG55GGGPPP5GGP5Y?JJYPGGBBBBGPJ!!!~~~!!!!J&@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@G!~~~~~~7G@@BY5P55YYG5PGPPB5YYJ75P5BBBB?~!!!~~~~~!!Y@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@B^~!!!!!?&@@@&YPGBBGGJYPYBBPPBP5GG?JPJBGP?~!!!!!!!!!!G@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@Y^~~!!!!7#@@@#YPGBBBBBB5PPJPBPPB#GG#5JY7!!!~~~~!!!!!!?&@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@&!^~~!!!!5@@@BYPGBBBBBBB#BGBPYGBBBPJ!~~~~~~~~~~~~~~!!!B@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@G^~7?YPPG##&PJPGBBBBBBBBGGBB##BBGBBY!~~~~~~~~~~~~!~?B@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@!77?B#BB5!!!?PGBBBBBBP5GB####P!~75#BY!~~!!!!~~~~!Y&@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@B7!G#J!!?YP5J5GBGGGBGGBBBBB##BY!~~7G#G7!!!!!!7?YG@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@&7P##Y~~~7BBGGGGPG5J7?GBBBBB###BJ!JB##G55J5G#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@5G#B7~!!5##BBBGPBJ!~~!?P########B###B###B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@&GB?~!7P&@@#BBGPBP5Y7!!!?YB######BGGGB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@#55PB@@@@@BPGG##BBBGPY777J5B#BGPPGG#&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##&&&#BBBBBB#&&&&&&@&#5Y5PGGGGB######B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@&@@&B#BBBBBBB####&&&&&&B#&&&##BBGGB########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@BGGGB##BBB#&###&&&&&###B##&&&&&BPPPPPPBB###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@&##&&@@&#BGG#&&#B#&###&&&&&&#B#&&#BBBBBBBB####&##B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@BBBB#&&&&&###&@@@@@####B#&&##BB########B&@&#&&##&#######&&&@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@#GGB#&&&&&&#######&&B#&&BG#&&#B#&##BBB##&&##&@&#B##BBBBBBBBBB#####&&@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@#GGGB##&&#BBG5YJJYG###&&&@&#B###B#&######&##&#B#######BBBBBB#&&&&&###&@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@&GPGB####BBPY?7!!7?J5P5YY55PPPGG#&&&&&###B&&#&&#BB#####BBB###&@@@@@@&&&&@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@#BGB###BB5?77!~~~!!!!!77??JJJYYY5G#@@@@@@&&#&&&#B#BBB#####B&@@@@@@@@&&&@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@PPGBGBP7!~~~~~~~~~!7???JJYYYYYYJJG@@@@@@@@&&##B#BBBBBBBB#@@@@@@@@@@&&@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@BY5GGGJ~~~~~~~~~^!77??JYY55555P5Y?G@@@@@@@@@PPGBBBBBBBBB#@@@@@@@@@&&@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@GY5GGJ!!~~~~~~:~77??JJYPB##GGGBY?Y@@@@@@@@PYGGGGGGGGBBBB&@@@@@@&&&@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&GPP5777!~~!~^!77??7Y##BB##BBPJ?Y@@@@@@@&JYGBGGGGGG&@&##&&&&&&&@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@&GP577??7?~!777?J?P#GPPPPPGY?7B@@@@@@@@BGGGGGGGGG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@BGGP5J7??7!777?JJYB#GPP5555?P@@@@@@@@@@&PBBBBBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@#B&&GJ77!777JJJY5P555GP?JG@@@@@@@@@@@#5####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PJ???JJJY555Y5G55&@@@@@@@@@@@@GG####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BGP55Y55555GG#@@@@@@@@@@@@@#P#######&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BB######GG&@@@@@@@@@@@@@@BBBB######&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GB#BB###BB#@@@@@@@@@@@@@@@@&&#&&#########&@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&#&#BB#&@@@@@@@@@@@@@@@@@@@@@@&########@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#&&@@@@@@@@@@@@@@@@@@@@@@@@@@
        ''')
        reapear = False
    else:
        if dumb == False:
            print('how did you mess that question up its just yes or no dumb ass')
            dumb = True
        elif dumb == True:
            dumb_precent = 0
            while dumb == True:
                dumb_precent_plus = random.randint(3, 8)
                dumb_precent = dumb_precent + dumb_precent_plus
                print(f'downloading zipbombwarrior.zip {dumb_precent}%')
                time.sleep(1)
                os.system('cls')
                if dumb_precent > 100:
                    dumb_precent = 100
                if dumb_precent == 100:
                    while dumb_precent == 100:
                        print('''
                        warior 20000 x 20000 pixels
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?!!!7P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&57777~~!B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5??7?J?7?G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#?JYYYJJYYB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#B5Y5GJ7Y5PP5Y5P5G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BGGPYJ5557J5PPP55PPPPB#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#P5GBGYJYB55JJJYYJYPPPGBBBBB###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BY?JPBBGJ?5BP5?!77!!5PGBBBBBBBBBBGGPG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5?JJYBBBGJ?JPGG5?!!7YGBBBBBBBBBBBPYJJJ?JB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?JJJYGBGB5?7JY55PPPGBBBBBBBBBBBBPYJJJJJ??YB@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@5!?JYYY5BBGGPYJ??7?Y5BBBBBBBBBBBBG5YYYYJJ?7?YG@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@Y~~~7J555PB#BBPPP5Y????YPGBBBBBBBGP55Y?!~~~~!!?&@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@#?~~~~~~?GG55GGGPPP5GGP5Y?JJYPGGBBBBGPJ!!!~~~!!!!J&@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@G!~~~~~~7G@@BY5P55YYG5PGPPB5YYJ75P5BBBB?~!!!~~~~~!!Y@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@B^~!!!!!?&@@@&YPGBBGGJYPYBBPPBP5GG?JPJBGP?~!!!!!!!!!!G@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@Y^~~!!!!7#@@@#YPGBBBBBB5PPJPBPPB#GG#5JY7!!!~~~~!!!!!!?&@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@&!^~~!!!!5@@@BYPGBBBBBBB#BGBPYGBBBPJ!~~~~~~~~~~~~~~!!!B@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@G^~7?YPPG##&PJPGBBBBBBBBGGBB##BBGBBY!~~~~~~~~~~~~!~?B@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@!77?B#BB5!!!?PGBBBBBBP5GB####P!~75#BY!~~!!!!~~~~!Y&@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@B7!G#J!!?YP5J5GBGGGBGGBBBBB##BY!~~7G#G7!!!!!!7?YG@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@&7P##Y~~~7BBGGGGPG5J7?GBBBBB###BJ!JB##G55J5G#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@5G#B7~!!5##BBBGPBJ!~~!?P########B###B###B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@&GB?~!7P&@@#BBGPBP5Y7!!!?YB######BGGGB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@#55PB@@@@@BPGG##BBBGPY777J5B#BGPPGG#&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##&&&#BBBBBB#&&&&&&@&#5Y5PGGGGB######B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@&@@&B#BBBBBBB####&&&&&&B#&&&##BBGGB########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@BGGGB##BBB#&###&&&&&###B##&&&&&BPPPPPPBB###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@&##&&@@&#BGG#&&#B#&###&&&&&&#B#&&#BBBBBBBB####&##B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@BBBB#&&&&&###&@@@@@####B#&&##BB########B&@&#&&##&#######&&&@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@#GGB#&&&&&&#######&&B#&&BG#&&#B#&##BBB##&&##&@&#B##BBBBBBBBBB#####&&@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@#GGGB##&&#BBG5YJJYG###&&&@&#B###B#&######&##&#B#######BBBBBB#&&&&&###&@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@&GPGB####BBPY?7!!7?J5P5YY55PPPGG#&&&&&###B&&#&&#BB#####BBB###&@@@@@@&&&&@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@#BGB###BB5?77!~~~!!!!!77??JJJYYY5G#@@@@@@&&#&&&#B#BBB#####B&@@@@@@@@&&&@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@PPGBGBP7!~~~~~~~~~!7???JJYYYYYYJJG@@@@@@@@&&##B#BBBBBBBB#@@@@@@@@@@&&@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@BY5GGGJ~~~~~~~~~^!77??JYY55555P5Y?G@@@@@@@@@PPGBBBBBBBBB#@@@@@@@@@&&@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@GY5GGJ!!~~~~~~:~77??JJYPB##GGGBY?Y@@@@@@@@PYGGGGGGGGBBBB&@@@@@@&&&@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@&GPP5777!~~!~^!77??7Y##BB##BBPJ?Y@@@@@@@&JYGBGGGGGG&@&##&&&&&&&@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@&GP577??7?~!777?J?P#GPPPPPGY?7B@@@@@@@@BGGGGGGGGG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@BGGP5J7??7!777?JJYB#GPP5555?P@@@@@@@@@@&PBBBBBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@#B&&GJ77!777JJJY5P555GP?JG@@@@@@@@@@@#5####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PJ???JJJY555Y5G55&@@@@@@@@@@@@GG####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BGP55Y55555GG#@@@@@@@@@@@@@#P#######&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BB######GG&@@@@@@@@@@@@@@BBBB######&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GB#BB###BB#@@@@@@@@@@@@@@@@&&#&&#########&@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&#&#BB#&@@@@@@@@@@@@@@@@@@@@@@&########@@@@@@@@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#&&@@@@@@@@@@@@@@@@@@@@@@@@@@
                        ''')
                        time.sleep(0.2)