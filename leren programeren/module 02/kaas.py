is_kaas_geel = input('Is de kaas geel?  ').lower()

if is_kaas_geel == 'ja':
    gaten_in_kaas = input('Zitten er gaten in?  ').lower()
    if gaten_in_kaas == 'ja': 
        is_de_kaas_duur =input('Is de kaas belagelijk duur?  ').lower()
        if is_de_kaas_duur == 'ja':
            print('emmenthaler')
        else:
            print('leerdammer')
    else:
        harde_kaas = input('Is de kaas hard als steen?  ').lower()
        if harde_kaas == 'ja':
            print('Parmigiano Reggiano')
        else :
            print('Goudse Kaas')
elif is_kaas_geel == "nee" :
    blauwe_kaas = input('heeft de kaas blauwe schimmel?  ').lower()
    if blauwe_kaas == 'ja':
        kaas_korst_blauw=input('Heeft de kaas een korst?  ').lower()
        if kaas_korst_blauw=='ja':
            print('blue de rochbaron')
        else:
            print('foume dambert')
    else:
        kaas_korst_geel = input('heeft de kaas een korst?  ').lower()
        if kaas_korst_geel == 'ja':
            stinkt = input('Stinkt de kaas?  ').lower()
            if stinkt== 'ja':
                print('camebert')
            elif stinkt == 'nee':
                print('brie')
        else:
            print ("mozzarella")