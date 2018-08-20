hold = ''
with open('../myfile.txt') as f:
    hold = f.read()
target = hold.split()
target2 = [item.strip('.') for item in target]
result = [(item, target2.count(item.rstrip())) for item in target2]
for (i,c) in result:
    print(i.ljust(15), c)




