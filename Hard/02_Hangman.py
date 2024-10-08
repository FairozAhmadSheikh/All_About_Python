import random

# Tuple of Possible results
words = ("goat", "cat", "dog", "cow", "sheep", "lamb", "lion")

# Hangman Art (6)
hangman_art = {
    0: ("    ",
        "    ",
        "    "),
    1: (" O  ",
        "    ",
        "    "),
    2: (" O  ",
        " |  ",
        "    "),
    3: (" O  ",
        "/|  ",
        "    "),
    4: (" O  ",
        "/|\\",
        "    "),
    5: (" O  ",
        "/|\\",
        "/   "),
    6: (" O  ",
        "/|\\",
        "/ \\"),
}

# Display Hangman Art
def display_man(wrong_guesses):
    print("***********************")
    for value in hangman_art[wrong_guesses]:
        print(value)
    print("***********************")

# Hint Display
def display_hint(hint):
    print(" ".join(hint))

# Display answer
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = list("_") * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter A Letter: ").lower()

        # Check whether guess is an alphabet and a single character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Entry. Type a Single Character.")
            continue
        
        # Check if already guessed the letter
        if guess in guessed_letters:
            print(f"{guess} has already been guessed.")
            continue

        # Add the guessed letter to the set
        guessed_letters.add(guess)

        # Check Guess in answer 
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose!")
            is_running = False

if __name__ == "__main__":
    main()
