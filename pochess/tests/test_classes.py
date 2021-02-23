import unittest
from ..classes import Player, Poker_Table

class TestPokerTableClass(unittest.TestCase):

    def setUp(self):

        self.A = Player('Gyogy')
        self.B = Player('Ygoyg')
        self.pt = Poker_Table(self.A, self.B)

    def test_invert_colors_func_when_iswhite_params_are_equal(self):

        self.assertEqual(self.pt.A.is_white, self.pt.B.is_white)

        self.pt.invert_colors()

        self.assertNotEqual(self.pt.A.is_white, self.pt.B.is_white)

    def test_invert_colors_when_iswhite_params_are_different(self):

        self.pt.A.is_white = True
        self.pt.B.is_white = False

        self.pt.invert_colors()

        self.assertFalse(self.pt.A.is_white)
        self.assertTrue(self.pt.B.is_white)

    def test_placing_of_blinds(self):
        pass
