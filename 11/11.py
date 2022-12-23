import math


with open("test.txt") as f:
    ls = [x.strip() for x in f.readlines()]


def new(operation, value):
    for i, x in enumerate(operation):
        try:
            operation[i] = int(x)
        except:
            if x == "old":
                operation[i] = value
    if operation[1] == "*":
        return operation[0] * operation[2]
    elif operation[1] == "+":
        return operation[0] + operation[2]

def monkey_business():
    monkeys = []
    inspections = []
    cache = []

    for l in ls:
        if l == "":
            continue
        elif l[0] == "M":
            monkeys.append([int(l[7:-1]), {}])
            inspections.append(0)
            cache.append([int(l[7:-1]), []])
        elif l[0] == "S":
            current_items = l.split(":")[-1].split(",")
            for i, x in enumerate(current_items):
                current_items[i] = int(x.strip())
            monkeys[-1][-1]["Items"] = current_items
        elif l[0] == "O":
            monkeys[-1][-1]["Operation"] = l.split(":")[-1].split(" = ")[-1].split(" ")
        elif l[0] == "T":
            monkeys[-1][-1]["Divisable"] = int(l.split(":")[-1][13:])
        elif l[0] == "I":
            if l[3] == "t":
                monkeys[-1][-1]["True"] = int(l[25:])
            elif l[3] == "f":
                monkeys[-1][-1]["False"] = int(l[25:])

    for iteration in range(1):
        for monkey in monkeys:
            operation = monkey[-1]["Operation"]
            divisable = monkey[-1]["Divisable"]
            if_true = monkey[-1]["True"]
            if_false = monkey[-1]["False"]
            for item in monkey[-1]["Items"]:
                inspections[monkey[0]] += 1
                new_item = math.floor(new(monkey[-1]["Operation"], item) / 3)
                if new_item % divisable == 0:
                    cache[if_true][-1].append(new_item)
                else:
                    cache[if_false][-1].append(new_item)
        for i in range(len(monkeys)):
            monkeys[i][-1]["Items"] = cache[i][-1]

    print(monkeys)
    inspections.sort()
    return inspections[-1] * inspections[-2]


print(monkey_business())