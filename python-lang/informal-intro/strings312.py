# Basic Strings in Python
a = 'spam eggs'
b = 'doesn\'t' # use \' to escape the single quote
c = "doesn't" # use double quote as well
d = '"Yes," they said'
print(a,"\n",b,"\n",c,"\n",d,"\n")

print("C:\some\name\other") # something wrong here
print(r"C:\some\name\ohter") # Python raw string, using 'r' before the quote

foo = "python "
print(10 * foo) # string concatenation in action

# strings can be indexed

print(foo[0])
print(foo[3])
print(foo[6])

print(foo[-1])
print(foo[-2])
print(foo[-6])

# string slicing

print(foo[0:2])
print(foo[2:5])
print(foo[:2])
print(foo[2:])
print(foo[:2] + foo[2:])

# strings in python are immutable, can't be changed in-place
# foo[0] = 'J' # will give error, uncomment to see
print(foo)

# we can however can a new string:
bar = 'J' + foo[1:]
print(bar)

# get length of string
print(len(foo)) # Yes, it will give 7, because we added an extra at first


