res = [[a,b,c] for a in range(1,100) for b in range(1,100) for c in range(1,100) if a**2 + b**2 == c**2]
for item in res:
    print(str(item[0]).center(10) +  str(item[1]).center(10)  + str(item[2]).center(10))
