import random
import os


def pick_word():
    """Pick random word to guess from words.txt, return letters"""
    with open('words.txt'):
        words_list = open("words.txt").read().split()
    word_letters = list(random.choice(words_list))
    empty_letters = ["_"] * len(word_letters)
    return word_letters, empty_letters

def update_picture(guess, lives_remaining):
    """Update game picture"""
    # Clear the console
    os.system('cls')
    print(f"Lives remaining: {lives_remaining}")
    for letter in guess:
        print(f"{letter} ", end=" ")
    print()
    print()
    print()

def letter_guess(word, guess):
    """Take letter from player, if word contain letter - change guess list"""
    guess_letter = ""
    index = 0
    success = False
    while not guess_letter:
        try:
            guess_letter = input("\nGuess a letter: ").lower()
        except ValueError:
            print("Sorry, that's not a letter")

    for letter in word:
        if letter.lower() == guess_letter:
            guess[index] = letter
            success = True
        index += 1
    return success

def game_flow(word, guess, lives):
    while True:
        if guess == word:
            update_picture(guess, lives)
            print(f"\nYou won! The word was '{"".join(word)}'")
            break
        elif lives <= 0:
            print("\nYou lose :(")
            print(f"The word was '{"".join(word)}'")
            break
        else:
            update_picture(guess, lives)
            if not letter_guess(word, guess):
                lives -= 1




if __name__ == '__main__':
    #Initiallization
    start_words = pick_word()
    word_letters_list = start_words[0]
    guess_letters_list = start_words[1]
    start_lives = 10

    #Start game
    game_flow(word_letters_list, guess_letters_list, start_lives)

