from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial

def show_frame(frame): #raises a frame when called
    frame.tkraise()


root = Tk()
#root.state('zoomed') #puts the window mode in zoomed
root.title('Wordle') #labels our frame

root.rowconfigure(0, weight=1) #configures rows to a weight of 1
root.columnconfigure(0, weight=1) #configures columns to weight of 1
root.geometry("450x800")
root.configure(bg="#1F2937")

wordle_start = Frame(root, width=450, height=800, bg="#1F2937")
wordle_start.grid(row=0, column=0, sticky = 'nsew')

#header = Frame(root, width=450, height=100, bg="#111827")
#header.grid(row=0, column=0, sticky = 'nsew')
#body = Frame(root, width=450, height=700, bg="#1F2937")
#body.grid(row=0, column=0, sticky = 'nsew')

myLabel1 = Label(wordle_start, 
                 text="Wordle",
                 bg="#111827",
                 fg="white",
                 font=("Segoe UI Semibold", 25)).place(relx=.5, rely=.1,anchor= CENTER)

frame1_button = Button(wordle_start, 
                       text="Start",
                       font=("Segoe UI Semibold",20, BOLD), 
                       #command=partial(show_frame,frame2), 
                       fg="white", 
                       bg="#111827", 
                       padx=20,pady=20, 
                       #image=img_start,
                       compound=CENTER).place(relx=.50, rely=.5,anchor= CENTER)

show_frame(wordle_start)
#show_frame(header)
#show_frame(body)


root.mainloop()
