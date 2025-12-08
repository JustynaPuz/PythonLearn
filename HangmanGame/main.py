import random

from hangman_art import stages, logo
from hangman_words import word_list

lives = len(stages) - 1

chosen_word = random.choice(word_list)

placeholder = "_" * len(chosen_word)
guessed_letters = []
print(logo)

while lives > 0 and '_' in placeholder:
    print("Word to guess: " + placeholder)
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)

    counter = 0
    guessed_right = False

    for letter in chosen_word:
        if letter == guess:
            placeholder = placeholder[:counter] + guess + placeholder[counter + 1:]
            guessed_right = True
        counter += 1

    if not guessed_right:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    print(stages[lives])

if lives == 0:
    print("Game Over!")
    print(f"The word was: {chosen_word}")
else:
    print("You won!")
    print(f"The word was: {chosen_word}")
