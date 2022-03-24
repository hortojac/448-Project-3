from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial   
from PIL import ImageTk, Image
import os
import sys

def show_frame(frame):
    frame.tkraise()

def runRPSLS():
    os.system('python3 rpsls.py')

root = Tk()
root.state('zoomed') #puts the window mode in zoomed
root.title("Rock Paper Scissors Lizard Spock") #labels our frame

frame1 = Frame(root)

#for frame in (frame1):
frame1.grid(row=0, column=0, sticky = 'nsew') #frame 1 - 10 rows and columns initiliazed to 0 and widgest are sticky.

# connect4_button  = Button(frame1, text="Connect 4",font=("Arial",20, BOLD), padx=25, pady=25, command=partial()).grid() #place(relx=.5,rely=.3,anchor= CENTER) 
rpsls_button = Button(frame1, text="RPSLS",font=("Arial",20, BOLD), padx=25, pady=25, command=runRPSLS).grid() #place(relx=.5,rely=.4,anchor= CENTER)
# blackjack_button = Button(frame1, text="BlackJack",font=("Arial",20, BOLD), padx=25, pady=25, command=partial()).grid() #place(relx=.5,rely=.5,anchor= CENTER)
# tictactoe_button = Button(frame1, text="Tic Tac Toe",font=("Arial",20, BOLD), padx=25, pady=25, command=partial()).grid() #place(relx=.5,rely=.6,anchor= CENTER)
# wordle_button = Button(frame1, text="Wordle",font=("Arial",20, BOLD), padx=25, pady=25, command=partial()).grid() #place(relx=.5,rely=.7,anchor= CENTER) 



show_frame(frame1)



root.mainloop()