import matplotlib.pyplot as plt

from random import randint


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.id = self.value + self.suit*13

    def __repr__(self):
        suit = Card.SuitsAsStrings[self.suit]
        value = Card.valuesAsStrings[self.value]
        return '%s %s' % (suit, value)
        # return str(self.id)

Card.SuitsAsStrings = ['♠️', '♥️', '♦️', '♣️']
Card.valuesAsStrings = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
Card.Suits = [0,1,2,3]
Card.values = [0,1,2,3,4,5,6,7,8,9,10,11,12]


class Deck:
    cards = []

    def __init__(self):
        for suit in Card.Suits:
            for value in Card.values:
                self.cards.append(Card(value, suit))

    def print(self):
        numPerLine, i = 13, 0
        for card in self.cards:
            print(card, end=' ')
            i += 1
            if i % numPerLine == 0:
                print()
        print()

    def id(self):
        idString = ''
        for card in self.cards:
            idString += str(card.id)
        return idString

    def shuffle(self):
        for i in range(len(self.cards)-1):
            j = randint(i+1, len(self.cards)-1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]



deck = Deck()
deck.shuffle()
deck.print()
print('==========')
deck.shuffle()
deck.print()
print('==========')
deck.shuffle()
deck.print()
print('==========')
deck.shuffle()
deck.print()
print('==========')