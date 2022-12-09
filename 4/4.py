# 04.12.22 No1
def full_overlaps():
    inp = ""
    overlaps = 0
    while inp != "exit":
        inp = input()
        if inp == "exit":
            break
        inp = inp.split(",")
        inp[0] = inp[0].split("-")
        inp[1] = inp[1].split("-")
        if int(inp[0][0]) >= int(inp[1][0]) and int(inp[0][-1]) <= int(inp[1][-1]):
            overlaps += 1
        elif int(inp[0][0]) <= int(inp[1][0]) and int(inp[0][-1]) >= int(inp[1][-1]):
            overlaps += 1
    print(overlaps)


# 04.12.22 No2
def overlaps():
    inp = ""
    overlaps = 0
    while inp != "exit":
        inp = input()
        if inp == "exit":
            break
        inp = inp.split(",")
        inp[0] = inp[0].split("-")
        inp[1] = inp[1].split("-")
        x1, y1 = int(inp[0][0]), int(inp[0][1])
        x2, y2 = int(inp[1][0]), int(inp[1][1])
        if x2 <= x1 <= y2:
            overlaps += 1
        elif x2 <= y1 <= y2:
            overlaps += 1
        elif x1 <= x2 <= y1:
            overlaps += 1
        elif x1 <= y2 <= y1:
            overlaps += 1

    print(overlaps)


overlaps()
