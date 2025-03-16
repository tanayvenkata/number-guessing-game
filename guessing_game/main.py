from guessing_game.game import NumberGame


def is_valid_input(user_input, min_num, max_num):
    """
    Check if user input is valid (either 'q' or an integer within range)
    """
    if user_input.lower() == "q":
        return True

    try:
        num = int(user_input)
        return min_num <= num <= max_num

    except ValueError:
        return False


def main():
    game = NumberGame()
    quit = "q"

    while True:
        user_response = input(
            f"Guess int between {game.min_num} and {game.max_num} or type 'q' to quit: "
        )

        if is_valid_input(user_response, game.min_num, game.max_num):
            if user_response == quit:
                break

            guess = int(user_response)
            result = game.check_guess(guess)

            if result == "correct":
                print(f"Congratulations! You guessed the number {game.num} correctly!")
                break
            if result == "higher":
                print(f"{guess} is too low! Try a higher number.")
            else:  # result == "lower"
                print(f"{guess} is too high! Try a lower number.")

        else:
            print(
                f"Input must be int between {game.min_num} and {game.max_num} inclusive."
            )

    print("The game has concluded. Thank you for playing")


if __name__ == "__main__":
    main()
