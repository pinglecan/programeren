is_kaas_geel = (input('Is de kaas geel?  '))

if is_kaas_geel == ('ja')or ('Ja'):
    gaten_in_kaas = (input('Zitten er gaten in?  '))
    if gaten_in_kaas == ('ja')or ('Ja'): 
        is_de_kaas_duur =(input('Is de kaas belagelijk duur?  '))
        if is_de_kaas_duur == ('ja')or ('Ja'):
            print('emmenthaler')
        else:
            print('leerdammer')
    else:
        harde_kaas = input('Is de kaas hard als steen?  ')
        if harde_kaas == ('ja')or ('Ja'):
            print('Parmigiano Reggiano')
        else :
            print('Goudse Kaas')
else :
    blauwe_kaas = input('heeft de kaas blauwe schimmel?  ')
    if blauwe_kaas == ('ja') or ('Ja'):
        kaas_korst_blauw=input('Heeft de kaas een korst?  ')
        if kaas_korst_blauw==('ja') or ('Ja'):
            print('blue de rochbaron')
        else:
            print('foume dambert')
    else:
        kaas_korst_geel = input('heeft de kaas een korst?  ')
        if kaas_korst_geel == ('ja') or ('Ja'):
            print('camebert')
        else:
            print ("mozzarella")