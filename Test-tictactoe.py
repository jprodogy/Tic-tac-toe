import unittest
from is_even import *

class TestIsEven(unittest.TestCase):
  def test_small_evens(self):
    self.assertEqual(False, game_winner([[],[],[]]))
    self.assertEqual(True, is_even(2))
    self.assertEqual(True, is_even(0))

  def test_small_odds(self):
    self.assertEqual(False, is_even(7))
    self.assertEqual(False, is_even(1))
    self.assertEqual(False, is_even(3))
