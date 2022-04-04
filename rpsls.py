from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial   
from PIL import ImageTk, Image

### GLOBAL VARIABLES
choice_player = ""
choice_ai = "Victory" 
result = "You lose!" 
###

def show_frame(frame):
    frame.tkraise()

def set_playerChoice(choice): #sets player's choice as the passed-in string
    print("Here!")
    global choice_player
    choice_player = choice

    #prep for frame 3
    frame3_txt1 = Label(frame3, text="You picked...\n" + choice_player,font=("Arial", 25))
    frame3_txt1.place(relx=.5, rely=.1,anchor= CENTER)

    frame3_txt2 = Label(frame3, text="Enemy picked...\n" + choice_ai,font=("Arial", 25))
    frame3_txt2.place(relx=.5, rely=.3,anchor= CENTER)

    frame3_txt3 = Label(frame3, text= result,font=("Arial", 40))
    frame3_txt3.place(relx=.5, rely=.5,anchor= CENTER)

    show_frame(frame3)# now skip to frame 3

root = Tk()
root.state('zoomed') #puts the window mode in zoomed
root.title("Rock Paper Scissors Lizard Spock") #labels our frame

root.rowconfigure(0, weight=1) #configures rows to a weight of 1
root.columnconfigure(0, weight=1) #configures columns to weight of 1


#Initialize start image for use

image=Image.open("assets/rpsls/start.jpeg") 
#img=image.resize((40,40))
img_start=ImageTk.PhotoImage(image) #image for just the start button

frame1 = Frame(root) #welcome menu frame
frame2 = Frame(root) # player pick screen
frame3 = Frame(root) # result screen

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky = 'nsew') #frames' rows and columns initiliazed to 0 and widgets are sticky.


show_frame(frame1)

#frame1 code
frame1_welcomeTxt = Label(frame1, text="Rock Paper Scissors Lizard Spock!\nPress start to begin playing.",font=("Arial", 25)) #welcome text 
frame1_welcomeTxt.place(relx=.5, rely=.1,anchor= CENTER)


frame1_startBtn = Button(frame1, text="Start",fg="white", font=("Arial",50, BOLD), command=partial(show_frame,frame2), bg="white", padx=20,pady=20, image=img_start, compound=CENTER) #Big button to start the game
frame1_startBtn.place(relx=.5, rely=.5, anchor=CENTER)

#frame1 quit button
frame1_exitBtn = Button(frame1, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the program
frame1_exitBtn.place(relx=.5, rely=.9, anchor=CENTER)


#frame2 code
frame2_txt = Label(frame2, text="What will you throw?",font=("Arial", 25))
frame2_txt.grid(rowspan=2, columnspan=4) #place(relx=.5, rely=.2, anchor=CENTER)

frame2_rockBtn = Button(frame2, text="ROCK",font=("Arial",40, BOLD), command=partial(set_playerChoice, "Rock")) #player chooses rock
frame2_rockBtn.place(relx=.5, rely=.2, anchor=CENTER)

frame2_paperBtn = Button(frame2, text="PAPER",font=("Arial",40, BOLD), command=partial(set_playerChoice, "Paper")) #player chooses paper
frame2_paperBtn.place(relx=.5, rely=.3, anchor=CENTER)

frame2_scissorsBtn = Button(frame2, text="SCISSORS",font=("Arial",40, BOLD), command=partial(set_playerChoice, "Scissors")) #player chooses scissors
frame2_scissorsBtn.place(relx=.5, rely=.4, anchor=CENTER)

frame2_lizardBtn = Button(frame2, text="LIZARD",font=("Arial",40, BOLD), command=partial(set_playerChoice, "Lizard")) #player chooses lizard
frame2_lizardBtn.place(relx=.5, rely=.5, anchor=CENTER)

frame2_spockBtn = Button(frame2, text="SPOCK",font=("Arial",40, BOLD), command=partial(set_playerChoice, "Spock")) #player chooses spock
frame2_spockBtn.place(relx=.5, rely=.6, anchor=CENTER)

#frame2 quit button
frame2_exitBtn = Button(frame2, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the program
frame2_exitBtn.place(relx=.5, rely=.9, anchor=CENTER)

#frame3 code (most of it is within a function)



#frame3 play again button
frame2_replayBtn = Button(frame3, text="Play Again",font=("Arial",30, BOLD), command=partial(show_frame, frame1)) #replays the game for the player
frame2_replayBtn.place(relx=.5, rely=.8, anchor=CENTER)

#frame3 quit button
frame2_exitBtn = Button(frame3, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the game, thus goes back to the game suite menu
frame2_exitBtn.place(relx=.5, rely=.9, anchor=CENTER)

root.mainloop() #keeps game running, part of basic Tkinter structure
