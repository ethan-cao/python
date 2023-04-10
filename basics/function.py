import time
from package1.module1 import greet

def f1(x, y, z = 1):
    # indention indicates the code scope, could 2 or 4 space
    return x + y + z

print(f1(1,2))

# param x is int
# reutrn type is boolean
def f2(x: int) -> int:
    if x > 0:
        print("input is positive")
        return 1
    elif x < 0:
        print("input is negative")
        return -1
    else:
        print("input is zero")
        return 0

print(f2(23))


def f3(x):
    return True if x > 0 else False

print(f3(23))


def outer_func():
    x = 1
    def inner_func():
        # use nonlocal when a nested function needs to access and modify a variable in the enclosing function's scope
        nonlocal x
        x += 1
        print(x)
    inner_func()

outer_func()  # Output: 2

    
# closure
def f5(x):
    def increase():
        # access x from outer scope
        return x + 1 
    return increase

increase = f5(5)
print(increase())  # 6


greet()


# lambda is anonymous function that can be defined inline and used as a single expression
doubleNumber = lambda num: num * 2
getSum = lambda a, b : a + b

print(doubleNumber(4))


# decorateor is a function that takes a function as parameter,
# returns a new function that may modify the behavior of the original function
def logtime(func):
    def wrapper():
        start_time = time.time()        
        val = func()
        end_time = time.time()
        print(f"took {end_time - start_time} seconds to execute")
        return val
    
    return wrapper

@logtime
def hello():
    print("hello")

hello()