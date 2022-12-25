import math
import copy


with open("test.txt") as f:
    ls = [x.strip() for x in f.readlines()]


def new(operation, value):
    op = operation.copy()
    for i, x in enumerate(op):
        try:
            op[i] = int(x)
        except:
            if x == "old":
                op[i] = value
    if op[1] == "*":
        return op[0] * op[2]
    elif op[1] == "+":
        return op[0] + op[2]


def monkey_business():
    monkeys = []
    inspections = []

    for l in ls:
        if l == "":
            continue
        elif l[0] == "M":
            monkeys.append({})
            inspections.append(0)
        elif l[0] == "S":
            current_items = l.split(":")[-1].split(",")
            for i, x in enumerate(current_items):
                current_items[i] = int(x.strip())
            monkeys[-1]["Items"] = current_items
        elif l[0] == "O":
            monkeys[-1]["Operation"] = l.split(":")[-1].split(" = ")[-1].split(" ")
        elif l[0] == "T":
            monkeys[-1]["Divisible"] = int(l.split(":")[-1][13:])
        elif l[0] == "I":
            if l[3] == "t":
                monkeys[-1]["True"] = int(l[25:])
            elif l[3] == "f":
                monkeys[-1]["False"] = int(l[25:])

    for iteration in range(20):
        for i, monkey in enumerate(monkeys):
            operation = monkey["Operation"]
            divisible = monkey["Divisible"]
            if_true = monkey["True"]
            if_false = monkey["False"]
            for item in monkey["Items"]:
                inspections[i] += 1
                new_item = math.floor(new(operation, item) / 3)
                if new_item % divisible == 0:
                    monkeys[if_true]["Items"].append(new_item)
                else:
                    monkeys[if_false]["Items"].append(new_item)
            monkeys[i]["Items"] = []

    inspections.sort()
    return inspections[-1] * inspections[-2]


def new(operation, value, divisible):
    op = operation.copy()
    for i, x in enumerate(op):
        try:
            op[i] = int(x)
        except:
            if x == "old":
                op[i] = value
    if op[1] == "*":
        op[0] = op[0] - (math.floor(op[0] / divisible) * divisible) + divisible
        op[2] = op[2] - (math.floor(op[2] / divisible) * divisible) + divisible
        result = op[0] * op[2]
        return result
        # return result - (math.floor(result / divisible) * divisible) + divisible
    elif op[1] == "+":
        return op[0] + op[2]


def worrying_monkey_business():
    monkeys = []
    inspections = []

    for l in ls:
        if l == "":
            continue
        elif l[0] == "M":
            monkeys.append({})
            inspections.append(0)
        elif l[0] == "S":
            current_items = l.split(":")[-1].split(",")
            for i, x in enumerate(current_items):
                current_items[i] = int(x.strip())
            monkeys[-1]["Items"] = current_items
        elif l[0] == "O":
            monkeys[-1]["Operation"] = l.split(":")[-1].split(" = ")[-1].split(" ")
        elif l[0] == "T":
            monkeys[-1]["Divisible"] = int(l.split(":")[-1][13:])
        elif l[0] == "I":
            if l[3] == "t":
                monkeys[-1]["True"] = int(l[25:])
            elif l[3] == "f":
                monkeys[-1]["False"] = int(l[25:])

    for iteration in range(10000):
        if iteration != 0 and iteration % 1000 == 0:
            print(iteration)
            print(inspections)
        for i, monkey in enumerate(monkeys):
            operation = monkey["Operation"]
            divisible = monkey["Divisible"]
            if_true = monkey["True"]
            if_false = monkey["False"]
            for item in monkey["Items"]:
                inspections[i] += 1
                new_item = math.floor(new(operation, item, divisible))
                if new_item % divisible == 0:
                    monkeys[if_true]["Items"].append(new_item)
                else:
                    monkeys[if_false]["Items"].append(new_item)
            monkeys[i]["Items"] = []

    inspections.sort()
    return inspections[-1] * inspections[-2]


print(worrying_monkey_business())
