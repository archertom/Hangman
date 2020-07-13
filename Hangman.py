import string

# Needs a working random word generator.  Unfortunately no good, working packages seem to be available
# on Windows.  I don't feel like writing one currently, but the fuctionality can be tested by writing your
# own word in the variable "word" below.  NB the programme is designed to work with lowercase only so
# the .lower() has been added to automatically convert.
word = "hello".lower()

# gallows is a dictionary of ASCII images which depict a simple hangman progression.
gallows = {
    1:
        "|\n"
        "|\n"
        "|\n"
        "|\n"
        "|______________________\n"
        "\n",

    2:
        "_____________\n"
        "|/\n"
        "|\n"
        "|\n"
        "|\n"
        "|______________________\n"
        "\n",
    3:
        "_____________\n"
        "|/          |\n"
        "|\n"
        "|\n"
        "|\n"
        "|______________________\n"
        "\n",
    4:
        "_____________\n"
        "|/          |\n"
        "|           O\n"
        "|\n"
        "|\n"
        "|______________________\n"
        "\n",
    5:
        "_____________\n"
        "|/          |\n"
        "|           O\n"
        "|           |\n"
        "|\n"
        "|______________________\n"
        "\n",
    6:
        "_____________\n"
        "|/          |\n"
        "|         __O\n"
        "|           |\n"
        "|\n"
        "|______________________\n"
        "\n",
    7:
        "_____________\n"
        "|/          |\n"
        "|         __O__\n"
        "|           |\n"
        "|\n"
        "|______________________\n"
        "\n",
    8:
        "_____________\n"
        "|/          |\n"
        "|         __O__\n"
        "|           |\n"
        "|          /\n"
        "|______________________\n"
        "\n",
    9:
        "_____________\n"
        "|/          |\n"
        "|         __O__\n"
        "|           |\n"
        "|          /\\ \n"
        "|______________________\n"
        "  Sorry, you lost\n"
}


# i is the counter that controls the game steps.  It must be global as it is iterated through the game.
i = 1

# alpha is a list of lowercase letters, which will be removed from as guesses are made.
alpha = list(string.ascii_lowercase)

# finished tells the game whether it is over.
finished = False

# guessed is the list of past guesses, to check for duplicate guesses.
guessed = []


def letter_handling():
    global alpha
    global guessed
    while True:
        your_guess = input("Guess a letter")
        if str.isalpha(your_guess):
            str.lower(your_guess)
            if your_guess not in guessed:
                alpha.remove(your_guess)
                guessed.append(your_guess)
                return your_guess
            else:
                pass
        else:
            pass


# answer is the copy of the word which will have all unguessed letters substituted with underscores
# it must be global as it is used by both guess and hangman
answer = ""


def guess():
    global i
    global alpha
    global answer
    your_guess = letter_handling()
    if your_guess not in word:
        i += 1
    else:
        pass
    answer = word
    for letter in alpha:
        answer = answer.replace(letter, "_")
    print(answer)
    print(word)


def hangman():
    global finished
    while not finished:
        print(gallows[i])
        guess()
        if i == 9:
            print("The answer was", word)
            finished = True
        if answer == word:
            print("You won!")
            finished = True


hangman()
