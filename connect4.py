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
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky = 'nsew') #frame 1 - 10 rows and columns initiliazed to 0 and widgest are sticky.


show_frame(frame1)

count_column1 = 5
count_column2 = 5
count_column3 = 5
count_column4 = 5
count_column5 = 5
count_column6 = 5
count_column7 = 5
main_count = 0

def disable():
    global btn_column1
    global btn_column2
    global btn_column3
    global btn_column4
    global btn_column5
    global btn_column6
    global btn_column7
    btn_column1.configure(state=DISABLED)
    btn_column2.configure(state=DISABLED)
    btn_column3.configure(state=DISABLED)
    btn_column4.configure(state=DISABLED)
    btn_column5.configure(state=DISABLED)
    btn_column6.configure(state=DISABLED)
    btn_column7.configure(state=DISABLED)

def check_win(row, col):
    #check vertical
    global main_count
    global label_frame2
    if(main_count%2==1):
        label_frame2.configure(text="Player 1 place your piece")
    else:
        label_frame2.configure(text="Player 2 place your piece")
    if(row<3):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col].cget('fg')=='red' and label_ids[row+2][col].cget('fg')=='red' and label_ids[row+3][col].cget('fg')=='red' ):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col].cget('fg')=='blue' and label_ids[row+2][col].cget('fg')=='blue' and label_ids[row+3][col].cget('fg')=='blue' ):
            label_frame2.destroy()
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            disable()
    
    #check horizontal
    if(col<4):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col+1].cget('fg')=='red' and label_ids[row][col+2].cget('fg')=='red' and label_ids[row][col+3].cget('fg')=='red' ):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col+1].cget('fg')=='blue' and label_ids[row][col+2].cget('fg')=='blue' and label_ids[row][col+3].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(col>2):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col-1].cget('fg')=='red' and label_ids[row][col-2].cget('fg')=='red' and label_ids[row][col-3].cget('fg')=='red' ):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col-1].cget('fg')=='blue' and label_ids[row][col-2].cget('fg')=='blue' and label_ids[row][col-3].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(col<5 and col>0):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col+1].cget('fg')=='red' and label_ids[row][col+2].cget('fg')=='red' and label_ids[row][col-1].cget('fg')=='red' ):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col+1].cget('fg')=='blue' and label_ids[row][col+2].cget('fg')=='blue' and label_ids[row][col-1].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(col<6 and col>1):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col+1].cget('fg')=='red' and label_ids[row][col-1].cget('fg')=='red' and label_ids[row][col-2].cget('fg')=='red' ):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col+1].cget('fg')=='blue' and label_ids[row][col-1].cget('fg')=='blue' and label_ids[row][col-2].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    
    #check diagonal
    if(row<3 and col<4):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col+1].cget('fg')=='red' and label_ids[row+2][col+2].cget('fg')=='red' and label_ids[row+3][col+3].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col+1].cget('fg')=='blue' and label_ids[row+2][col+2].cget('fg')=='blue' and label_ids[row+3][col+3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(row>2 and col>2):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col-1].cget('fg')=='red' and label_ids[row-2][col-2].cget('fg')=='red' and label_ids[row-3][col-3].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col-1].cget('fg')=='blue' and label_ids[row-2][col-2].cget('fg')=='blue' and label_ids[row-3][col-3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(row>2 and col<4):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col+1].cget('fg')=='red' and label_ids[row-2][col+2].cget('fg')=='red' and label_ids[row-3][col+3].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col+1].cget('fg')=='blue' and label_ids[row-2][col+2].cget('fg')=='blue' and label_ids[row-3][col+3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(row>0 and row<4 and col<5 and col>1):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col+1].cget('fg')=='red' and label_ids[row+1][col-1].cget('fg')=='red' and label_ids[row+2][col-2].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col+1].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue' and label_ids[row+2][col-2].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(row>1 and row<5 and col<4 and col>0):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col+1].cget('fg')=='red' and label_ids[row-2][col+2].cget('fg')=='red' and label_ids[row+1][col-1].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col+1].cget('fg')=='blue' and label_ids[row-2][col+2].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()  
            disable() 
    if(row<3 and col>2 ):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col-1].cget('fg')=='red' and label_ids[row+2][col-2].cget('fg')=='red' and label_ids[row+3][col-3].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue' and label_ids[row+2][col-2].cget('fg')=='blue' and label_ids[row+3][col-3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(row<4 and row>0 and col>0 and col<5 ):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col+1].cget('fg')=='red' and label_ids[row+2][col+2].cget('fg')=='red' and label_ids[row-1][col-1].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue' and label_ids[row+2][col+2].cget('fg')=='blue' and label_ids[row-1][col-1].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()
    if(row<5 and row>1 and col>1 and col<6 ):
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col+1].cget('fg')=='red' and label_ids[row-1][col-1].cget('fg')=='red' and label_ids[row-2][col-2].cget('fg')=='red'):
            label_frame2.destroy()
            win_frame.grid(row=0, column=0)
            disable()
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue' and label_ids[row-1][col-1].cget('fg')=='blue' and label_ids[row-2][col-2].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")
            win_frame.grid(row=0, column=0)
            label_frame2.destroy()
            disable()

