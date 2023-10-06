import random

def wordle_game(word_list, max_attempts=5):
    # Choose a random word from the list
    chosen_word = random.choice(word_list)
    print("Welcome to Wordle! Guess the word.")
    print("This time the word that you will try to guess is a Fruit.")
    print("It's a fruit with 5 letters. Can you guess it?")
    
    attempts = 0
    while attempts < max_attempts:
        guess = input("Enter your guess: ")
        if len(guess) != len(chosen_word):
            print("Please enter a word of length", len(chosen_word))
            continue

        # Check each letter in the guess
        hint = ['_' for _ in range(len(guess))]
        for i in range(len(guess)):
            if guess[i] == chosen_word[i]:
                hint[i] = guess[i].upper()  # Correct letter and position
            elif guess[i] in chosen_word:
                hint[i] = guess[i]  # Correct letter, wrong position

        print("Hint:", ' '.join(hint))

        # Check if the player has won
        if guess == chosen_word:
            print("Congratulations, you've guessed the word!")
            break

        attempts += 1
        print("You have", max_attempts - attempts, "attempts left.")

    if attempts == max_attempts:
        print("Sorry, you've reached the maximum number of attempts. The word was", chosen_word)

# List of words for the game
words = ['apple', 'grape', 'lemon', 'peach', 'mango', 'plum', 'guava', 'melon', 'prune']
wordle_game(words)