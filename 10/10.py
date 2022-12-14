with open("test.txt") as f:
    ls = [x.strip() for x in f.readlines()]


def signal_strengths():
    tick = 0
    signal = 0
    for l in ls:
        if l[:4] == "noop":
            tick += 1
        elif l[:4] == "addx":
            tick += 1
            if (tick + 20) % 40 == 0:
                print("Tick:", tick, "Signal:", signal, "Tick * Signal:", tick * signal)
            tick += 1
            if (tick + 20) % 40 == 0:
                print("Tick:", tick, "Signal:", signal, "Tick * Signal:", tick * signal)
            signal += int(l[5:])
        if (tick + 20) % 40 == 0:
            print("Tick:", tick, "Signal:", signal, "Tick * Signal:", tick * signal)


signal_strengths()
