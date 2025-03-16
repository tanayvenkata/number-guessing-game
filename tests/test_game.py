import unittest
from guessing_game.game import NumberGame


class TestNumberGame(unittest.TestCase):
    def setUp(self):
        # Set a fixed random number for testing
        self.game = NumberGame()
        self.game.num = 50

    def test_check_guess_higher(self):
        self.assertEqual(self.game.check_guess(25), "higher")

    def test_check_guess_lower(self):
        self.assertEqual(self.game.check_guess(75), "lower")

    def test_check_guess_correct(self):
        self.assertEqual(self.game.check_guess(50), "correct")


if __name__ == "__main__":
    unittest.main()
