# 06.12.22 No1 + No2
def find_marker(length):
    message = input()
    for x in range(len(message)):
        if len(set(message[x:x+length])) == length:
            print(x+length)
            break


find_marker(4)
