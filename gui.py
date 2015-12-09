#Main GUI

from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Create First Label
        self.label1 = Label(self, text = "Welcome to the Mini-Game Console!")
        self.label1.grid()

        #Create Second Label
        self.label2 = Label(self, text = "Enter your name then press start to begin!")
        self.label2.grid(row=1)

        #Create Third Label
        self.label3 = Label(self, text = "Enter Name Here:")
        self.label3.grid(row=2, sticky=W)

        #Create Name Entry Box
        self.en1 = Entry(self)
        self.en1.grid(row=2, sticky=E)

        #Create Start Button
        self.button1 = Button(self, text = "START", command = self.next_screen)
        self.button1.grid(row=3)

    def next_screen(self):
        #Save input name
        self.user_name = StringVar()
        self.user_name = self.en1.get()
        #Clear welcome screen
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.en1.destroy()
        self.button1.destroy()
        #Resize the frame
        gui.geometry("500x500")
        #Move to the main menu
        self.main_menu()

    def main_menu(self):
        self.label4 = Label(self, text = "Main Menu", font = 38, fg="red")
        self.label4.grid(row=0)

        self.label5 = Label(self, text ="Welcome to the fun")
        self.label5.grid(row=1)

        self.label6 = Label(self, textvariable = self.user_name)
        self.label6.grid(row=2)

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

    def hangman(self):
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.hangman_button.destroy()
        self.hangman_desc.destroy()
        self.hangman_desc_cont.destroy()
        self.tictactoe_button.destroy()
        self.tictactoe_desc.destroy()
        self.tictactoe_desc_cont.destroy()
        self.connect4_button.destroy()
        self.connect4_desc.destroy()
        self.connect4_desc_cont.destroy()

    def tictactoe(self):
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.hangman_button.destroy()
        self.hangman_desc.destroy()
        self.hangman_desc_cont.destroy()
        self.tictactoe_button.destroy()
        self.tictactoe_desc.destroy()
        self.tictactoe_desc_cont.destroy()
        self.connect4_button.destroy()
        self.connect4_desc.destroy()
        self.connect4_desc_cont.destroy()
        #Start Tic-Tac-Toe Code

    def connect4(self):
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.hangman_button.destroy()
        self.hangman_desc.destroy()
        self.hangman_desc_cont.destroy()
        self.tictactoe_button.destroy()
        self.tictactoe_desc.destroy()
        self.tictactoe_desc_cont.destroy()
        self.connect4_button.destroy()
        self.connect4_desc.destroy()
        self.connect4_desc_cont.destroy()

#modify root window
gui = Tk()
gui.title("GameConsole")
gui.geometry("230x200")

app = Application(gui)

#kick off the event loop
gui.mainloop()
