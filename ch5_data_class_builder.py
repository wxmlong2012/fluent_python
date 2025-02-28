import dataclasses
from inspect import get_annotations
from typing import get_type_hints
from collections import namedtuple
from typing import NamedTuple
import json
from dataclasses import dataclass, asdict, field


City = namedtuple('City', 'name country population coordinate')
tokyo = City('tokyo', 'JP', 36.12, (35, 139))
tokyo
tokyo.population
tokyo.name
tokyo[2]

tokyo._asdict()
tokyo._fields

Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi', 'IN', 21.9, Coordinate(28.6, 77.2))
delhi = City._make(delhi_data)
delhi
delhi._asdict()


json.dumps(delhi._asdict())


# Typed Named Tuple
class Coordinate(NamedTuple):
    lat: float  # every field must be annotated
    lon: float
    references: str = 'WGS84'

# a plain class
# a is not an attribute, b and c are
class DemoPlainClass:
    a: int
    b: float=1.1
    c = 'spam'
pn = DemoPlainClass()
pn.a
pn.b
pn.c
pn.b = 2.3
pn.c = "aaa"


# a and b are instance attributes,
#  c is an old class attribute,
# a and b are read only after assignment
class DemoNTClass(NamedTuple):
    a: int
    b: float=1.1
    c = 'spam'

DemoNTClass.__annotations__
DemoNTClass.a
DemoNTClass.b
DemoNTClass.c

nt = DemoNTClass(a=1, b=2.3)
nt.a
nt.b
nt.c

nt.a = 2

nt._asdict()

## dataclass
@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'

DemoDataClass.__annotations__
DemoDataClass.__doc__
DemoDataClass.a  # the attribute will only exist in an instance, not in a class
DemoDataClass.b
DemoDataClass.c

dc = DemoDataClass(9)
dc.a
dc.b
dc.c

dc.a = 8
dc.b = 2.3
dc.c = 'aa'
dc.z = "whatever"
dc.z

# only a and b are class attributes and  bound to the instance,
# c and z are not
asdict(dc)

# Mutable default is not allowed
@dataclass()
class ClubMember:
    name: str
    guests: list = []

# Use default_factory instead
@dataclass()
class MemberClub:
    name: str = "Mike"
    book: int = 20
    guests: list[str] = field(default_factory=list)

MemberClub.__annotations__
MemberClub.__doc__
mc = MemberClub("Sam", 1, ["a", "b"])
mc.__annotations__
asdict(mc)
mc