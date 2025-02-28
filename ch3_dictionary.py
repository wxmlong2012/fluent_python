
# dictionary comprehension
dial_codes = [
        (880, 'Bangladesh'),
        (55,  'Brazil'),
        (86,  'China'),
        (91,  'India'),
        (62,  'Indonesia'),
        (81,  'Japan'),
        (234, 'Nigeria'),
        (92,  'Pakistan'),
        (7,   'Russia'),
        (1,   'United States'),
]
country_dial = {country: dial for dial, country in dial_codes}
print(country_dial)

# Sorting country_dial by name, reversing the pairs again, uppercasing values, and filtering items with code < 70
country_dial1 = {code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
print(country_dial1)

d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 | d2



# unpacking mapping
# ** can be used more than once in argument
def dump(**kwargs):
    return kwargs
dump(**{"x": 1, "y": 2}, z=3, **{"a": 4, "b": 5})

def test_fun(a=1, b=2, c=3, d=4):
    print(a, b, c, d)

test_arg2 = {"a": 10, "b": 20}
test_arg2 = {"d": 40}
test_fun(**test_arg, **test_arg2)

# ** can be used more than once inside a dict liberal
test_dict = {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}

fruits = {'apple': [1,2], 'banana': [3,4]}
# lookup key one
cherry = fruits.get('cherry', [])
cherry.append(5)
# lookup key two
fruits['cherry'] = cherry
fruits

# if use setdfault, we only to lookup key once
fruits.setdefault('plum', []).append(6)
fruits
fruits.setdefault('banana', []).append(7)
fruits

# Merging Mappings with |
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 | d2
d1 |= d2
d1



# dict.get(key, default) can be used to avoid KeyError
test_dict.get("b", [])
# setdefault(k, default)
test_dict.setdefault("b", []).append((10,20))




# dict views
a = {"a": 1, "b": 2}
a.items()
a.values()
a.keys()

# values is a view of the dict value, a projection. It will be updated if the original dict change
values = a.values()
values
a["c"] = 3
values


# set to remove duplicates
l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
set(l)

# If you want to remove duplicates but also preserve the order of the first occurrence of each item, you can now use a plain dict to do it
list(dict.fromkeys(l).keys())

a = {i for i in range(10)}
b = {i for i in range(5, 15)}
# intersection
a & b
c = a & b
# union
a | b
# difference
a - b
# symmetric difference
a ^ b

a-b
b-a

c < b
c > b


# a dict_keys view can always be used as a set, because every key is hashable—by definition.
d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)
s = {"a", "b", "c"}
d1.keys() & d2.keys()
d1.keys() & s



>>># example of defaultdict
>>>from collections import defaultdict
>>>fruits = defaultdict(list)
>>># updating the dict without checking the keys whether is exist or not
>>>fruits['apple'].append(1)
>>>fruits['banana'].append(7)
>>>fruits


class StrKeyDict(dict):
    # StrKeyDict inherits from dict
    def __missing__(self, key):
        # check whether key is already a str,  If it is, and it's missing, raise KeyError
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        # The get method delegates to __getitem__ by using the self[key] notation; that
        # gives the opportunity for our __missing__ to act.
        try:
            return self[key]
        except KeyError:
            return default

# OrderedDict
from collections import OrderedDict
d1 = OrderedDict(a=1, b=2, c=3, d=4)
d1.popitem()
d1.popitem(last=False)

>>> d1 = dict(a=1, b=3)
>>> d2 = dict(a=2, b=4, c=6)
>>> from collections import ChainMap
>>> chain = ChainMap(d1, d2)
>>> chain['a']
1
>>> chain['c']
6

>>> chain['c'] = -1
>>> d1
{'a': 1, 'b': 3, 'c': -1}
>>> d2
{'a': 2, 'b': 4, 'c': 6}

>>> ct = collections.Counter('abracadabra')
>>> ct
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
>>> ct.update('aaaaazzz')
>>> ct
Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
>>> ct.most_common(3)
[('a', 10), ('z', 3), ('b', 2)]


>>> d = dict(a=10, b=20, c=30)
>>> values = d.values()
>>> values
dict_values([10, 20, 30])
>>> len(values)
3
>>> list(values)
[10, 20, 30]
>>> reversed(values)
<dict_reversevalueiterator object at 0x10e9e7310>
>>> values[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_values' object is not subscriptable

>>> d['z'] = 99
>>> d
{'a': 10, 'b': 20, 'c': 30, 'z': 99}
>>> values
dict_values([10, 20, 30, 99])

# define an attribute outside of __init__
class MyClass:
	def __init__(self):
		self.a_val = 10
	def start(self, number):
		self.b_val = 10 * number
	def get_b(self):
		return self.b_val

# an improved way to define the attributes inside __init__
class MyClass:
	def __init__(self):
		self.a_val = 10
		self.b_val = None
	def start(self, number):
		self.b_val = 10 * number
	def get_b(self):
		return self.b_val

>>> from types import MappingProxyType
>>> d = {1: 'A'}
>>> d_proxy = MappingProxyType(d)
>>> d_proxy
mappingproxy({1: 'A'})
>>> d_proxy[1]
'A'
>>> d_proxy[2] = 'x'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'mappingproxy' object does not support item assignment

l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
set(l)
list(set(l))

dict.fromkeys(l)
dict.fromkeys(l).keys()
list(dict.fromkeys(l).keys())

s1 = set([1,2,3,4,3,2])
s2 = set([3,4,5,6,4])
s1
s2
# s1 | s2 returns their union
s1 | s2
# s1 & s2 returns their intersection
s1 & s2
# s1 ^ s2 returns their symmetric difference
s1 ^ s2
# s1 - s2 returns the difference
s1 - s2
s2 - s1


s1 = {1, 2, 3}
s1 = {}  # empty dict
s1 = set()  #empty set
frozen_s1 = frozenset(range(10)) # frozenset has no special syntax to represent


>>>{chr(i) for i in range(32, 40)}
{'&', '"', "'", '$', '#', '!', '%', ' '}


s3 = {3,4,5,6,7}
>>> d1 = dict(a=1, b=2, c=3, d=4)
>>> d2 = dict(b=20, d=40, e=50)
>>> d1.keys() & d2.keys()
{'b', 'd'}

>>> s = {'a', 'e', 'i'}
>>> d1.keys() & s
{'a'}
>>> d1.keys() | s
{'a', 'c', 'b', 'd', 'i', 'e'}


{1,2} < s1
{1,2,3,4} <= s1
s1 < s2
>>>{1,2} < s1
True
>>>{1,2,3,4} <= s1
True
>>>s1 < s2
False
>>>{1,2,3,4,5} > s1
True



>>>found = len(set(needles) & set(haystack))

# another way: haystack can be any iterable types
>>>found = len(set(needles).intersection(haystack))

l1 = ["b", "a", "c", "a", "b", "c"]