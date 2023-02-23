def aantal_poten(giraffen : int, zebras: int, struisvogels :int):
    poten_giraffen = giraffen * 4
    poten_zebras = zebras * 4
    poten_struisvogels = struisvogels * 2
    poten_totaal = poten_struisvogels + poten_giraffen + poten_zebras

    return poten_giraffen , poten_zebras , poten_struisvogels, poten_totaal



giraff = int(input("hoeveel giraffen zijn er?  "))
zebra = int(input("hoeveel zebras zijn er?  "))
struisvogel = int(input("hoeveel struisvogels zijn er"))

print(aantal_poten(giraff,zebra,struisvogel))