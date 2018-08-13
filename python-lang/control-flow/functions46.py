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

def concat(*args, sep="/"): # default value for sep argument
    # print(type(args)) # this will be of type tuple
    return sep.join(args) # we can also return the calculation

def myfunc2(param1: str, param2: str = "param2", *args: tuple ) -> str:
    print("Annotations: ", myfunc2.__annotations__)
    print("myfunc2.__annotations__:", type(myfunc2.__annotations__))
    print("type(param1):", type(param1))
    print("type(param2):", type(param2))
    print("type(args): ", type(args))



if __name__ == '__main__':
    fibo(50)
    mytup = ('a', "something", 23.5, 23)
    mydict = {'a':"apple", "b":"bat"}
    myfunc("Hello there", mytup, mydict)#what if we pass an explicit tup/dict
    print()
    myfunc("New Hello", "a", "list", "of", "items", name="name", age=34) #normal
    print()
    myfunc("New Hello", *mytup, **mydict) # unpacking at action
    print()
    print(concat("earth", "mars", "jupiter"))
    print(concat("earth", "mars", "jupiter", sep="#"))
    print()
    myfunc2("param1")


    




















