import random

def hangman_game():
    # List of possible words
    word_list = ['python', 'hangman', 'random', 'challenge', 'game']
    
    # Randomly select a word
    word_to_guess = random.choice(word_list)
    word_length = len(word_to_guess)
    guessed_word = ['_'] * word_length
    guessed_letters = set()
    attempts_remaining = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    
    # Game loop
    while attempts_remaining > 0:
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts Remaining: {attempts_remaining}")
        
        guess = input("Enter a letter: ").lower()
        
        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter has been guessed before
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess in word_to_guess:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts_remaining -= 1
        
        # Check if the player has guessed the word
        if ''.join(guessed_word) == word_to_guess:
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nGame Over! The word was: {word_to_guess}")

# Run the game
hangman_game()
