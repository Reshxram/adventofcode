# 05.12.22 No1
def rearange():
    stacks = [[] for x in range(9)]
    while True:
        inp = input()
        if inp[0] == " ":
            break
        for x in range(9):
            if inp[:3] != "   ":
                stacks[x].append(inp[:3])
            inp = inp[4:]
    for x in range(9):
        stacks[x].reverse()
    input()
    while True:
        inp = input()
        if inp == "":
            break
        inp = inp.split(" ")
        inp = list(map(int, inp[1::2]))
        for x in range(inp[0]):
            stacks[inp[2]-1].append(stacks[inp[1]-1].pop())
    result = ""
    for x in range(9):
        result += stacks[x][-1][1]
    print(result)


# 05.12.22 No2
def rearange_multiple():
    stacks = []
    for x in range(9):
        stacks.append([])
    while True:
        inp = input()
        if inp[0] == " ":
            break
        for x in range(9):
            if inp[:3] != "   ":
                stacks[x].append(inp[:3])
            inp = inp[4:]
    for x in range(9):
        stacks[x].reverse()
    input()
    while True:
        inp = input()
        if inp == "":
            break
        inp = inp.split(" ")
        inp = list(map(int, inp[1::2]))
        crane = []
        for x in range(inp[0]):
            crane.append(stacks[inp[1]-1].pop())
        crane.reverse()
        for x in range(len(crane)):
            stacks[inp[2]-1].append(crane[x])
    result = ""
    for x in range(9):
        result += stacks[x][-1][1]
    print(result)


rearange_multiple()
