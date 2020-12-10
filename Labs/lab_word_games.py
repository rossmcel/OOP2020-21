# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: Lab wk8 - Word Games

# base class
class WordGames:
    """
    Class to represent the word game's base class.
    Methods and attributes that every type of word
    game should have are defined here.
    ...
    Attributes:
    -----------
        __my_words : str
        Read from user input and identifies the word
        or sentence that a user has inputted.

    Methods:
    --------
        the_words:
            Property getter method that returns
            the value of the user inputted word
            or sentence

        word_play:
            Contains logic for playing the game.
            Child classes should override this
            method in order to implement their own
            game logic.
    """
    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordGame object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            __my_words : str
                Variable that holds the user inputted word or
                sentence. Set to enforced encapsulation via
                name mangling.
        """
        self.__my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        """
        Property method to return the value of the user
        inputted word or sentence.

        Parameters: None.
        -----------

        Returns:
        ________
            __my_words : str
                The value of the word or sentence that has
                been inputted by a user.
        """
        return self.__my_words

    def word_play(self):
        """
        Plays the game. The base class version of playing
        the game simply prints the value that has been
        inputted.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        print("User input was: "+self.the_words)

class WordDuplication(WordGames):
    def word_play(self):

        print("User input doubled")

        print(self.the_words + ' ' + self.the_words)


class WordScramble(WordGames):
    def word_play(self):
        scrambled = ''
        list_of_words = self.the_words.split()
        tuple_of_punctuation = (',', '.', ';', '?', ' ', '!')

        for word in list_of_words:
            if(len(word) > 4 and word not in tuple_of_punctuation):
                scrambled += word[0] + word[-1] + word[2:-1] + word[1] + ' '
            else:
                print("Too few letters for scrambling: ", word)

        print(scrambled)



# prints the docstrings info
# if this class was a python module
print(WordGames.__doc__)

# Create an instances of the classes here:

#wd = WordDuplication()
#wd.word_play

ws = WordScramble()
ws.word_play()

