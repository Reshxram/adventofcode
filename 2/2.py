# 02.12.22 No1
def cheat():
    inputs = []
    inp = ""
    while inp != "exit":
        inp = input()
        if inp != "exit":
            inputs.append(inp)

    points = 0
    for x in inputs:
        if x[-1] == "X":
            points += 1
            if x[0] == "C":
                points += 6
            elif x[0] == "A":
                points += 3
        elif x[-1] == "Y":
            points += 2
            if x[0] == "A":
                points += 6
            elif x[0] == "B":
                points += 3
        elif x[-1] == "Z":
            points += 3
            if x[0] == "B":
                points += 6
            elif x[0] == "C":
                points += 3
    print(points)


# 02.12.22 No2
def cheat2():
    inputs = []
    inp = ""
    while inp != "exit":
        inp = input()
        if inp != "exit":
            inputs.append(inp)

    points = 0
    for x in inputs:
        if x[-1] == "X":  # loose
            if x[0] == "A":  # Rock
                points += 3
            elif x[0] == "B":  # Paper
                points += 1
            elif x[0] == "C":  # Scissors
                points += 2
        elif x[-1] == "Y":  # draw
            points += 3
            if x[0] == "A":  # Rock
                points += 1
            elif x[0] == "B":  # Paper
                points += 2
            elif x[0] == "C":  # Scissors
                points += 3
        elif x[-1] == "Z":  # win
            points += 6
            if x[0] == "A":  # Rock
                points += 2
            elif x[0] == "B":  # Paper
                points += 3
            elif x[0] == "C":  # Scissors
                points += 1
    print(points)


cheat2()
