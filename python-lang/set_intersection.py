ec = int(input()) # total students subscribed to english newspaper
e = list(map(int, input().split()))[:ec] # english newspaper student roll numberes
fc = int(input()) # total students subscribed to french newspaper
f = list(map(int, input().split()))[:fc] # french newspaper student roll numbers

e_set = set(e)
f_set = set(f)
print(len(e_set.intersection(f_set)))

