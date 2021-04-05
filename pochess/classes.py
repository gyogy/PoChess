# from random import choice
from random import shuffle


class Card():

    def __init__(self, face, val):
        self.face = str(face)
        self.val = str(val)

    def __repr__(self):
        if self.face != self.val:
            return f'A {self.face} worth a {self.val}'
        else:
            return f'A {self.face}'

    def set_val(self, new_val):
        self.val = str(new_val)


class Player():

    def __init__(self, name):

        self.name = name
        self.chips = 5000
        self.bet = 0
        self.hand = []

# raise (all-in option), call, check, fold


class Dealer():

    def __init__(self, deck):
        self.deck = deck

    def shuffle(self):
        shuffle(self.deck)

    def deal(self, n):
        cards = []

        for i in range(n):
            card = self.deck.pop()
            cards.append(card)

        return cards


'''
class Dealer
get players
W places small blind
B places big blind
W gets 2 cards
B gets 2 cards
betting
2 cards
betting
last card
betting

if one folds, the other wins
'''
