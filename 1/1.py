# 01.12.22 No1
def most_calories():
    cals = []
    inp = ""
    while inp != "exit":
        inp = input()
        if inp != "exit":
            cals.append(inp)
    sums = []
    index = 0
    ram = 0
    for x in cals:
        if x == "":
            sums.append(ram)
            ram = 0
            index += 1
            continue
        ram += int(x)

    print(max(sums))


# 01.12.22 No2
def top_3_cals():
    cals = []
    inp = ""
    while inp != "exit":
        inp = input()
        if inp != "exit":
            cals.append(inp)
    sums = []
    index = 0
    ram = 0
    for x in cals:
        if x == "":
            sums.append(ram)
            ram = 0
            index += 1
            continue
        ram += int(x)

    top_3 = 0
    for x in range(3):
        top_3 += max(sums)
        sums.remove(max(sums))

    print(top_3)


top_3_cals()
