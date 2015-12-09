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
        self.label2 = Label(self, text = "Enter Name Here:")
        self.label2.grid(row=2, sticky=W)

        #Create Name Entry Box
        self.en1 = Entry(self)
        self.en1.grid(row=2, sticky=E)

        #Create Start Button
        self.button1 = Button(self, text = "START")
        self.button1.grid(row=3)

#modift root window
gui = Tk()
gui.title("GameConsole")
gui.geometry("230x200")

app = Application(gui)

#kick off the event loop
gui.mainloop()
