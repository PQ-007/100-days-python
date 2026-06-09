from random import randint

logo = r"""                                                                                                                                        

  _  _            _                ___                _              ___                
 | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
 |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
                                                            |___/                       
"""

def set_difficulty():
    """Ask the player to choose a difficulty and return attempts."""
    while True:
        choice = input("Choose a difficulty level ('easy' or 'hard'): ").lower()
        if choice == 'easy':
            return 10
        if choice == 'hard':
            return 5
        print("Please enter 'easy' or 'hard'.")


def get_guess():
    """Prompt the player for a numeric guess and validate input."""
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")


def play_game():
    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    print(f"You have {attempts} attempts to guess the number.")
    number = randint(1, 100)

    while attempts > 0:
        guess = get_guess()
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Congratulations! You've guessed the number {number} correctly!")
            return

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")

    print(f"Game over! The number was {number}. Better luck next time!")





if __name__ == '__main__':
    play_game()
