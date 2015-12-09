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
        #hangman game method
        self.word_select = random.randint(0, 16)
        self.guess_count = 0
        self.words=dictionary.readlines()
        self.answer = self.words[self.word_select]
        
        #guess entry window and submit button
        self.entry_window = Entry(self)
        self.entry_window.grid(row=1, sticky=W)
        self.submit = Button(self, text = "Submit", command = self.update_hang)
        self.submit.grid(row=1, sticky=E)
        self.feedback = Label(self, text = "___ \n   |")
        self.feedback.grid(row=2)
        
    def update_hang(self):
        self.guess_count +=1
        

#modify root window
gui = Tk()
gui.title("GameConsole")
gui.geometry("230x200")

app = Application(gui)

#kick off the event loop
gui.mainloop()
