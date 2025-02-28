import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('"The time has come,", the walrus said')

iter(s)
b = 123
iter(b)

try:
    iter(b)
except TypeError:
    print("the test object is not iterable")

