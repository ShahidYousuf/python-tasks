# Python Lists
names = ["apple", "orange", "car", "house", "box"]

# List Methods
print(names) # original list

# list.appen(x) : Add item to the end of the list

names.append("bus")
print(names)

# list.extend(iterable) : extend by appending an iterable

names.extend(["new apple", "new orange", "new car"])
print(names)
iterab = "hello"
names.extend(iterab) # individual item of iterable added

# list.insert(i, x): Insert item at a given position

names.insert(1, "mango")
print(names)

# list.remove(x) : remove the first item with value x

names.remove('h')
print(names)
for item in "ello":
    names.remove(item)
print(names)

names.remove("new orange")
names.remove("new apple")
names.remove("new car")
try:
    names.remove("something") # try to remove something not there
except (ValueError):
    print("\nCannot remove something not in the list\n")

print(names)
# list.pop([i]) : remove item at a given index i, and return the item
# index i here is optional, if not given, last item is removed from the list

item = names.pop(1) # removes the second item in the list
print("Pop item: ", item)
print(names) 


# list.index(x, [start], [end]) : returns index of the value x, first
# occurrence. start and end can be given to search in a slice, but still
# absolute index is given
index = names.index("box")
print("Index of box: ", index)
for item in names:
    print(names.index(item), ":", item)

# list.count(x): returns number of times x appears in the list
names.append("box")
print()
for item in names:
    print(names.count(item), ":", item)

names.remove("box") # removes the first occurrence of box
print(names)
count = 0
# check how many items start with letter 'b'
for item in names:
    if item.startswith("b"):
        count = count +1
print(count)

# list.sort(key=None, reverse=False) : sort the items of the list

names.sort()
print(names)

# Now sort based on the item lenght
names.sort(key=len)
print(names)

# sort in reverse order now
names.sort(key=len, reverse=True)
print(names)

# list.reverse() : reverse the items of the list in place

names.reverse()
print(names)

# list.copy() : Returns a shallow copy of the list

names_copy = names.copy()
print(names_copy)

