#!/usr/local/bin/python3


from enum import Enum



class Card:
	suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	ranks = {
		2: 'Two',
		3: 'Three',
		4: 'Four',
		5: 'Five',
		6: 'Six',
		7: 'Seven',
		8: 'Eight',
		9: 'Nine',
		10: 'Ten',
		11: 'Jack',
		12: 'Queen',
		13: 'King',
		14: 'Ace'
	}

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '['+Card.suits[self.suit]+','+Card.ranks[self.rank]+']'


class Deck:

	def __init__(self):
		self.cards = []
		for s in range(4):
			for r in Card.ranks.keys():
				self.cards.append(Card(s,r))


class Hand:
	