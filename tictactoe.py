
from cgitb import text
from distutils import command
from email import message
from functools import partial
from glob import glob
from itertools import count
from pickle import GLOBAL
from tkinter import *
import tkinter as tk
from tkinter import messagebox


count = 0
player = ' '
player1Score = 0
player2Score = 0

def playGame( ):
    gameWindow = Toplevel()
    gameWindow.title("Tic-Tac-Toe")
    gameWindow.geometry("400x400")

    global count, player1Score, player2Score
    count=0
    player1Score = 0 
    player2Score = 0
    
    ##print(count)

    def button_click(passedButton):
        global count, player1Score, player2Score, player
        count = count+1
       
        
        

        if(count%2==0): ##Player 2
            player = "Player 2"
            print("Player 2: ", player2Score)
            tempPlayer2Score = int(passedButton.cget('text')) ##Keeps track of score
            player2Score = player2Score + tempPlayer2Score
            if(player2Score == 15):
                player2Score = 0
                response = messagebox.askquestion(player, player + " Won. \n Play Again?")
                if(response == "yes"):
                    gameWindow.destroy()
                    playGame()
                elif(response == "no"):
                    gameWindow.destroy()
            passedButton.config(text = "X", fg='red', state = "disable")
            passedButton.config(text = "X", disabledforeground='red', state = "disable")
            
        else: #Player 1
            player = "Player 1"
            print("Player 1: ", player1Score)
            tempPlayer1Score = int(passedButton.cget('text')) ##Keeps track of score
            player1Score = player1Score + tempPlayer1Score
            if(player1Score == 15):
                player1Score = 0
                response = messagebox.askquestion(player, player + " Won. \n Play Again?")
                if(response == "yes"):
                    gameWindow.destroy()
                    playGame()
                elif(response == "no"):
                    gameWindow.destroy()
            passedButton.config(text = "O", fg='blue', state = "disable")
            passedButton.config(text = "O", disabledforeground='blue', state = "disable")

        

    ##Buttons
    button_1 = Button(gameWindow, text="4", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_1))
    button_1.grid(row=3, column=0)
    button_2 = Button(gameWindow, text="3", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_2))
    button_2.grid(row=3, column=1)
    button_3 = Button(gameWindow, text="8", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_3))
    button_3.grid(row=3, column=2)
    button_4 = Button(gameWindow, text="9", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_4))
    button_4.grid(row=2, column=0)
    button_5 = Button(gameWindow, text="5", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_5))
    button_5.grid(row=2, column=1)
    button_6 = Button(gameWindow, text="1", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_6))
    button_6.grid(row=2, column=2)
    button_7 = Button(gameWindow, text="2", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_7))
    button_7.grid(row=1, column=0)
    button_8 = Button(gameWindow, text="7", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_8))
    button_8.grid(row=1, column=1)
    button_9 = Button(gameWindow, text="6", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_9))
    button_9.grid(row=1, column=2)
    button_close = Button(gameWindow, text="Exit Game", command=gameWindow.destroy)
    button_close.grid(row=4, column=2)
    gameInfo = Label(gameWindow, text="Game by Group 11 \n Player 1: 'O' \nPlayer 2: X")
    gameInfo.grid(row=5, column= 0)
    
    

