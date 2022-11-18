cant_tell = False

while cant_tell != 'C' or 'C: cant tell':
    print('is she into you?')
    print('A: yes she is')
    print('B:No she isnt')
    print('C: cant tell')
    cant_tell = input('')

    if cant_tell == 'A' or 'A: yes she is':
        print('wrong try again')
    elif cant_tell == 'B' or 'B:No she isnt':
        print('wrojng try again')
if cant_tell == 'C' or 'C: cant tell':
    print('correct you cant tell')