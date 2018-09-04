import time
from functools import wraps
# we want to find the time taken by a function to execute.
# Let's make a decorator
def duration_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Execution time for {0} {1:.3f}".format(func.__name__,end-start))
        return result
    return wrapper
def count_decorator(func):
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        # enclosing scope variable is read-only, but we can
        # use the nonlocal keyword to modify them
        nonlocal count
        count = count + 1
        result = func(*args, **kwargs)
        print(func.__name__ + " called " + str(count) + " times")
        return result
    return wrapper

@duration_decorator
@count_decorator
def foo(message):
    print("Function foo called with " + str(message))
    
@duration_decorator
def bar(count):
    for i in range(count):
        print("hahaha ", end=' ')
        
@count_decorator
@duration_decorator
def foobar(x):
    print("Foobar called " + str(x))
    
foo("Shahid")
foo("Yousuf")
bar(100)
foobar("hello")
foobar("tick")
foobar("tock")




