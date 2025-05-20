import random

def hangman_game():
    word_list = ["python", "banana", "giraffe", "hangman", "elephant", "challenge"]
    chosen_word = random.choice(word_list)
    masked_word = ['*' for _ in chosen_word]
    guessed_letters = set()
    attempts = 0
    max_attempts = 6
    body_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

    print("🎯 Welcome to Hangman!")
    print("Guess the word:", ''.join(masked_word))

    while attempts < max_attempts and '*' in masked_word:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print("✅ Good guess!")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    masked_word[i] = guess
        else:
            print(f"❌ Wrong guess! Adding body part: {body_parts[attempts]}")
            attempts += 1

        print("Word:", ''.join(masked_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Body parts: {attempts}/{max_attempts}\n")

    if '*' not in masked_word:
        print(f"🎉 Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f"💀 Game Over! The word was: {chosen_word}")

# Run the game
hangman_game()
