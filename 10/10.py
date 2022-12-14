with open("test.txt") as f:
    ls = [x.strip() for x in f.readlines()]


def increase_tick(signal, tick):
    tick += 1
    if (tick + 20) % 40 == 0:
        print("Tick:", tick, "Signal:", signal, "Tick * Signal:", tick * signal)
    return tick

def signal_strengths():
    tick = 0
    signal = 0
    for l in ls:
        if l[:4] == "noop":
            tick = increase_tick(signal, tick)
        elif l[:4] == "addx":
            tick = increase_tick(signal, tick)
            tick = increase_tick(signal, tick)
            signal += int(l[5:])


signal_strengths()
