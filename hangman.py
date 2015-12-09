from Tkinter import *

import random

class Application(Frame):

    #constructor for the app
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.hang_man()

    def hang_man(self):
        
        dictionary = open('Dictionary.txt', 'r')
        self.HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

        
        #hangman game method
        self.word_select = random.randint(0, 16)
        self.guess_count = 0
        self.words=dictionary.readlines()
        self.answer = self.words[self.word_select]
        #close the file now
        dictionary.close()
        
        #guess entry window and submit button
        self.rules = Label(self, text = "Rules:\nAll letters are lower case\nType a letter to guess in the box and hit submit")
        self.rules.grid(row=0, column=0)
        self.entry_window = Entry(self)
        self.entry_window.grid(row=1, sticky=W)
        self.submit = Button(self, text = "Submit", command = self.update_hang)
        self.submit.grid(row=1, sticky=E)
        self.feedback = Text(self, width=40, height=15, wrap=NONE)
        self.feedback.grid(row=2)
        self.letter_guesses = "You've guessed: "
        self.guesses = Label(self, text = self.letter_guesses)
        self.guesses.grid(row=3, stick=W)        
        
    def update_hang(self):
        #updates feedback window
        #currently WILL increment every time
        #not just when wrong
        #fix
        self.feedback.delete(0.0, END)
        for i in self.HANGMANPICS:
            if i == self.guess_count:
                self.feedback.insert(self.HANGMANPICS[i])
        self.guess_count +=1
        
        #updates letter guess Label
        letter = self.entry_window.get()
        for i in self.answer:
            if letter == i:
                boolVar = TRUE
            else:
                boolVar = FALSE
        if boolVar == TRUE:
            #do stuff
            for inc in self.answer:
                if letter == inc:
                    print(letter)
                else:
                    print("_")
        else:
            self.letter_guesses += " " + letter + ","
            self.guesses["text"] = self.letter_guesses
            
        
        self.feedback.insert(0.0, "answer is: " + self.answer)
        self.feedback.insert(0.0, "guess count is : " + str(self.guess_count) + " ")
        
        

#modify root window
gui = Tk()
gui.title("GameConsole")
gui.geometry("400x400")

app = Application(gui)

#kick off the event loop
gui.mainloop()
