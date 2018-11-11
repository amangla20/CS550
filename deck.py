# https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
from card import Card
import random
class Deck:
	def __init__(self):
		self.cards = []
		for i in range(1,14):
			a = random.randrange(1,14)
			self.cards.append(Card(a, "Hearts"))
			self.cards.append(Card(a, "Diamonds"))
			self.cards.append(Card(a, "Clubs"))
			self.cards.append(Card(a, "Spades"))
	def __str__(self):
		result = ""
		for i in self.cards
			str(Card)

dealer_deck = Deck()
print(str(dealer_deck))

