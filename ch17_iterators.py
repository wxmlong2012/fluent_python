b = "sentence"
for c in b:
    print(c)

b_it = iter(b)
while True:
    try:
        print(next(b_it))
    except StopIteration:
        del b_it
        break


import itertools
import functools
sample = [5,4,2,8,7,6,3,0,9,1]
sample1 = ["a", "b", "c"]
sample2 = [True, False]
# accumulate works on a iterable, returns a generator
accumulate_gen = itertools.accumulate(sample)
list(accumulate_gen)

# reduce works on a iterable, returns an object
reduced_obj = functools.reduce(lambda x, y: x + y, sample)
print(reduced_obj)

# map applies a func to each item of the iterable, returns a generator
mapped_obj = map(lambda x: 2*x, sample)
mapped_obj

# filter function also create a generator
filtered_obj = filter(lambda x: x > 5, sample)
list(filtered_obj)

# create a cartesian product of the input iterables. (combination for each item from each list)
product_obj = itertools.product(sample, sample1, sample2)
list(product_obj)


type(reduced_obj)
type(accumulate_gen)


from collections.abc import Generator
from typing import Union, NamedTuple

class Result(NamedTuple):
    count: int  # type: ignore
    average: float

class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'

STOP = Sentinel()

SendType = Union[float, Sentinel]

def averager2(verbose: bool=False) -> Generator[None, SendType, Result]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        if verbose:
            print("received", term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

coro_average = averager2(True)
