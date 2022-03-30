from dataclasses import dataclass
from datetime import datetime
from os import sep
import time


def sum(*args):
    print(type(args))
    print(args)


sum(1, 2, 3, 4, 5)
sum()

def add(a, b):
    return a + b

print(add(1, 2))

number_pair = (3, 4)
print(add(number_pair[0], number_pair[1]))
print(add(*number_pair))

def print_employee(**kwargs):
    print(type(kwargs))
    print(kwargs)

print_employee(name="John Doe", age=40)

number_pair = {"a": 1, "b": 2}
print(add(**number_pair))

print("aaa")
print("aaa", "bbb", "ccc")
print("aaa", "bbb", "ccc", sep="***")

def substract(a, b):
    return a - b

print(substract(6, 2))

kivon = substract
print(kivon(6, 2))

reverse = lambda s: s[::-1]
print(reverse("korte"))

def print_nevem():
    print("oktato")

def haromszor(ezt_csinald):
    for i in range(3):
        ezt_csinald()

haromszor(print_nevem)
haromszor(lambda :print("hello"))

# Számojátok meg egy hosszú szövegben, hogy melyik szó hányszor szerepel!
# Mintapélda dictionary használatára!

# Dekorátor függvény

def uppercase_decorator(function):
    def wrapper():
        value: str = function()
        return value.upper()
    return wrapper

@uppercase_decorator
def say_my_name():
    return "John Doe"

@uppercase_decorator
def say_hello():
    return "Welcome"

print(say_my_name())
print(say_hello())

def log_decorator(function):
    def wrapper():
        now = datetime.now()
        print(str(now) + " " + function.__name__ + " " + function.__doc__)
        return function()
    return wrapper

@log_decorator
def transfer():
    """Transfer amount between accounts"""
    x = 1 + 2
    print("grrrr")

@log_decorator
def create_client():
    """Create a client"""
    name = "John Doe"

transfer()
create_client()

start = datetime.now()
time.sleep(3)
stop = datetime.now()
diff = stop - start
print(diff)