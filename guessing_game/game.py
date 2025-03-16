import random


class NumberGame:
    def __init__(self, min_num=0, max_num=100):
        """Initialize a game with a random number between min_num and max_num"""
        self.min_num = min_num
        self.max_num = max_num
        self.num = random.randint(min_num, max_num)

    def check_guess(self, guess):
        """
        Check if guess is correct, too high, or too low
        Returns: "correct," "higher," or "lower"
        """
        CORRECT = "correct"
        LOWER = "lower"
        HIGHER = "higher"

        if guess == self.num:
            return CORRECT
        if guess > self.num:
            return LOWER
        return HIGHER
