# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# original template author: B. Schoen-Phelan
# primary author: Ross McElhinney
# date: Oct 2020
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *
from tkinter import simpledialog

# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle

# used to shuffle the deck
import random


# used to restart the program
import os


import time


class CardGame():

    # initialises the application
    def __init__(self):
        # set up game logic here:


        # variable for holding the score
        self.score = 0

        # load and shuffle the cards before first use
        self.load_cards()

        # update the score to the value of the first card
        self.update_score()

        # initiate window on start-up - all further function calls are executed through the buttons in this function
        self.init_window()







    # used by __init__
    # initialises the GUI window
    def init_window(self):

        # set the window
        self.root = Tk()
        self.root.geometry("500x600")
        self.root.title("Card Game")

        master_frame = Frame(master=self.root)
        master_frame.pack(expand=True)


        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        self.cards_frame = LabelFrame(master=master_frame)
        self.cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        self.score_frame = LabelFrame(master=master_frame)
        self.score_frame.grid(row=1, column=0, columnspan=2)



        # add first card into the image frame
        # present card
        self.open_card = Button(self.cards_frame)
        card = "cards/" + self.part_the_card
        self.the_card = PhotoImage(file=card)
        self.open_card.config(image=self.the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = self.the_card



        # closed deck image frame - clicking on this fetches a new card - through the self.pick_card function
        closed_deck = Button(self.cards_frame, command=self.pick_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        # done button - clicking on this calls self.done_playing()
        done_button = Button(button_frame, text="I'm done!", command=self.done_playing)
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.reset_game)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        # score label
        self.score_label = Label(self.score_frame, text="Your score: " + str(self.score), justify=LEFT)
        self.score_label.pack()

        # mainloop - keeps the program running waiting for user input
        self.root.mainloop()


    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # helper function to load the cards and card images
    # assigns .gif files to each card
    # puts everything in a tuple list first as it needs to be shuffled
    # copies tuple list contents into queue
    def load_cards(self):
        # cards queue
        self.cards = Queue(maxsize=52)
        # picture for cards queue
        self.cardsPicture = Queue(maxsize=52)

        # card groups
        suits = ("hearts", "diamonds", "spades", "clubs")
        people = ("queen", "jack", "king")
        ace = "Ace"

        #temporary lists for card and card picture assignments
        card_list = []
        card_list_pic = []

        # loop through each suit and assign the number, people and ace cards to each, along with their
        # corresponding gif images
        for t in range(len(suits)):
            card_list.append(suits[t] + ace)
            card_list_pic.append("1" + "_" + suits[t] + ".gif")
            # number cards
            for i in range(9):
                # increase value by 1 to account for index starting at 0 and increase by 1 again to account for
                # there being no #1 card (e.g. 1 of Hearts - does not exist) - subsequently, range is decreased to 9
                # to accommodate this
                holder = i + 2
                # cast holder to string to allow concatenation
                holder = str(holder)
                card_list.append(suits[t] + holder)
                card_list_pic.append(holder + "_" + suits[t] + ".gif")
            # people cards
            for i in range(3):
                card_list.append(suits[t] + people[i])
                card_list_pic.append(people[i] + "_" + suits[t] + ".gif")

        # your code goes here:
        c = list(zip(card_list, card_list_pic))

        random.shuffle(c)

        card_list, card_list_pic = zip(*c)
        print(card_list)
        print(card_list_pic)

        for i in range(52):
            self.cards.put(card_list[i])
            self.cardsPicture.put(card_list_pic[i])

        self.part_the_card = self.cardsPicture.get()
        self.cardTemp = self.cards.get()


    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score
    def pick_card(self):

        # image for card
        self.part_the_card = self.cardsPicture.get()
        # card
        self.cardTemp = self.cards.get()

        # Start new card frame
        self.open_card = Button(self.cards_frame)
        card = "cards/" + self.part_the_card
        self.the_card = PhotoImage(file=card)
        self.open_card.config(image=self.the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = self.the_card

        # update the score
        self.update_score()
        # check the score to make sure it is under 21 - else the game finishes
        self.check_scores()

        # update the score label
        self.score_label = Label(self.score_frame, text="Your score: " + str(self.score), justify=LEFT)
        self.score_label.pack()

    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label
    def check_scores(self):

        # cast the variable as an integer to allow number comparison
        self.score = int(self.score)

        # is score is above 21, end the game
        if self.score > 21:
            self.done_playing()





    # calculates the new score
    def update_score(self):
        # lScore is a temporary holder for the current card - cast as string to allow string split
        lScore = str(self.cardTemp)
        if "clubs" in lScore:
            lScore = lScore.split("clubs", 1)
        elif "diamonds" in lScore:
            lScore = lScore.split("diamonds", 1)
        elif "hearts" in lScore:
            lScore = lScore.split("hearts", 1)
        elif "spades" in lScore:
            lScore = lScore.split("spades", 1)

        # Assigning it the lScore[1] value is needed because for some reason '' is returned along with the score,
        # at the 0th index
        lScore = lScore[1]
        print(lScore)

        # queen, kings, jacks assigned 10
        if lScore == "queen" or lScore == "king" or lScore == "jack":
            self.score = self.score + 10
        # ace assigned 1
        elif lScore == "Ace":
            self.score = self.score + 1
        # numbers assigned their individual values
        else:
            self.score = self.score + int(lScore)

    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.
    def done_playing(self):
        # update the score label to display the message that the game is finished and display the user's score
        self.score_label = Label(self.score_frame, text="You're done! You finished with a score of " + str(self.score), justify=LEFT)
        self.score_label.pack()

        # force user to choose between starting a new game and exiting the game - 'n' for new game, any other key for exit
        answer = simpledialog.askstring("Input", "Enter 'n' to start a new game, or any other key to exit",
                                        parent=self.root)
        if answer == 'n':
            self.reset_game()
        else:
            self.game_exit()

    # this method is called when the "New Game" button is clicked
    # restarts the module completely
    def reset_game(self):
        # completely restart the game - using os import
        os.system("python lab5_card_game.py")
        exit()





# object creation here:
app = CardGame()
