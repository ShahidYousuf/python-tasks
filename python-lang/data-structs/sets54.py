# Python Set Basics
# sets are unordered collection with no duplicate elements.
# sets support set operations like union, intersection etc

# to create empty set use set(), not {}, the later creates an empty dictionary

names = {"apple", "orange", "apple", "pear", "banana"}
print(type(names))
print(names) # duplicates removed

# membership test

print("apple" in names) # return True
x = set("apple") # set containing the letters of word apple

print(x)
# set operations
print()
a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
print("Letter in a but not in b")
print(a-b)
print("Union of a and b")
print(a | b)
print("Intersection of a and b")
print(a & b)
print("Letter in a or b, but not both")
print(a ^ b)

# set comprehensions
some_set = {x for x in 'apple' if x not in 'like'}
print(some_set)


