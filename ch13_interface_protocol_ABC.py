class Vowel:
    def __getitem__(self, i):
        return "AEIOU"[i]


v = Vowel()
v[0]
for c in v: print(c)


from collections import namedtuple, abc

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):  # <1>
        self._cards[position] = value

    def __delitem__(self, position):  # <2>
        del self._cards[position]

    def insert(self, position, value):  # <3>
        self._cards.insert(position, value)


class FrenchDeck1():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

class FrenchDeck3(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(deck, position, value):  # <1>
        deck._cards[position] = value

    def __delitem__(self, position):  # <2>
        del self._cards[position]

    def insert(self, position, value):  # <3>
        self._cards.insert(position, value)


from random import shuffle
l = list(range(10))
shuffle(l)
l

import abc

class Tombola(abc.ABC):  # <1>

    @abc.abstractmethod
    def load(self, iterable):  # <2>
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):  # <3>
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):  # <4>
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())  # <5>

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:  # <6>
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)  # <7>
        return tuple(items)

import random
class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._item = []
        self.load(items)

    def load(self, items):
        self._item.extend(items)
        self._randomizer.shuffle(self._item)

    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()



class LottoBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # <1>

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))  # <2>
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)  # <3>

    def loaded(self):  # <4>
        return bool(self._balls)

    def inspect(self):  # <5>
        return tuple(self._balls)
