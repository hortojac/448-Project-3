
# import tkinter module
from array import array
from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial     
from itertools import product
 
# Create Object
root = Tk()
root.title("Connect 4") 
root.state('zoomed') 

def show_frame(frame): #raises a frame when called
    frame.tkraise()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky = 'nsew') #frame 1 - 10 rows and columns initiliazed to 0 and widgest are sticky.


show_frame(frame1)

global textvariable
textvariable = 'X'

def enable_player1():
    global btn_frame2
    global btn_column1
    global btn_column2
    global btn_column3
    global btn_column4
    global btn_column5
    global btn_column6
    global btn_column7
    btn_frame2.configure(state=NORMAL)
    btn_column1.configure(state=DISABLED)
    btn_column2.configure(state=DISABLED)
    btn_column3.configure(state=DISABLED)
    btn_column4.configure(state=DISABLED)
    btn_column5.configure(state=DISABLED)
    btn_column6.configure(state=DISABLED)
    btn_column7.configure(state=DISABLED)

def enable_player2():
    global btn_frame3
    global btn_column1_2
    global btn_column2_2
    global btn_column3_2
    global btn_column4_2
    global btn_column5_2
    global btn_column6_2
    global btn_column7_2
    btn_frame3.configure(state=NORMAL)
    btn_column1_2.configure(state=DISABLED)
    btn_column2_2.configure(state=DISABLED)
    btn_column3_2.configure(state=DISABLED)
    btn_column4_2.configure(state=DISABLED)
    btn_column5_2.configure(state=DISABLED)
    btn_column6_2.configure(state=DISABLED)
    btn_column7_2.configure(state=DISABLED)

def setup_frame2():
    global btn_frame2
    global btn_column1
    global btn_column2
    global btn_column3
    global btn_column4
    global btn_column5
    global btn_column6
    global btn_column7
    btn_frame2.configure(state=DISABLED)
    btn_column1.configure(state=NORMAL)
    btn_column2.configure(state=NORMAL)
    btn_column3.configure(state=NORMAL)
    btn_column4.configure(state=NORMAL)
    btn_column5.configure(state=NORMAL)
    btn_column6.configure(state=NORMAL)
    btn_column7.configure(state=NORMAL)
    show_frame(frame2)

def setup_frame3():
    global btn_frame3
    global btn_column1_2
    global btn_column2_2
    global btn_column3_2
    global btn_column4_2
    global btn_column5_2
    global btn_column6_2
    global btn_column7_2
    btn_frame3.configure(state=DISABLED)
    btn_column1_2.configure(state=NORMAL)
    btn_column2_2.configure(state=NORMAL)
    btn_column3_2.configure(state=NORMAL)
    btn_column4_2.configure(state=NORMAL)
    btn_column5_2.configure(state=NORMAL)
    btn_column6_2.configure(state=NORMAL)
    btn_column7_2.configure(state=NORMAL)
    show_frame(frame3)


label_frame1 = Label(frame1, text="Connect 4!\nPress start to begin playing.",font=("Arial", 25)) 
label_frame1.place(relx=.5, rely=.1,anchor= CENTER)
btn_frame1 = Button(frame1, text="Start", font=("Arial",50, BOLD), command=partial(show_frame,frame2), padx=20,pady=20, compound=CENTER) #Big button to start the game
btn_frame1.place(relx=.5, rely=.5, anchor=CENTER)
button_quit_game = Button(frame1, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the program
button_quit_game.place(relx=.5, rely=.9, anchor=CENTER)

label_frame2 = Label(frame2, text="Player 1 place your piece").grid(row=0, column=0)
btn_frame2 = Button(frame2, text = 'Next', command=partial(setup_frame3), state=DISABLED, padx=5,pady=5)
btn_frame2.grid(row=1, column=0)
button_quit_game = Button(frame2, text="Press to Quit" , command=root.destroy).grid(row=0, column=40) #press to quit button, closes program

btn_column1 = Button(frame2, text = 'Column 1', command=partial(enable_player1), padx=5,pady=5)
btn_column1.grid(row=3, column = 1)
btn_column2 = Button(frame2, text = 'Column 2', command=partial(enable_player1), padx=5,pady=5)
btn_column2.grid(row=3, column=2)
btn_column3 = Button(frame2, text = 'Column 3', command=partial(enable_player1), padx=5,pady=5)
btn_column3.grid(row=3, column=3)
btn_column4 = Button(frame2, text = 'Column 4', command=partial(enable_player1), padx=5,pady=5)
btn_column4.grid(row=3, column=4)
btn_column5 = Button(frame2, text = 'Column 5', command=partial(enable_player1), padx=5,pady=5)
btn_column5.grid(row=3, column=5)
btn_column6 = Button(frame2, text = 'Column 6', command=partial(enable_player1), padx=5,pady=5)
btn_column6.grid(row=3, column=6)
btn_column7 = Button(frame2, text = 'Column 7', command=partial(enable_player1), padx=5,pady=5)
btn_column7.grid(row=3, column=7)

for i in range(6):
    for j in range(7):
        game_board = Label(frame2, text=textvariable, fg='black', padx=20,pady=20).grid(row=4+i, column=j+1)

label_frame3 = Label(frame3, text="Player 2 place your piece").grid(row=0, column=0)
btn_frame3 = Button(frame3, text = 'Next', command=partial(setup_frame2), padx=5,pady=5, state=DISABLED)
btn_frame3.grid(row=1, column=0)
button_quit_game = Button(frame3, text="Press to Quit" ,command=root.destroy).grid(row=0, column=40)#press to quit button, closes program
btn_column1_2 = Button(frame3, text = 'Column 1', command=partial(enable_player2), state=NORMAL, padx=5,pady=5)
btn_column1_2.grid(row=3, column = 1)
btn_column2_2 = Button(frame3, text = 'Column 2', command=partial(enable_player2), padx=5,pady=5)
btn_column2_2.grid(row=3, column=2)
btn_column3_2 = Button(frame3, text = 'Column 3', command=partial(enable_player2), padx=5,pady=5)
btn_column3_2.grid(row=3, column=3)
btn_column4_2 = Button(frame3, text = 'Column 4', command=partial(enable_player2), padx=5,pady=5)
btn_column4_2.grid(row=3, column=4)
btn_column5_2 = Button(frame3, text = 'Column 5', command=partial(enable_player2), padx=5,pady=5)
btn_column5_2.grid(row=3, column=5)
btn_column6_2 = Button(frame3, text = 'Column 6', command=partial(enable_player2), padx=5,pady=5)
btn_column6_2.grid(row=3, column=6)
btn_column7_2 = Button(frame3, text = 'Column 7', command=partial(enable_player2), padx=5,pady=5)
btn_column7_2.grid(row=3, column=7)
for i in range(6):
    for j in range(7):
        game_board = Label(frame3, text=textvariable, fg='black', padx=20,pady=20).grid(row=4+i, column=j+1)


root.mainloop()