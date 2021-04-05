import unittest
from ..classes import Player, Poker_Table, Card


class TestCardClass(unittest.TestCase):

    def setUp(self):
        self.c1 = Card('p', 'p')
        self.c2 = Card('p', 'p')
        self.c3 = Card('p', 'p')
        self.c4 = Card('B', 'B')
        self.c5 = Card('R', 'R')

        self.deck = [self.c1, self.c2, self.c3, self.c4, self.c5]

        self.gosho = Player('gosho_g')

    def test_val_setting(self):
        self.assertEqual(self.deck[-1].val, 'R')

        self.deck[-1].set_val('p')

        self.assertEqual(self.deck[-1].val, 'p')
        '''
        this doesn't break the next test =>
        setUp is run for each method separately
        '''

    def test_dealing_two_cards(self):
        self.assertEqual(self.gosho.hand, [])

        dealt_card_1 = self.deck.pop()  # pops the [-1] element of deck
        dealt_card_2 = self.deck.pop()

        self.gosho.hand.append(dealt_card_1)
        self.gosho.hand.append(dealt_card_2)
        self.assertEqual(len(self.gosho.hand), 2)

        result1 = self.gosho.hand[0]
        result2 = self.gosho.hand[1]

        self.assertEqual(result1.face, 'R')
        self.assertEqual(result2.face, 'B')

class TestPokerTableClass(unittest.TestCase):

    def setUp(self):
        self.table = Poker_Table(Player('Gyogy'), Player('Ygoyg'))

    def test_invert_colors(self):
        old_white = self.table.white.name
        old_black = self.table.black.name

        self.table.invert_colors()

        self.assertEqual(old_white, self.table.black.name)
        self.assertEqual(old_black, self.table.white.name)
