import unittest
from ..classes import Player, Poker_Table

class TestPokerTableClass(unittest.TestCase):

    def setUp(self):
        self.table = Poker_Table(Player('Gyogy'), Player('Ygoyg'))

    def test_invert_colors(self):
        old_white = self.table.white.name
        old_black = self.table.black.name

        self.table.invert_colors()

        self.assertEqual(old_white, self.table.black.name)
        self.assertEqual(old_black, self.table.white.name)
