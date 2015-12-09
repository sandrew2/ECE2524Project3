#Main GUI

from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.start_screen()

    def start_screen(self):
        #Create First Label
        self.label1 = Label(self, text = "Welcome to the Mini-Game Console!")
        self.label1.grid()

        #Create Second Label
        self.label2 = Label(self, text = "Press start to begin!")
        self.label2.grid(row=1)

        #Create Start Button
        self.button1 = Button(self, text = "START", command = self.next_screen)
        self.button1.grid(row=2)

        #Class Stuff
        self.class_label = Label(self, text = "ECE 2524 UNIX Project 3")
        self.class_label.grid(row=3)
        
        #Author Stuff
        self.author_label = Label(self, text = "By Adam Donovan, Anthony Clifton,")
        self.author_label.grid(row=4)

        self.author_cont = Label(self, text = "and Andrew Shivers")
        self.author_cont.grid(row=5)

    def next_screen(self):
        #Clear welcome screen
        self.label1.destroy()
        self.label2.destroy()
        self.button1.destroy()
        self.class_label.destroy()
        self.author_label.destroy()
        self.author_cont.destroy()
        #Resize the frame
        gui.geometry("500x300")
        #Move to the main menu
        self.main_menu()

    def main_menu(self):
        self.label4 = Label(self, text = "Main Menu", font = 38, fg="red")
        self.label4.grid(row=0)

        self.label5 = Label(self, text = "Would you like to play a game?")
        self.label5.grid(row=1, column=1)

        #Hangman BTN and description
        self.hangman_button = Button(self, text = "START", command = self.hangman)
        self.hangman_button.grid(row=3)

        self.hangman_desc = Label(self, text = "Play the classic game of hangman versus a computer! You have 7 tries")
        self.hangman_desc.grid(row=3, column=1, sticky=W)

        self.hangman_desc_cont = Label(self, text = "to guess the word before the man hangs!")
        self.hangman_desc_cont.grid(row=4, column=1, sticky=W)

        #Tic-Tac-Toe BTN and description
        self.tictactoe_button = Button(self, text = "START", command = self.tictactoe)
        self.tictactoe_button.grid(row=5)

        self.tictactoe_desc = Label(self, text = "Play the classic game of tic-tac-toe versus a computer! Choose to be")
        self.tictactoe_desc.grid(row=5, column=1, sticky=W)

        self.tictactoe_desc_cont = Label(self, text = "X's or O's and see if you can best the computer!")
        self.tictactoe_desc_cont.grid(row=6, column=1, sticky=W)

        #Connect4 BTN and description
        self.connect4_button = Button(self, text = "START", command = self.connect4)
        self.connect4_button.grid(row=7)

        self.connect4_desc = Label(self, text = "Play the classic game of Connect Four versus a computer! Choose to be")
        self.connect4_desc.grid(row=7, column=1, sticky=W)

        self.connect4_desc_cont = Label(self, text = "Red or Black and see if you can best the computer!")
        self.connect4_desc_cont.grid(row=8, column=1, sticky=W)

        #General Stuff
        self.divider = Label(self, text = "---------------------------------------------------------------------------")
        self.divider.grid(row=9, column=1, sticky=W)
        
        self.description = Label(self, text = "Each time you select a game it will open a new window with that game.")
        self.description.grid(row=10, column=1, sticky=W)

        self.description2 = Label(self, text = "Simply close out of the game window when you are done with that")
        self.description2.grid(row=11, column=1, sticky=W)

        self.description3 = Label(self, text = "game and select a new one!")
        self.description3.grid(row=12, column=1, sticky=W)


    def hangman(self):
        import hangman

    def tictactoe(self):
        import TicTacToe
        TicTacToe.playGame()

    def connect4(self):
        import connect4
        

#modify root window
gui = Tk()
gui.title("GameConsole")
gui.geometry("200x130")

app = Application(gui)

#kick off the event loop
gui.mainloop()

