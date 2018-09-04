n = int(input()) # number of elements in the set
s = set(map(int, input().split())) # set
c = int(input()) # number of commads to operate

for i in range(c):
    command = input().split()
    try:
        if command[0] == "pop":
            s.pop()
        if command[0] == "remove":
            s.remove(int(command[1]))
        if command[0] == "discard":
            s.discard(int(command[1]))
    except (KeyError):
        continue
print(sum(s))
