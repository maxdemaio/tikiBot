##############################
""" Hangman """
##############################

import sys
from random import randint
from hangmanPics import pics

# Fetch random word from the English dictionary
def randomWord():
    with open("words_alpha.txt") as word_file:
        englishWordList = word_file.read().split()
        randomNum = randint(0, len(englishWordList) - 1)
        randomWord = englishWordList[randomNum]
    return randomWord

def main(secretWord):
    secretWord = secretWord.lower()
    errors = 0
    correct = 0
    corrGuesses = ["_" for i in range(len(secretWord))]
    incorrGuesses = []

    while errors < 6:
        # Print the hangman picture based on amount of errors
        print(pics[errors])

        # Print the correct guesses list
        print("Secret Word:", end=" ")
        for x in corrGuesses:
            print(x, end=" ")
        print()

        # Print the incorrect guesses list
        print("Incorrect Guesses:", end=" ")
        for x in incorrGuesses:
            print(x, end=" ")
        print()

        # Get character from user
        # Check if the user's input is a valid character / if the character was already guessed
        while True:
            guessedChar = input("Guess a character: ").lower()
            if not guessedChar.isalpha() or not len(guessedChar) == 1:
                print("Please enter characters A-Z only")
                continue
            elif guessedChar in corrGuesses or guessedChar in incorrGuesses:
                print("That character was already used, please guess again.")
                continue
            else:
                break

        # Check user input
        # The variable miniCorrect is used if the guessed char appears more than once
        miniCorrect = 0
        for x in range(len(secretWord)):
            # User guess was correct
            if guessedChar == secretWord[x]:
                miniCorrect += 1
                correct += 1
                corrGuesses[x] = guessedChar

            # User guess was incorrect
            if x == (len(secretWord)-1) and miniCorrect == 0:
                print("Incorrect")
                errors += 1
                incorrGuesses.append(guessedChar)

        # One or more correct characters were found, print correct
        if miniCorrect > 0:
            print("Correct!")

        # Check if they got the whole word correct
        if correct == len(secretWord):
            print("********You won!********", "\nThe secret word was '{}'".format(secretWord))
            return 1

    # Errors were greater than 6, return you lost
    print(pics[6])
    print("********You lost!********", "\nThe Secret Word was '{}'".format(secretWord))
    return 0


main(randomWord())
while True:
    play = input("Would you like to play again? (Please type 'y' or 'n'): ")
    if play == "y":
        main(randomWord())
    else:
        break
exit()
