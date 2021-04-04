# from random import choice

deck = 16 * 'p' + 8 * 'N' + 8 * 'B' + 8 * 'R' + 4 * 'Q'
DECK = list(deck)


class Card():

    def __init__(self, face, val):
        self.face = face
        self.val = val


class Player():

    def __init__(self, name):

        self.name = name
        self.chips = 5000
        self.bet = 0
        self.hand = []

# raise (all-in option), call, check, fold


class Poker_Table():

    def __init__(self, player1, player2):

        self.white = player1
        self.black = player2
        self.phase = 0
        self.small_blind = 100
        self.big_blind = self.small_blind * 2
        self.pot = 0

    def deal(self, n, player):
        pass

    def invert_colors(self):

        players = (self.white, self.black)
        self.white = players[1]
        self.black = players[0]

    def place_blinds(self):
        self.white.chips -= self.small_blind
        self.black.chips -= self.big_blind
        self.pot += self.small_blind + self.big_blind

        self.small_blind += 50
        self.big_blind = self.small_blind * 2


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
