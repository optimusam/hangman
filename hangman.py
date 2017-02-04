# Hangman game

import random
import string
import os

WORDLIST_FILENAME = "words.txt"

def clear():
    os.system("cls")

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    hint = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            hint+=letter
        else:
            hint+=" _ "
    return hint




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remLetters=""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            remLetters+=letter
    return remLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    guessesLeft = 8
    lettersGuessed = []
    previousWrongGuesses = []
    while guessesLeft!=0:
        print("-------------")
        print("You have {} guesses left.".format(guessesLeft))

        availableLetters = list(getAvailableLetters(lettersGuessed))

        print("Available letters: {}".format(''.join(availableLetters)))

        letGuessed = input("Please guess a letter: ")
        lettersGuessed.append(letGuessed)
        guessedWord = getGuessedWord(secretWord, lettersGuessed)

        if letGuessed in guessedWord and letGuessed not in previousWrongGuesses and letGuessed in availableLetters:
            print("Good guess: {}".format(guessedWord))
            availableLetters.remove(letGuessed)

        elif letGuessed in guessedWord and letGuessed not in previousWrongGuesses and letGuessed not in availableLetters:
            print("Oops! You've already guessed that letter: {}".format(guessedWord))


        elif letGuessed not in guessedWord and letGuessed not in previousWrongGuesses:
            print("Oops! That letter is not in my word: {}".format(guessedWord))
            guessesLeft-=1
            previousWrongGuesses.append(letGuessed)

        elif letGuessed in previousWrongGuesses:
            print("Oops! You've already guessed that letter: {}".format(guessedWord))

        gameOver = isWordGuessed(secretWord, lettersGuessed)
        if gameOver:
            print("-------------")
            print("Congratulations, you won!")
            break
    if guessesLeft==0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))


while True:
    clear()
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    ch = input("Do you want to play again? y or n: ")
    if ch=='n' or ch=='no' or ch=='nope':
        break




