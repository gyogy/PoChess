import unittest
from ..classes import Player, Poker_Table

class TestPokerTableClass(unittest.TestCase):

    def setUp(self):

        self.A = Player('Gyogy')
        self.B = Player('Ygoyg')
        self.pt = Poker_Table(self.A, self.B)

    def test_invert_colors_func_when_is_white_is_none(self):

        color_A = self.pt.A.is_white
        self.assertIsNone(color_A)

        self.pt.invert_colors()
        color_A = self.pt.A.is_white
        color_B = self.pt.B.is_white

        self.assertIsNotNone(color_A)
        self.assertNotEqual(color_A, color_B)

    def test_invert_colors_when_is_white_has_a_previous_value(self):

        self.pt.A.is_white = True
        self.pt.B.is_white = False

        self.pt.invert_colors()

        self.assertFalse(self.pt.A.is_white)
        self.assertTrue(self.pt.B.is_white)

    def test_placing_of_blinds(self):
        pass
