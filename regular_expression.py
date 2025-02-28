import re

# put angles around all numbers
# catch them as a group and then replace the group.
text = "Turn the 35 boxes into the 100 boxes."
re.sub(r"([0-9]+)", r"<\1>", text)
re.sub(r'(\d+)', r'<\1>', text)


# capture group
# which text will the patter match
pattern = r"the (.*)er they (.*), the \1er we \2"
text1 = "the faster they ran, the faster we ran"
text2 = "the faster they ran, the faster we ate"

re.match(pattern, text1)
re.match(pattern, text2)
matched = re.match(pattern, text1)
print(matched)
type(matched)
# entire matched string
matched.group(0)
# each group being captured
matched.group(1)
matched.group(2)
# start and end position for matched string
matched.start()
matched.end()

# not capture group  (?: pattern ).
# "some" just match no capture, "cats" match and capture
pattern = r"(?:some|a few) (people|cats) like some \1"
text1 = "some cats like some cats"
text2 = "some cats like some dogs"
re.match(pattern, text1)
re.match(pattern, text2)
# entire matched string
matched = re.match(pattern, text1)
matched.group(0)
# each group being captured
matched.group(1)
matched.group(2)


# The (?=pattern) is a part of a regular expression known as a "positive lookahead" assertion.
# It is used to match a specific pattern only if it is followed by another specific pattern,
# without including the second pattern in the match.

# The (?!pattern) is a part of a regular expression known as a "negative lookahead" assertion.
# It is used to match a specific pattern only if it is NOT followed by another specific pattern.

text = "I like apple pie, but not apple juice or apple sauce."

# apple not followed by juice
pattern1 = r"apple(?! juice)"
# apple followed by pie
pattern2 = r"apple(?= pie)"

# should find two
re.findall(pattern1, text)
# should find one
re.findall(pattern2, text)

# match telephon number ###-###-####
text = "Here is my telephone cellphone 984-209-8878, this is also my number: 9842098878 "
pattern1 = r"\d{3}-\d{3}-\d{4}"
pattern2 = r"\d{3}-\d{3}-\d{4}|\d{10}"
re.findall(pattern1, text)
re.findall(pattern2, text)

# match the first occurrence from the beginning, not in the middle
re.match(pattern2, text)
# match the first occurrence any where in the string
matched = re.search(pattern2, text)
matched.group()

# match gruppy or grappies
# findall only find the groups, not the whole text?
text = "it is gruppy or gruppies"
pattern = r"grupp(y|ies)"
pattern1 = r"grupp(?:y|ies)"
pattern2 = r"gruppy"
re.findall(pattern, text)
re.search(pattern, text)
re.search(pattern, text).group()

re.findall(pattern1, text)
re.search(pattern1, text)

re.findall(pattern2, text)

# In the first pattern, we match the entire date as a whole.
# In the second pattern, we capture the day, month, and year separately.
# You can see the difference between matching and capturing in the output.

text = "Today's date is 14-10-2023."

# Match the entire date pattern
pattern = r"\d{2}-\d{2}-\d{4}"
match = re.search(pattern, text)

if match:
    matched_text = match.group()
    print("Matched:", matched_text)
else:
    print("No match")

# Capture the day, month, and year individually
pattern = r"(\d{2})-(\d{2})-(\d{4})"
match = re.search(pattern, text)

if match:
    day = match.group(1)
    month = match.group(2)
    year = match.group(3)
    print("Captured:")
    print("Day:", day)
    print("Month:", month)
    print("Year:", year)
else:
    print("No match")


text = "My phone number is 123-456-7890" #, and my other number is 987-654-3210."
pattern = r"is (\d{3})-(\d{3})-(\d{4})"
matches = re.findall(pattern, text)
print(matches)


import nltk
text = 'That U.S.A. poster-print costs $12.40...'
# note here ?: match but not capture the group
pattern = r"""(?x)                 # set flag to allow verbose regexps
              (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
              |\w+(?:-w+)*           # words with optional internal hyphens
              |\$?\d+(?:\.\d+)?%?    # currency and percentages, e.g. $12.40, 82%
              |\.\.\.              # ellipsis
              |[][.,;?():-_]       # these are separate tokens; includes ], [ . , ( ) etc
"""
tokens = nltk.regexp_tokenize(text, pattern)
print(tokens)



