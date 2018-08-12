# Python for statement
# for iterates over the items of any sequence like 
# strings, lists etc.

names = ["alex", "bob", "catherine", "dummy"]
for name in names:
    print(name) # this will print column-wise

for name in names:
    print(name, end=' ') # this will print horizontal

for name in names:
    if name == "catherine":
        print("\nName found: %s" %name)

for name in names:
    print(name, len(name), sep=" ----- ")

# use the range() function for various purposes:

for number in range(1, 11): # prints numbers from 1 to 10
    print(number, end=' ')

print() # dummy print call to output a new line

for even in range(2, 101, 2): # prints from 2 to 100, in steps of 2
    print(even, end= ' ')

print()

for i in range(len(names)):
    print(i, names[i])

print(list(range(2,21,2))) # list of even numbers upto 20

# prime numbers upto 100
for n in range(2, 101):
    for x in range(2, n):
        if n % x ==0:
            break        # breaks out of the innermost enclosing for or while
    else:                # loop's else clause runs when no break occurs
        print(n, end=' ')


