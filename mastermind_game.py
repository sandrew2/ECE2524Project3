#Mastermind Game

from Tkinter import *
from random import randint

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.start_screen()

    def start_screen(self):
        #Create First Label
        self.welcome = Label(self, text = "Welcome to the Game of Mastermind!")
        self.welcome.grid()

        #Directions
        self.directions = Label(self, text = "The possible code characters are '#' '$' '%' '*' '@' '&'.")
        self.directions.grid(row=1)

        self.directions1 = Label(self, text = "You have 10 tries to guess the 4 character code.")
        self.directions1.grid(row=2)

        self.directions2 = Label(self, text = "If an 'X' is output, you guessed the right character in the right location.")
        self.directions2.grid(row=3)

        self.directions3 = Label(self, text = "If an 'O' is output, you guessed the right character in the wrong location.")
        self.directions3.grid(row=4)

        self.directions4 = Label(self, text = "If a '_' is output, the character is not in the code.")
        self.directions4.grid(row=5)

        self.directions5 = Label(self, text = "Repeats are allowed! Press start and good luck!")
        self.directions5.grid(row=6)

        self.start_btn = Button(self, text = "START", command = self.game)
        self.start_btn.grid(row=7)

    def game(self):
        #Initialize the possible character array and
        #the code array
        self.char_array = ['#', '$', '%', '*', '&', '@']
        self.code = [' ', ' ', ' ', ' ']
        
        #Populate the code array with randomly chosen possible
        #characters
        for num in (0,1,2,3):
            self.code[num] = self.char_array[randint(0,5)]
        
        #Clear the screen
        self.welcome.destroy()
        self.directions.destroy()
        self.directions1.destroy()
        self.directions2.destroy()
        self.directions3.destroy()
        self.directions4.destroy()
        self.directions5.destroy()
        self.start_btn.destroy()

        #Number of guesses tried if 0, player loses
        self.tries = 10

        #Initializes the game screen
        self.game_title = Label(self, text = "Lets play Mastermind!")
        self.game_title.grid(row=0, column=1, sticky=W)

        self.tries_rem = Label(self, text = "Tries Remaining: ")
        self.tries_rem.grid(row=1, sticky=W)

        self.tries_rem_out = Label(self, text=self.tries)
        self.tries_rem_out.grid(row=1, column=1, stick=W)

        self.game_in = Label(self, text="Input your guess,")
        self.game_in.grid(row=2, sticky=W)

        self.game_in = Label(self, text="please include spaces")
        self.game_in.grid(row=3, sticky=W)

        self.input_box = Entry(self)
        self.input_box.grid(row=2, column=1)
        self.guess = [' ', ' ', ' ', ' ']

        self.your_hint = Label(self, text = "Hint:")
        self.your_hint.grid(row=4, sticky=E)
        
        self.text = Text(self, width = 25, height = 1, wrap=WORD)
        self.text.grid(row=4, column=1, sticky=W)

        self.possible = Label(self, text = "Char's: # @ $ % & *")
        self.possible.grid(row=5, sticky=W)

        self.prev = Label(self, text="Previous entries and hints in command line")
        self.prev.grid(row=6, column=1)
                

        def get_in():
            self.guess = self.input_box.get()
            self.guess = self.guess.split()
            print self.guess
            self.tries -= 1
            self.tries_rem_out.destroy()
            self.tries_rem_out = Label(self, text=self.tries)
            self.tries_rem_out.grid(row=1, column=1, stick=W)
            self.text.delete(0.0, END)
            self.check_input()

        self.get_input = Button(self, text= "Enter", command=get_in)
        self.get_input.grid(row=2,column=2)

    def check_input(self):
        self.hint = [' ', ' ', ' ', ' ']
        if (self.guess == self.code):
            print "true"
            self.you_win()
        else:
            for num in (0,1,2,3):
                if(self.guess[num] == self.code[num]):
                   self.hint[num] = 'X'
                else:
                    elsewhere = 'False'
                    for x in (0,1,2,3):
                        if(self.guess[num] == self.code[x]):
                           self.hint[num] = 'O'
                           elsewhere = 'True'
                           x = 4
                        if(x == 3):
                            if(elsewhere == 'False'):
                                self.hint[num] = '_'
                                
        self.text.insert(0.0, self.hint)
        print self.hint
        if(self.tries == 0):
            self.you_lose()

    def you_win(self):
        self.game_title.destroy()
        self.tries_rem.destroy()
        self.tries_rem_out.destroy()
        self.game_in.destroy()
        self.input_box.destroy()
        self.your_hint.destroy()
        self.text.destroy()
        self.get_input.destroy()
        self.possible.destroy()
        self.prev.destroy()

        self.win_mess = Label(self, text = "Congradulations! You Win!")
        self.win_mess.grid()

        self.win_mess1 = Label(self, text = "Press reset to start a new game.")
        self.win_mess1.grid(row=1)

        self.win_mess2 = Label(self, text = "Or close this window and select a new game!")
        self.win_mess2.grid(row=2)

        self.reset_btn = Button(self, text="RESET", command = self.reset_game)
        self.reset_btn.grid(row=4)
                            
    def you_lose(self):
        self.game_title.destroy()
        self.tries_rem.destroy()
        self.tries_rem_out.destroy()
        self.game_in.destroy()
        self.input_box.destroy()
        self.your_hint.destroy()
        self.text.destroy()
        self.get_input.destroy()
        self.possible.destroy()
        self.prev.destroy()

        self.win_mess = Label(self, text = "Game Over. You lose!")
        self.win_mess.grid()

        self.win_mess1 = Label(self, text = "Press reset to start a new game.")
        self.win_mess1.grid(row=1)

        self.win_mess2 = Label(self, text = "Or close this window and select a new game!")
        self.win_mess2.grid(row=2)

        self.reset_btn = Button(self, text="RESET", command = self.reset_game)
        self.reset_btn.grid(row=4)

    def reset_game(self):
        self.win_mess.destroy()
        self.win_mess1.destroy()
        self.win_mess2.destroy()
        self.reset_btn.destroy()
        self.game()

        
game = Tk()
game.title("Mastermind")
game.geometry("390x200")

app = Application(game)

game.mainloop()
