import numpy as np


with open("test.txt") as f:
    ls = [x.strip() for x in f.readlines()]


trees = []
for l in ls:
    l = list(l)
    trees.append(list(map(int, l)))
    #  np.append(trees, np.array(list(map(int, l.split()))))


def visable_trees(trees):
    trees = np.array(trees)
    visable = []

    for x in range(len(trees)):
        prev_highest = [-1, -1, -1, -1]
        for y in range(len(trees[0])):
            if prev_highest[0] < trees[x, y]:  # left -> right
                # print("H: ", trees[x, y], " at: ", [x, y], " higher than ", prev_highest[0])
                prev_highest[0] = trees[x, y]
                visable.append((x, y))
            if prev_highest[1] < trees[x, len(trees[0]) - y - 1]:  # right -> left
                # print("H: ", trees[x, len(trees[0]) - y - 1], " at: ", [x, len(trees[0]) - y - 1], " higher than ",
                # prev_highest[1])
                prev_highest[1] = trees[x, len(trees[0]) - y - 1]
                visable.append((x, len(trees[0]) - y - 1))
            if prev_highest[2] < trees[y, x]:  # top -> bottom
                # print("H: ", trees[y, x], " at: ", [y, x], " higher than ", prev_highest[2])
                prev_highest[2] = trees[y, x]
                visable.append((y, x))
            if prev_highest[3] < trees[len(trees[0]) - y - 1, x]:  # bottom -> top
                # print("H: ", trees[len(trees[0]) - y - 1, x], " at: ", [len(trees[0]) - y - 1, x], " higher than ",
                # prev_highest[3])
                prev_highest[3] = trees[len(trees[0]) - y - 1, x]
                visable.append((len(trees[0]) - y - 1, x))

    my_set = list(set(visable))
    my_list = list(my_set)
    my_list.sort()
    return len(my_list)


# print(visable_trees(trees))


def scenic_highscore(trees):
    trees = np.array(trees)
    visable = []
    highscore = 0

    for x in range(len(trees)):
        for y in range(len(trees[0])):
            score = [0, 0, 0, 0]
            print("-------------------------------------")
            print("Checking: ", [x, y])
            i, j = x, y
            while i > 0:
                if i == x:
                    i -= 1
                    continue
                if trees[i, j] >= trees[x, y]:
                    break
                score[0] += 1
                i -= 1
            while i < len(trees[0]):
                if i == x:
                    i += 1
                    continue
                if trees[i, j] >= trees[x, y]:
                    break
                score[1] += 1
                i += 1
            while j > 0:
                if i == x:
                    i -= 1
                    continue
                if trees[i, j] >= trees[x, y]:
                    break
                score[2] += 1
                i -= 1
            while j < len(trees[0]):
                if i == x:
                    i += 1
                    continue
                if trees[i, j] >= trees[x, y]:
                    break
                score[3] += 1
                i += 1

            print("Score: ", score)
            product = np.prod(score)
            print("Prod: ", product)
            if product > highscore:
                highscore = product


    my_set = list(set(visable))
    my_list = list(my_set)
    my_list.sort()
    return highscore


print(scenic_highscore(trees))