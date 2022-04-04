from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial   
from PIL import ImageTk, Image

def show_frame(frame):
    frame.tkraise()


root = Tk()
root.state('zoomed') #puts the window mode in zoomed
root.title("Rock Paper Scissors Lizard Spock") #labels our frame


#Initialize start image for use

image=Image.open("assets/rpsls/start.jpeg") 
#img=image.resize((40,40))
img_start=ImageTk.PhotoImage(image) #image for just the start button (bg set to blue)

image=Image.open("assets/rpsls/rules.png") 
#img=image.resize((40,40))
img_start=ImageTk.PhotoImage(image) #image for just the start button (bg set to blue)

frame1 = Frame(root) #welcome menu frame

frame2 = Frame(root) # main gameplay frame

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky = 'nsew') #frames' rows and columns initiliazed to 0 and widgets are sticky.


show_frame(frame1)

#frame1 code
frame1_welcomeTxt = Label(frame1, text="Welcome to Rock Paper Scissors Lizard Spock",font=("Arial", 25))
frame1_welcomeTxt.grid(rowspan=2, columnspan=4) #place(relx=.5, rely=.2, anchor=CENTER)

frame1_startBtn = Button(frame1, text="Start",font=("Arial",50, BOLD), command=partial(show_frame,frame2))
frame1_startBtn.grid()#place(relx=.5, rely=.5, anchor=CENTER)

frame1_exitBtn = Button(frame1, text="Exit",font=("Arial",50, BOLD), command=partial(root.destroy)) #exits the program
frame1_exitBtn.grid()#place(relx=.5, rely=.5, anchor=CENTER)

##
myLabel1 = Label(frame1, text="Battleship!\nPress start to begin playing.",font=("Arial", 25)).place(relx=.5, rely=.2,anchor= CENTER)
frame1_button = Button(frame1, text="Start",font=("Arial",70, BOLD), command=partial(show_frame,frame2), bg="white", padx=20,pady=20, image=img_start, compound=CENTER).place(relx=.50, rely=.5,anchor= CENTER)

#frame2 code
frame2_txt = Label(frame2, text="Gameplay Coming Soon!",font=("Arial", 25))
frame2_txt.grid(rowspan=2, columnspan=4) #place(relx=.5, rely=.2, anchor=CENTER)
frame2_exitBtn = Button(frame2, text="Exit",font=("Arial",50, BOLD), command=partial(root.destroy)) #exits the program
frame2_exitBtn.grid()#place(relx=.5, rely=.5, anchor=CENTER)

root.mainloop()