# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # check input type
        self.user_input = self.user_input.lower()

        # split string into list of words
        my_list = (list(self.user_input.split(" ")))

        # first scramble is just one word
       # word = my_list[0]
        #print(word)
        #wordList = list(word)
        #print(wordList)
        #wordList[1], wordList[2] = wordList[2], wordList[1]
        #print(wordList)


        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3

        #wordList[-2], wordList[-3] = wordList[-3], wordList[-2]
        #word = ''.join(wordList)
        #print(word)


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

        for i in range(len(my_list)):

            word = my_list[i]

            if(len(word) > 3):
                wordList = list(word)
                wordList[1], wordList[2] = wordList[2], wordList[1]
                wordList[-2], wordList[-3] = wordList[-3], wordList[-2]
                my_list[i] = ''.join(wordList)



        my_list = ' '.join(my_list)
        print(my_list)




word_scrambler = WordScramble()
word_scrambler.scramble()

