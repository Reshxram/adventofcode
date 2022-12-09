# 07.12.22 No1
def cmd1():
    size = 0
    size_cache = [0]
    command = input()
    while True:
        if command == "":
            break
        if command[0] == "$":
            if command[2:4] == "cd":
                if command[5:] == "..":
                    if size_cache[-1] <= 100000:
                        size += size_cache.pop()
                else:
                    size_cache.append(0)
            elif command[2:4] == "ls":
                while True:
                    command = input()
                    if command[:3] == "dir":
                        pass
                    elif not command == "" and not (command[0] == "$" or command[:2] == "ls"):
                        for x in range(len(size_cache)):
                            size_cache[x] += int(command.split(" ")[0])
                    else:
                        break
                continue
        elif command[:3] == "dir":
            pass

        command = input()
    print(size)
    print(size_cache[0])


# 07.12.22 No2
def cmd2():
    unused = 70000000 - 42476859
    size_needed = 30000000 - unused
    smallest_dir = 7000000000
    size_cache = [0]
    command = input()
    while True:
        if command == "":
            break
        if command[0] == "$":
            if command[2:4] == "cd":
                if command[5:] == "..":
                    new = size_cache[-1] - size_needed
                    old = smallest_dir - size_needed
                    print(size_cache, new)
                    if 0 < new < old:
                        smallest_dir = size_cache[-1]
                    size_cache.pop()
                else:
                    size_cache.append(0)
            elif command[2:4] == "ls":
                while True:
                    command = input()
                    if command[:3] == "dir":
                        pass
                    elif not command == "" and not (command[0] == "$" or command[:2] == "ls"):
                        for x in range(len(size_cache)):
                            size_cache[x] += int(command.split(" ")[0])
                    else:
                        break
                continue
        elif command[:3] == "dir":
            pass

        command = input()
    for x in range(len(size_cache)):
        new = size_cache[-1] - size_needed
        old = smallest_dir - size_needed
        print("Cache: ", size_cache, " New: ",  new, " Old: ", old)
        if 0 < new < old:
            smallest_dir = size_cache[-1]
        size_cache.pop()
    print(smallest_dir)


cmd2()
