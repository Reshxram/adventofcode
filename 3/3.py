import numpy as np


def get_prio(char):
    if char == char.lower():
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26


# 03.12.22 No1
def check_bags():
    inp = ""
    priority = 0
    while inp != "exit":
        inp = input()
        bag1, bag2 = inp[:len(inp) // 2], inp[len(inp) // 2:]
        for x in bag1:
            for y in bag2:
                if x == y:
                    priority += get_prio(x)
                    break
            else:
                continue
            break
    print(priority)


# 03.12.22 No2
def check_3bags():
    inputs = []
    inp = ""
    while inp != "exit":
        inp = input()
        if inp != "exit":
            inputs.append(inp)
    inputs = np.array_split(np.array(inputs), len(inputs) / 3)

    priority = 0
    all_chars = {}
    for group in inputs:
        chars = {}
        for bag in group:
            bag = "".join(set(bag))
            for x in bag:
                if x not in dict.keys(chars):
                    chars[x] = 1
                else:
                    chars[x] += 1
        priority += get_prio(max(chars, key=chars.get))
    print(priority)


check_3bags()
