#Main GUI

from Tkinter import *

#create the window
gui = Tk()

#modift root window
gui.title("GameConsole")
gui.geometry("230x200")

app = Frame(gui)
app.grid()
Label(gui, text = "Welcome to the Mini-Game Console!").grid(row=0)
Label(gui, text = "Enter your name then press start to begin!").grid(row=1)
Label(gui, text = "Enter Name Here:").grid(row=2, sticky=W)
Entry(gui).grid(row=2, sticky=E)
Button(gui, text = "START").grid(row=3)

#kick off the event loop
gui.mainloop()
