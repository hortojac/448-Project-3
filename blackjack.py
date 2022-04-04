from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial   
from PIL import ImageTk, Image

def show_frame(frame):
    frame.tkraise()


root = Tk()
root.state('zoomed') #puts the window mode in zoomed
root.title("BlackJack") #labels our frame

frame1 = Frame(root) #welcome menu frame

frame2 = Frame(root) # main gameplay frame

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky = 'nsew') #frames' rows and columns initiliazed to 0 and widgets are sticky.


show_frame(frame1)

#frame1 code
frame1_welcomeTxt = Label(frame1, text="Welcome to BlackJack",font=("Arial", 25))
frame1_welcomeTxt.grid(rowspan=2, columnspan=4)

frame1_startBtn = Button(frame1, text="Start",font=("Arial",50, BOLD), command=partial(show_frame,frame2))
frame1_startBtn.grid(row=5, column = 2)

frame1_exitBtn = Button(frame1, text="Exit",font=("Arial",50, BOLD), command=partial(root.destroy)) #exits the program
frame1_exitBtn.grid(row=6, column=2)

root.mainloop()
