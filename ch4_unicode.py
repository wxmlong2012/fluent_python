cafe = bytes('café', encoding='utf_8')
cafe
cafe[0]
cafe[1]
cafe[2]
cafe[3]
cafe[4]

tab_return_newline = 'abc\nabc\rab\tc\\'

tab_return_newline

tab='tab'
cafe[-1:]
bytes('c', encoding='utf')[0]

bytes("ABC", encoding='utf8')
a = bytes.fromhex('41')
a.decode(encoding='utf8')

bytes.fromhex('F0 9D 84 9E')
a
fp = open("cafe.txt", "w", encoding="utf-8")
fp
fp.write("café")
fp.close()
import os
os.stat('cafe.txt').st_size
fp2 = open('cafe.txt')
fp2
fp2.encoding
fp2.read()


import locale
import sys

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
my_file = open("dummy", "w")

for expression in expressions.split():
    value = eval(expression)
    print(f"{expression:>30} -> {value!r}")


from unicodedata import normalize, name
name("A")
name("é")
name("!")
name("#")
name("@")
name("^")
name("&")
name("~")
name("`")

single_map = str.maketrans("""‚ƒ„ˆ‹‘’“”•–—˜›""",
                           """'f"^<''""---~>""")
single_map
multi_map = str.maketrans({
    '€': 'EUR',
    '…': '...',
    'Æ': 'AE',
    'æ': 'ae',
    'Œ': 'OE',
    'œ': 'oe',
    '™': '(TM)',
    '‰': '<per mille>',
    '†': '**',
    '‡': '***',
})
multi_map.update(single_map)
multi_map

