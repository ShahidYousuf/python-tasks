# This is our function decorator
# It returns a wrapper for the original function
def our_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        return_value = func(*args, **kwargs)
        print("After calling " + func.__name__)
        return return_value
    return wrapper

# This is our original function
def foo(x):
    print("Hi, foo has been called with " + str(x))

# Calling original function without decorator
print("We call foo before decoration")
foo("Hello")

# Calling original function with decorator
print("We call foo after decoration")
foo = our_decorator(foo)
foo("Hello")


# But usually, and the correct way, we use decorators like following
print("="*50)
@our_decorator
def bar(x):
    print("Hi, bar has been called with " + str(x))
bar("Hello")

print("="*50)
# We can defince decorators as classes as well, like following:
class mydecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Decorating ", self.func.__name__)
        res = self.func(*args, **kwargs)
        return res

@mydecorator
def foobar(x):
    print("Hi, foobar has been called with " + str(x))

foobar("Hello")
