import random
import os
from turtle import clear
import time
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
elif bitches == 'yes':
    print('congratts man you have some bitches')