def counting_column(column):
    global count_column1
    global count_column2
    global count_column3
    global count_column4
    global count_column5
    global count_column6
    global count_column7
    global label_ids
    global main_count
    if(column==0):
        if(main_count%2==0):
            label_ids[count_column1][0].configure(fg='red')
        else:
            label_ids[count_column1][0].configure(fg='blue')
        check_win(count_column1, 0)
        count_column1 = count_column1 - 1
    elif(column==1):
        if(main_count%2==0):
            label_ids[count_column2][1].configure(fg='red')
        else:
            label_ids[count_column2][1].configure(fg='blue')
        check_win(count_column2, 1)
        count_column2 = count_column2 - 1
    elif(column==2):
        if(main_count%2==0):
            label_ids[count_column3][2].configure(fg='red')
        else:
            label_ids[count_column3][2].configure(fg='blue')
        check_win(count_column3, 2)
        count_column3 = count_column3 - 1
    elif(column==3):
        if(main_count%2==0):
            label_ids[count_column4][3].configure(fg='red')
        else:
            label_ids[count_column4][3].configure(fg='blue')
        check_win(count_column4, 3)
        count_column4 = count_column4 - 1
    elif(column==4):
        if(main_count%2==0):
            label_ids[count_column5][4].configure(fg='red')
        else:
            label_ids[count_column5][4].configure(fg='blue')
        check_win(count_column5, 4)
        count_column5 = count_column5 - 1
    elif(column==5):
        if(main_count%2==0):
            label_ids[count_column6][5].configure(fg='red')
        else:
            label_ids[count_column6][5].configure(fg='blue')
        check_win(count_column6, 5)
        count_column6 = count_column6 - 1
    elif(column==6):
        if(main_count%2==0):
            label_ids[count_column7][6].configure(fg='red')
        else:
            label_ids[count_column7][6].configure(fg='blue')
        check_win(count_column7, 6)
        count_column7 = count_column7 - 1
    main_count = main_count + 1
    

def enable_player1(column):
    global btn_column1
    global btn_column2
    global btn_column3
    global btn_column4
    global btn_column5
    global btn_column6
    global btn_column7
    global label_frame2
    global count_column1
    global count_column2
    global count_column3
    global count_column4
    global count_column5
    global count_column6
    global count_column7
    global main_count
    counting_column(column)
    if(count_column1<0):
        btn_column1.configure(state=DISABLED)
    if(count_column2<0):
        btn_column2.configure(state=DISABLED)
    if(count_column3<0):
        btn_column3.configure(state=DISABLED)
    if(count_column4<0):
        btn_column4.configure(state=DISABLED)
    if(count_column5<0):
        btn_column5.configure(state=DISABLED)
    if(count_column6<0):
        btn_column6.configure(state=DISABLED)
    if(count_column7<0):
        btn_column7.configure(state=DISABLED)


btn_column1 = Button(frame2, text = 'Column 1', command=partial(enable_player1, 0), padx=5,pady=5)
btn_column1.grid(row=3, column = 1)
btn_column2 = Button(frame2, text = 'Column 2', command=partial(enable_player1, 1), padx=5,pady=5)
btn_column2.grid(row=3, column=2)
btn_column3 = Button(frame2, text = 'Column 3', command=partial(enable_player1, 2), padx=5,pady=5)
btn_column3.grid(row=3, column=3)
btn_column4 = Button(frame2, text = 'Column 4', command=partial(enable_player1, 3), padx=5,pady=5)
btn_column4.grid(row=3, column=4)
btn_column5 = Button(frame2, text = 'Column 5', command=partial(enable_player1, 4), padx=5,pady=5)
btn_column5.grid(row=3, column=5)
btn_column6 = Button(frame2, text = 'Column 6', command=partial(enable_player1, 5), padx=5,pady=5)
btn_column6.grid(row=3, column=6)
btn_column7 = Button(frame2, text = 'Column 7', command=partial(enable_player1, 6), padx=5,pady=5)
btn_column7.grid(row=3, column=7)

label_frame1 = Label(frame1, text="Connect 4!\nPress start to begin playing.",font=("Arial", 25)) 
label_frame1.place(relx=.5, rely=.1,anchor= CENTER)
btn_frame1 = Button(frame1, text="Start", font=("Arial",50, BOLD), command=partial(show_frame,frame2), padx=20,pady=20, compound=CENTER) #Big button to start the game
btn_frame1.place(relx=.5, rely=.5, anchor=CENTER)
button_quit_game = Button(frame1, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the program
button_quit_game.place(relx=.5, rely=.9, anchor=CENTER)


label_frame2 = Label(frame2, text="Player 1 place your piece", font=('Helvatical bold',30))
label_frame2.grid(row=0, column=0)
button_quit_game = Button(frame2, text="Press to Quit" , command=root.destroy).grid(row=0, column=40) #press to quit button, closes program

w, h = 7, 6
label_ids = [[0 for x in range(w)] for y in range(h)] 

for i in range(6):
    for j in range(7):
        game_board = Label(frame2, text="O", fg='black', font=('Helvatical bold',50), padx=10,pady=10)
        game_board.grid(row=4+i, column=j+1)
        label_ids[i][j] = game_board

win_frame = Label(frame2, text="Player 1 wins!!!", font=('Helvatical bold',50))

root.mainloop()