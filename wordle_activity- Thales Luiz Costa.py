import random

def wordle():
    words = ['apple', 'grape', 'lemon', 'peach', 'mango']
    word_to_guess = random.choice(words)
    attempts = 6

    print("Welcome to Wordle!")
    print("Guess the word with 5 letters. You have 6 attempts.")

    while attempts > 0:
        guess = input("Digite sua suposição: ")
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        correct_letters = sum(a==b for a, b in zip(word_to_guess, guess))
        print(f"{correct_letters} letters are correct and in the correct position.")
        print("It's a fruit!")

        if guess == word_to_guess:
            print("Congratulations! You guessed the word!")
            return
        else:
            attempts -= 1
            print(f"You have {attempts} attempts to remain.")

    print(f"You couldn't guess the word. The word was {word_to_guess}.")

wordle()