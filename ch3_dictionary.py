

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
{code: country.upper() for country, code in sorted(country_dial.items())
                                         if code < 70}


test_dict = {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}


# dict.get(key, default) can be used to avoid KeyError
test_dict.get("b", [])
# setdefault(k, default)
test_dict.setdefault("b", []).append((10,20))



