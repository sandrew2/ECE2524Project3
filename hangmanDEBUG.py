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
        self.word_select = random.randint(0, 22)
        self.words=dictionary.readlines()
        self.answer = self.words[self.word_select]
        #close the file now
        dictionary.close()
        #initialize other necessary variables
        self.correctLetters = ''
        self.missedLetters = ''
        self.gameOver = False
        
        #guess entry window and submit button
        self.rules = Label(self, text = "Rules:\nAll letters are lower case\nType a letter to guess in the box and hit submit")
        self.rules.grid(row=0, column=0)
        self.entry_window = Entry(self)
        self.entry_window.grid(row=1, sticky=W)
        self.submit = Button(self, text = "Submit", command = self.update_hang)
        self.submit.grid(row=1, sticky=E)
        self.feedback = Text(self, width=40, height=15, wrap=NONE)
        self.feedback.grid(row=2)
        self.feedback.insert(0.0, self.HANGMANPICS[0])
        self.guesses = Label(self, text = self.missedLetters)
        self.guesses.grid(row=3, sticky=W)

        self.correct = Label(self, text = correctLetters)
        self.correct.grid(row=3, sticky=E)
        
        
    def update_hang(self):

        self.feedback.delete(0.0, END)
        hangIndex = len(self.missedLetters)
        self.feedback.insert(0.0, self.HANGMANPICS[hangIndex])
        
        #updates letter guess Label
        letter = self.entry_window.get()
        #ensures that the user input is lowercase
        letter = letter.lower()
        if len(letter) != 1:
            self.feedback.insert(0.0, "Enter a LETTER please")
        
        for i in range(len(self.answer)):
            if letter in self.answer:
                self.correctLetters += letter
                foundAllLetters = True
                if self.answer[i] not in correctLetters:
                    foundAllLetters = False
                    break
                
                if foundAllLetters:
                    self.correct["text"] = "You have won the answer is : " + self.answer
                    self.gameOver = True
                
            else:
                self.missedLetters += letter
                #check to make sure they didn't run out of attempts
                if len(self.missedLetters) == len(self.HANGMANPICS) - 1:
                    self.guesses["text"] = "You've run out of guesses. Answer was: " + self.answer
                    self.gameOver = True


            
        
        self.feedback.insert(0.0, "answer is: " + self.answer)
        self.feedback.insert(0.0, "incorrect guess count is : " + str(len(self.missedLetters) + " ")

        
        
                             
        

#modify root window
gui = Tk()
gui.title("Hangman")
gui.geometry("400x400")

app = Application(gui)

#kick off the event loop
gui.mainloop()
