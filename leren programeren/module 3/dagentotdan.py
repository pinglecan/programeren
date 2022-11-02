dagen = ['maandag','dinsdag','woendsdag','donderdag','vrijdag','zaterdag','zondag']
totdan = input('geef een dag  ')

while totdan != dagen[0]:
    print(dagen[0])
    dagen.pop(0)