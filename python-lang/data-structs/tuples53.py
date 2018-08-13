# Python Tuples and Sequences
# create a basic tuple
t = 12, 13, 14, 15, "hello", ["apple","bat","cat"]
print(t)

# nesting a tuple
t1 = t , 'something'
print(t1)

# indexing
t1[0]
print(t1[0])

print(t1[0][2])

# tuples are immutable
try:
    t[1] = 33
except (TypeError):
    print("TypeError, Tuples are immutable")

# but tuples can contain mutables which can be changed in place
t[5][2]="cattle"
print(t)

# slicing
print(t[2:5])
t_copy = t[:]
print(t_copy)

# iteration (of sequences)
for item in t:
    print(item)

# unpacking
print(*t)

first, second, third, *rest = t
print(first, second, third)
print(rest)
# unpack rest
print(*rest)
print()
first, *middle, last = t
print(first, last)
print(*middle)



