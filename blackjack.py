from tkinter import *
import random
from tkinter.font import BOLD, Font
from functools import partial   
from PIL import ImageTk, Image

root = Tk()
root.title("BlackJack") #sets title
root.geometry("1200x800") #sets size of window
root.rowconfigure(0, weight=1) #configures rows to a weight of 1
root.columnconfigure(0, weight=1) #configures columns to weight of 1

def show_frame(frame):
    frame.tkraise()

frame1 = Frame(root) #welcome menu frame
frame2 = Frame(root) # main gameplay frame

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky = 'nsew') #frames rows and columns initiliazed to 0 and widgets are sticky.

#frame1 code
show_frame(frame1)
frame1.configure(bg='green')
label_welcome1 = Label(frame1, text="Welcome to BlackJack!\nPress start to begin playing.",font=("Arial", 25)) #welcome label for blackjack
label_welcome1.place(relx=.5, rely=.1,anchor= CENTER)
btn_start1 = Button(frame1, text="Start", font=("Arial",50, BOLD), command=partial(show_frame,frame2), padx=20, pady=20, compound=CENTER) #start the game
btn_start1.place(relx=.5, rely=.4, anchor=CENTER)
button_quit1 = Button(frame1, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exit the program
button_quit1.place(relx=.5, rely=.7, anchor=CENTER)

#frame 2

image = Image.open('Assets/card.png')
photo = ImageTk.PhotoImage(image.resize((150, 150), Image.ANTIALIAS))

frame2.configure(bg='green')

dealer_label = Label(frame2, text="Dealer's Cards")
dealer_label.place(relx = 0.5, rely = .1, anchor=CENTER)

player_label = Label(frame2, text="Player's Cards")
player_label.place(relx = 0.5, rely = .6, anchor=CENTER)

card1_label = Label(frame2, image = photo).place(relx = .4, rely = .25, anchor=CENTER)
card2_label = Label(frame2, image = photo).place(relx = .6, rely = .25, anchor=CENTER)
card3_label = Label(frame2, image = photo).place(relx = .4, rely = .75, anchor=CENTER)
card4_label = Label(frame2, image = photo).place(relx = .6, rely = .75, anchor=CENTER)

btn_shuffle = Button(frame2, text="Shuffle Deck", font=("Helvetica", 14))
btn_shuffle.place(relx = 0.3, rely = .5, anchor=CENTER)

btn_cards = Button(frame2, text="Get Cards", font=("Helvetica", 14))
btn_cards.place(relx = 0.4, rely = .5, anchor=CENTER)

btn_hit = Button(frame2, text="Hit", font=("Helvetica", 14))
btn_hit.place(relx = 0.5, rely = .5, anchor=CENTER)

btn_split = Button(frame2, text="Split", font=("Helvetica", 14))
btn_split.place(relx = 0.6, rely = .5, anchor=CENTER)

btn_stand = Button(frame2, text="Stand", font=("Helvetica", 14))
btn_stand.place(relx = 0.7, rely = .5, anchor=CENTER)

btn_quit = Button(frame2, text="EXIT", command=partial(root.destroy)).place(relx = 0.8, rely = 0.8, anchor=CENTER)


root.mainloop()
