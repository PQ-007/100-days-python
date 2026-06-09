from random import choice
from art import logo, vs
from game_data import data


def evaluate_guess(guess, account_a, account_b):
    """Evaluate the player's guess and return True if correct, False otherwise."""
    if account_a['follower_count'] > account_b['follower_count']:
        return guess == 'A'
    else:
        account_a = account_b
        return guess == 'B'
def format_account(account):
    """Format the account data into a printable string."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def play_game():
    score = 0
    game_should_continue = True
    account_a = choice(data)
    data.remove(account_a)

    print(logo)
    while game_should_continue:
        if len(data) == 0:
            print("Congratulations! You've compared all accounts!")
            break
        account_b = choice(data)
        data.remove(account_b)
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_correct = evaluate_guess(guess, account_a, account_b)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

if __name__ == "__main__":
    while input("Do you want to play? Type 'y' or 'n': ").lower() == 'y':
        play_game()