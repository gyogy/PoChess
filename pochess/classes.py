from random import choice

deck = 16 * 'p' + 8 * 'N' + 8 * 'B' + 8 * 'R' + 4 * 'Q'
DECK = list(deck)

class Player():

    def __init__(self, name):

        self.name = name
        self.is_white = None
        self.chips = 5000
        self.bet = 0
        self.hand = []

# raise (all-in option), call, check, fold


class Poker_Table():

    def __init__(self, A, B):

        self.A = A
        self.B = B
        self.phase = 0
        self.small_blind = 100
        self.big_blind = self.small_blind * 2
        self.pot = 0

    def deal(self, n, player):

        for i in range(n):
            self.player.hand.append(DECK.pop())

    def invert_colors(self):

        if self.A.is_white is not None:
            self.A.is_white = not self.A.is_white
            self.B.is_white = not self.B.is_white

        else:
            self.A.is_white = choice([True, False])
            self.B.is_white = not self.A.is_white

    def place_blinds(self):

        if self.A.is_white:
            pass
        else:
            pass

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
