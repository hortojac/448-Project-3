# import tkinter module
from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial
from itertools import product       
 
# Create Object
root = Tk()
root.title("Connect 4") #labels our frame

# Initialize tkinter window with dimensions 100x100            
root.geometry('1500x1000')    
 
def show_frame(frame): #raises a frame when called
    frame.tkraise()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky = 'nsew') #frame 1 - 10 rows and columns initiliazed to 0 and widgest are sticky.


show_frame(frame1)

btn_frame1 = Button(frame1, text = 'Start', command=partial(show_frame,frame2), padx=100,pady=100).pack(side='right')
label_frame1 = Label(frame1, text="Press start to begin").pack(side='top')    

btn_frame2 = Button(frame2, text = 'Next', command=partial(show_frame,frame3), padx=100,pady=100).pack(side='right')
label_frame2 = Label(frame2, text="Player 1 place your piece").pack(side='top')

btn_frame3 = Button(frame3, text = 'Next', command=partial(show_frame,frame2), padx=100,pady=100).pack(side='right')
label_frame3 = Label(frame3, text="Player 2 place your piece").pack(side='top')
 
root.mainloop()