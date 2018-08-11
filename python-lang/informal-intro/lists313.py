# Python Basic Lists
mylist = [1,4,9,16,25]

print(type(mylist)) # returns the type of mylist here.

print(mylist) # print the whole list

diffs = ['a', "big" , 23, 45.98, 3+7j] # list can contain various types
print(diffs) 
# lists are also sequence types like strings, and
# can be indexed and sliced.

print(mylist[3])
print(mylist[-1])

print(mylist[2:])

print(mylist[:]) # shallow copy of the list

# list also support concatenation
list1 = [2,4,6]
list2 = [1,3,5]

print(list1 + list2)

# Unlike strings, lists are mutable, it is possible to change their content

mylist[0] = 0
print(mylist)
# we can also use list methods

mylist.append(36)
print(mylist)

mylist.append(diffs) # it will now contain a list inside the list
print(mylist)

# slice assignment is also possible
mylist[3:] = [] # empty from index 3
print(mylist)

# to get the length of the list:
print("The length of list is " + str(len(mylist)) + ".")
print("The length of list is ", len(mylist))
print('The length of list is ', len(mylist))



