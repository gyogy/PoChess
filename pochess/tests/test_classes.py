import unittest
from ..classes import Player, Dealer, Card

# @classmethod
# def setUpClass(cls):
#     pass

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
        setUp is run separately for each method
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


class TestDealerClass(unittest.TestCase):
    def setUp(self):
        deck = 16 * 'p' + 8 * 'N' + 8 * 'B' + 8 * 'R' + 4 * 'Q'
        DECK = [Card(letter, letter) for letter in deck]

        self.dealer = Dealer(DECK)
        self.tosho = Player('tOsHeCa')

    def test_shuffle(self):
        self.dealer.shuffle()

        default = 16 * 'p'
        result = ''

        for i in range(16):
            result += self.dealer.deck[i].face

        self.assertNotEqual(default, result)

    def test_deal_two(self):
        self.tosho.hand += self.dealer.deal(2)
        self.assertEqual(len(self.tosho.hand), 2)

#    def test_deal_more_cards_than_in_deck(self):
#        self.assertEqual(44, len(self.dealer.deck))
#        self.tosho.hand += self.dealer.deal(45)
