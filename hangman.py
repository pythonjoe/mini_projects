"""
Name: Hangman.py
Author: Joe Hartman
"""

def index_finder(word, letter):
	"""
	Takes in a word and a letter as parameters and returns the index of the letter in the word.
	:param word: str
	:param letter: str
	:return: list

	>>> index_finder("apple", "p")
	[2, 3]

	>>> index_finder("joe", "o")
	[2]

    """
	indexes = []
	for index, char in enumerate(word):
		if char == letter:
			indexes.append(index + 1)
	return indexes

def valid_input(letter):
    """
    Takes in a letter as a string and returns a boolean based on if the input is valid.
    :paramen letter: str
    :return: bool

    >>> valid_input('a')
    True

    >>> valid_input("apple")
    False

    >>> valid_input('sfo')
    False

    """
    if len(letter) == 1 and type(letter) == str:
        return True
    return False

def picture(num):
    """
    Takes in a number and prints the index of that number.
    :paramen letter: int

    >>> picture(2)
    '''
    ______
	|    o
	|    |
	|
	|
	|
	|
	--------
    '''

    """

	lives = (
	'''
	______
	|
	|
	|
	|
	|
	|
	--------
	''',
	'''
	______
	|    o
	|
	|
	|
	|
	|
	--------
	''',
	'''
	______
	|    o
	|    |
	|
	|
	|
	|
	--------
	''',
	'''
	______
	|    o
	|    |
	|   /
	|
	|
	|
	|
	|
	|
	--------
	''',
	'''
	______
	|    o
	|    |
	|   / \\
	|
	|
	|
	|
	|
	--------
	''',
	'''
	______
	|    o
	|   /|
	|   / \\
	|
	|
	|
	|
	|
	--------
	''',
	'''
	______
	|    o
	|   /|\\
	|   / \\
	|
	|
	|
	|
	|
	--------
	''',
	'''
	______
	|    |
	|    x
	|   /|\\
	|   / \\
	|
	|
	|
	|
	|
	--------
	'''
	)

	print(lives[num])




def hangman():
	indexes = []
	lives = 0
	word = raw_input("Give me word: ")
	already_guessed = []
	while lives < 7:
		if len(indexes) == len(word):
			print("The word is {0}.".format(word))
			print("You win!")
			return
		guess = raw_input("Guess a letter: ")
		if valid_input(guess):
			if guess not in already_guessed:
				already_guessed.append(guess)
				if guess in word :
					indexes += 	index_finder(word, guess)
					print("You guessed {0}. It occurs {1} times. It's in the following postions: {2}".format(guess, len(index_finder(word, guess)), index_finder(word, guess)))
					picture(lives)

				else:
					lives += 1
					lives_left = 7 - lives
					picture(lives)
					print("{0} is not in the word. You have {1} lives left.".format(guess, lives_left))
			else:
				print("You already guessed that. Try again.")

		else:
			print("That is not a valid input. Please try again.")

	else:
		print("You lost!")

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    hangman()
