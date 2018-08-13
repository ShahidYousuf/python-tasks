# Basic things using functions:

# Fibonacci sequence upto n

def fibo(n):
    """ Print a Fibonacci series upto a number n """
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a + b
    print()

def myfunc(param, *args, **kwargs):
    print("Ist param is %s" %param)
    for item in args:
        print(item)
    for key in kwargs:
        print(key, ':', kwargs[key])

if __name__ == '__main__':
    fibo(50)
    mylist = ['a', "something", 23.5, 23]
    mydict = {'a':"apple", "b":"bat"}
    myfunc("Hello there", mylist, mydict)#what if we pass an explicitlist/dict
    print()
    myfunc("New Hello", "a", "list", "of", "items", name="name", age=34) #normal





















