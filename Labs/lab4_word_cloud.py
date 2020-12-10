# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 4


class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.gettylistmain = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html()

        print(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self):

        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        for word in self.gettylistmain:
            size = self.my_dict[word]
            basesize = 10
            size = size * basesize
            fo.write('<span style="font-size:' + str(size) + 'px">' + word + ' </span>')

        fo.write('</div>\
            </body>\
            </html>')

        fo.close()


    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):

        # your code goes here:
        gettisburgTextFile = open("gettisburg.txt")
        gettisburgText = gettisburgTextFile.read()

        gettylist = (list(gettisburgText.split(" ")))

        self.my_dict = dict()

        for word in gettylist:
            if word in self.my_dict:
                self.my_dict[word] = self.my_dict[word] + 1
            else:
                self.my_dict.update({word: 1})


        for word in self.my_dict:
            if self.my_dict[word] > 1:
                self.my_dict[word] = self.my_dict[word] + 1



        return gettylist

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):
        # your code goes here

        return the_dict


wc = WordCloud()
wc.__init__()
