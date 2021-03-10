import random

DECKSIZE = 52
TYPES = 4
VALUES = 13


class BasicStack:
    def __init__(self):
        self.lst = []

    def insert(self, item):
        self.lst.append(item)

    def top(self):
        return self.lst[self.size() - 1]

    def pop(self):
        if (self.isEmpty()):
            raise IndexError('error stack is empty.')
        return self.lst.pop()

    def size(self):
        return len(self.lst)

    def isEmpty(self):
        return len(self.lst) == 0


class Card():
    valuesDictionary = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                        7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
    typesDictionary = {1: 'Hearts', 2: 'Diamonds', 3: 'Clubs', 4: 'Spades'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self) -> str:
        return str(Card.valuesDictionary[self.value]) + ' of ' + str(Card.typesDictionary[self.type])

    def getValue(self):
        return int(self.value)

    def sameValueAs(self, card):
        return (int(self.value) == int(card.getValue()))

    def getSumValue(self):
        if (int(self.value) >= 10):
            return 10
        elif (int(self.value) == 1):
            return (1, 11)
        else:
            return int(self.value)

    def getType(self):
        return str(Card.typesDictionary[self.type])

    def print(self):
        print(str(Card.valuesDictionary[self.value]) + ' of ' + str(Card.typesDictionary[self.type]))


class Deck:
    def __init__(self, dcount=1):
        self.deckCount = dcount
        self.stack = BasicStack()

    def create(self):
        for _ in range(self.deckCount):
            for i in range(TYPES):
                for j in range(VALUES):
                    card = Card(j + 1, i + 1)
                    self.stack.insert(card)
        # self.stack.insert(Card(1,1))
        # self.stack.insert(Card(1,2))
        # self.stack.insert(Card(1,3))
        # self.stack.insert(Card(1,4))
        # self.stack.insert(Card(2,1))
        # self.stack.insert(Card(2,2))
        # self.stack.insert(Card(2,3))

    def draw(self):
        if (self.stack.isEmpty()):
            raise NameError('Deck is empty:')
        return self.stack.pop()

    def peek(self):
        return self.stack.top()

    def shuffle(self):
        temp = []
        for i in range(1, DECKSIZE + 1):
            temp.append(self.draw())
        for i in range(1, DECKSIZE + 1):
            self.stack.insert(temp.pop(random.randrange(0, len(temp))))