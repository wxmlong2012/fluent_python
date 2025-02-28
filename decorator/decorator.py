from functools import cache
from dataclasses import dataclass
from functools import wraps
import json

@cache
def add(x, y):
    print("adding", x, "and", y)
    return (x + y)

add(3,2)
add(3,5)

# slow
def lucas(n):
    """Get the nth Lucas number."""
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n-1) + lucas(n-2)

# fast, when there are recursive calculation
@cache
def lucas(n):
    """Get the nth Lucas number."""
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n-1) + lucas(n-2)

@dataclass
class Point:
    x: float
    y: float
    z: float


a = Point(10,12,15)
b = Point(10,12,15)
a == b

def square(n): return n**2
def cube(n): return n**3
operations = [square, cube]

list(map(bool, ["word", 0, "", 2]))
[*map(bool, ["word", 0, "", 2])]


def greet_me(name="friend"):
    def greet():
        print(f"hello {name}")
    return greet

greet_me()

def count_calls(func):
    """A decorator that counts the number of times a function is called."""
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} times")
        return func(*args, **kwargs)
    wrapper.call_count = 0

    return wrapper

@count_calls
def say_hello():
    """print hello world"""
    print("hello world")

say_hello.__doc__




def count_calls(func):
    """A decorator that counts the number of times a function is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} times.")
        return func(*args, **kwargs)

    wrapper.call_count = 0  # Initialize the call count
    return wrapper

@count_calls
def say_hello():
    """print hello world"""
    print("hello world")

say_hello.__doc__


def jsonify(func):
    """jsonify the output of the function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        return json.dumps(results)

    return wrapper

@jsonify
def get_data():
    return {"name": "Peter", "age": 45}

get_data()