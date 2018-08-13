# Python Dictionaries Basic
# dicts are indexed by keys, which can be any immutable type: strings, numbers
# dicts are key: value pairs.

# creating a dictionary
data = {'name':"Some Name", "age": 23, "salary": 2300.34}
print(data)
print(data['name'])
print(data['age'])

data['job'] = "programmer"
print(data)

# to return a list of all the keys

print(list(data))
print()
for key in list(data): # keys in insertion order
    print(key, " -------- ", data[key])
print()
for key in sorted(data): # keys in sorted order
    print(key, " -------- ", data[key])

# dictionary comprehension
# following works because keys are unique
data2 = {key:value for key in ["name", "age", "profession"] for value in ["Some", 23, "Prof"] }
# We can use zip() function instead
data3 = {key:value for key, value in zip(["name","age","prof"],["some",34,"prog"])}

print("data2")
print(data2)
print("data3")
print(data3)

print()
# special dictionary looping
for key, value in data.items():
    print(key, " : ", value)


