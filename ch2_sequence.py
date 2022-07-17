x = "ABC"
codes = [ord(x) for x in x]

[last := ord(c) for c in x]
last
c
symbols = "$CFGD"
[c for c in map(ord, symbols)]
list(filter(lambda x: x > 67, map(ord, symbols)))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                            for size in sizes]
tshirts

# ---------- Generator expression ---------------
# Generator expression saves memory, it won't need to create the whole list
# Here the number is created one by one to feed the tuple, the whole list is not created
symbol_tuple = tuple(ord(symbol) for symbol in symbols)
import array
array.array("I", (ord(symbol) for symbol in symbols))

# same as above here the whole list is never created, the generator expression feeds the for loop producing one item at a time.
for tshirt in (f"{c} {s}" for c in colors for s in sizes):
    print(tshirt)

# --------- unpack tuple -------------
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# The % formatting operator understands tuples and treats each item as a separate field.
for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in traveler_ids:
    print(country)

hash("1234")
hash("12345")
t1 = (1,2,3)
t2 = (4,5,6)
t1*=2

l1 = [1,2,3]
l1.reverse()

tshirts.sort(key = lambda x: x[0])
tshirts.sort(key = lambda x: x[1])
tshirts

# Using * to Grab Excess Items
a, b, *rest = range(5)
a, *rest, c, d = range(10)

# Unpacking with * in Function Calls and Sequence Literals
def func(a, b, c, d, *rest):
    return a, b, c, d, rest


func(*[1,2], 3, *range(4,7))

# * can be used to define list, tuple, set
*range(3), 4
*[2,3], 4
[*range(3), 4]
{*range(3), 4, *(5,6,7)}

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    main()


print(f'{2000:*20} | {"latitude":>9} | {"longtitude":>9}')

a = 0.12355476
b = 12.23459
print(f"percent = {a:.2%}, two digit = {b:.2f}")
print(f"percent = {a:.2%}, two digit = {b:4.3f}")
print(f"percent = {a:.2%}, two digit = {'b'!s}")


invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""

line_items = invoice.split("\n")[2:]
unit_price = slice(40, 52)
description = slice(6, 40)
for item in line_items:
    print(item[description], item[unit_price])

l = list(range(10))
l[2:5] = [10,20,30,40]
l

my_list = [[]] * 3
my_list

t = (1, 2, [30, 40])
t[2] += [50, 60]
t







