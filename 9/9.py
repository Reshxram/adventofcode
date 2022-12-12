with open("input.txt") as f:
    ls = [x.strip() for x in f.readlines()]


def print_grid(coords, height, width):
    for y in range(height):
        for x in range(width):
            if [x, y] in coords:
                print(coords.index([x, y]), end=" ")
            else:
                print("-", end=" ")
        print()


def tail_visits():
    visited = [(0, 0)]
    head = [0, 0]
    tail = [0, 0]
    for l in ls:
        steps = int(l[2:])
        for x in range(steps):
            match l[0]:
                case "L":  # Left
                    head[0] -= 1
                    if abs(tail[0] - head[0]) > 1:
                        if abs(tail[1] - head[1]) > 0:
                            tail[1] += head[1] - tail[1]
                        tail[0] -= 1
                        visited.append(tuple(tail))
                case "R":  # Right
                    head[0] += 1
                    if abs(tail[0] - head[0]) > 1:
                        if abs(tail[1] - head[1]) > 0:
                            tail[1] += head[1] - tail[1]
                        tail[0] += 1
                        visited.append(tuple(tail))
                case "U":  # Up
                    head[1] -= 1
                    if abs(tail[1] - head[1]) > 1:
                        if abs(tail[0] - head[0]) > 0:
                            tail[0] += head[0] - tail[0]
                        tail[1] -= 1
                        visited.append(tuple(tail))
                case "D":  # Down
                    head[1] += 1
                    if abs(tail[1] - head[1]) > 1:
                        if abs(tail[0] - head[0]) > 0:
                            tail[0] += head[0] - tail[0]
                        tail[1] += 1
                        visited.append(tuple(tail))
    visited = list(set(visited))
    visited = list(visited)
    visited.sort()
    print(visited)
    return len(visited)


def k_tail_visits():
    visited = [(10, 10)]
    knots = []
    for x in range(10):
        knots.append([10, 10])

    for l in ls:
        steps = int(l[2:])
        for x in range(steps):
            match l[0]:
                case "L":  # Left
                    knots[0][0] -= 1
                case "R":  # Right
                    knots[0][0] += 1
                case "U":  # Up
                    knots[0][1] -= 1
                case "D":  # Down
                    knots[0][1] += 1

            for y in range(len(knots) - 1):
                if abs(knots[y + 1][0] - knots[y][0]) > 0 and abs(knots[y + 1][1] - knots[y][1]) > 1 or abs(
                        knots[y + 1][0] - knots[y][0]) > 1 and abs(knots[y + 1][1] - knots[y][1]) > 0:
                    knots[y + 1][0] += (-1 if knots[y][0] - knots[y + 1][0] < 0 else 1)
                    knots[y + 1][1] += (-1 if knots[y][1] - knots[y + 1][1] < 0 else 1)
                elif abs(knots[y + 1][0] - knots[y][0]) > 1:
                    knots[y + 1][0] += (-1 if knots[y][0] - knots[y + 1][0] < 0 else 1)
                elif abs(knots[y + 1][1] - knots[y][1]) > 1:
                    knots[y + 1][1] += (-1 if knots[y][1] - knots[y + 1][1] < 0 else 1)
            visited.append(tuple(knots[9]))
        print("Arg: ", l, ", ", "Step: ", x)
        print("Knots: ", knots)
        print_grid(knots)
        print("---")

    visited = list(set(visited))
    visited = list(visited)
    visited.sort()
    print(visited)
    return len(visited)


print(k_tail_visits())
