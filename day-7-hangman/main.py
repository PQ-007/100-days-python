import random
import hangman_words
import hangman_art
lives = 6

chosen_word = random.choice(hangman_words.words)
print(f"The chosen word is {chosen_word}")

placeholder = []
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + " ".join(placeholder))  

game_over = False
correct_guess = False

print(hangman_art.logo)
print("Welcome to the Hangman game!")

while not game_over:
    print(f"You have {lives} lives left.")
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            placeholder[position] = letter
    print(placeholder)
    if guess not in chosen_word:
        print(hangman_art.stages[6-lives])
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. Lives left: {lives}")


        if lives == 0:
            game_over = True
            print("You lose.")
    if "_" not in placeholder:
        game_over = True
        print("You win!")

