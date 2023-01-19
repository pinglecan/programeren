def fiboreeks(nummer: int):
    reeks = [0, 1]

    def fibo2(limiet: int):
        if len(reeks) == limiet:
            return

        reeks.append(reeks[-2] + reeks[-1])
        fibo2(limiet)

    fibo2(100)

    if nummer not in reeks:
        print(f"{nummer} zit niet in reeks")
    elif nummer in reeks:
        print(reeks[0:reeks.index(nummer) + 1])


fiboreeks(82)