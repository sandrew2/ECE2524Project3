#Main GUI

from Tkinter import *

#create the window
gui = Tk()

#modift root window
gui.title("GameConsole")
gui.geometry("225x200")

app = Frame(gui)
app.grid()
Label(gui, text = "Welcome to the Mini-Game Console!").grid(row=0)
Label(gui, text = "Enter your name then press start to begin!").grid(row=1)
Label(gui, text = "Your Name:").grid(row=2, column=0)
name = Entry(gui)
name.grid(row=2, column=1)
Button(gui, text = "START").grid(row=3)

#kick off the event loop
gui.mainloop()
