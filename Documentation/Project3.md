#### Estimation of Person-Hours/Accounted Person-Hours: 
https://docs.google.com/spreadsheets/d/1lUsOUC2fbRDljCjvxWwighowklgWpwoVV_gzfDf-2TM/edit?usp=sharing

# Our Project: Game Suite
We are developing a game suite, stocked with 5 fun and exciting games to play:
 - BlackJack 
 - Connect 4 
 - Tic-Tac-Toe 
 - Wordle 
 - Rock Paper Scissors Lizard Spock 

### BlackJack
Blackjack is a casino banking game that uses a 52 card deck with the objective of the game for the player or dealer to be dealt a hand with a value of no more than 21. Highest hand wins the round. Rules on how to play are below:

<img src="blackjack_rules.png" width="400" height="600"/>

### Connect 4
Two player game where each player has a set of colored tokens that they will take turns placing on a 6 by 7 playing board. Tokens are placed one by one in any available column and will drop down to the lowest available row. Play continues until a player gets four of their tokens in a row or a stalemate occurs. Four in a row vertical, horizontal, or diagonal are all valid ways to win.

<img src="connect4.png" width="300" height="300"/>

### Tic-Tac-Toe
A two player game where each player takes turns marking spaces in a three-by-three grid with X's or O's. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

### Wordle
A one player game where the player has six tries to guess a certain 5-letter word. All the hints they have are given by other guesses, according to these rules:

<img src = "https://i.inews.co.uk/content/uploads/2022/01/PRI_217279117.jpg" height = 300px />


### Rock Paper Scissors Lizard Spock
A spin on the classic "rock paper scissors", "Rock Paper Scissors Lizard Spock" is a more complex twist on the game adapted from the TV show "The Big Bang Theory". The Rules for what wins against what is nicely illustrated with the following image:

<img src="RPSLS_rules.png" alt="Rules for Rock Paper Scissors Lizard Spock" width="500"/>

# Further Documentation

### Story Point Estimation

| 1 | 2 | 3 | 5 | 8 | 13 | 
| :-- | :-- | :-- | :-- | :-- | :-- | 
|Importing Project|Creating minigame classes |Maintaining consistent Python + Tkinter versions|RPSLS prototype|Connect 4 prototype|UML Diagram for Project 3|
|Dividing tasks|Barebones code for minigames|Merging code|Tic-Tac-Toe prototype|Wordle prototype|Design Paradigm|
|Determining projected hours|Linking minigames to menu screen|creating game ideas + functionality|BlackJack prototype|Software Architecture|Project Design Pattern|

#### Reasoning for estimation:
- We set each story point to have a time value of 20 minutes
- Since project 3 is just prototyping, we knew that the overall hours necessary to complete would be significantly lower, and that the heavy lifting would come into play during Project 4, where we will be fully implementing and polishing our games
- Overall, the documentation for Project 3 actually should take longer than the code, since we want to be very specific on the specifications for our finished Project before development goes into full swing (i.e. when Project 4 begins)


### Design Paradigms

Out of the four design paradigms, the one most applicable to our project is the object-oriented paradigm. 

We are creating a suite of games: RPSLS (Rock-Paper-Scissors-Lizard-Spock, an extension of the classic Rock-Paper-Scissors developed in the show _The Big Bang Theory_ to decrease the likelihood of ties), Blackjack, Tic-Tac-Toe, Connect 4, and Wordle. 

Class design normally associated with object-oriented design (i.e classes with methods and attributes) can be seen in each of our games; for example, in Blackjack, we have the Card class. Each Card object has a rank and suit attribute to represent the type of card it is (e.g. the Ace of Spades card has the rank Ace and the suit Spaces). In each game of Blackjack, 52 Card objects are created to represent a full deck of cards. There is also a Deck class, which holds all 52 Cards and has class methods such as shuffle(), which puts its cards into a random order. 

Additionally, in RPSLS, there is a class representing each possible move a player can throw, each with attributes of what other move it beats and what it is beaten by (e.g. Scissor beats Paper and Lizard and is beaten by Spock and Rock). 

This sort of structure follows in our other games, which will be fully documented and described by Project 4. Because our project doesn’t follow



* function-oriented design (there is not a focus on data to transform with a series of functions), 
* aspect-oriented design (we do not implement interpreters that separate and identify the code based on cross-cutting concerns), or 
* data-structured centered design (there is no central database which we modify),

The design paradigm most applicable to our project is the object-oriented paradigm. 

### Project Design Patterns

One design pattern we used in our design was the ‘bridge’, which falls under the structural design patterns. For project 3, we created a suite of games, and each member of our team had their own game to write. 

The way all of our games were connected was through a main menu window which would pop up initially when the user runs our program. We wrote the functionality for the main menu so when a certain game was selected, that specific game would open to begin playing. We created the main menu so that its functionality was completely separate from the rest of our code in the sense that any new improvements to a specific game would not change how the main menu would work. 

Another design pattern used was the ‘iterator’ which falls under the behavioral design patterns. A specific example of where this design pattern was used was in the connect 4 game. The game board has 7 columns and 6 rows. Instead of creating 42 different labels on the screen an iterator was used to create these labels via a nested for loop. Each label then has their own specific ID so as the user plays the game the ID’s are updated and visually changed on the screen. 

Another design pattern used was the ‘state’ which also falls under the behavioral design patterns. A specific example of this design pattern is how the state of buttons change based on the user's actions. For example, player 1 can not move on to player 2’s turn until they have completed their turn. The ‘next’ button is disabled until player 1 completes their turn, then the ‘next’ button changes states and becomes enabled. 

### Software Architecture

The Software Architecture we used for Project 3 was the Event Driven Architecture. Our program uses the tkinter framework, which is even driven through button clicks to perform actions such as changing colors/images/letters, dealing cards, etc. 

For example, in our main menu, the user is faced with 5 buttons, each corresponding to one of the games we have provided. When the user clicks a button, the corresponding game starts up. Each game also is event-driven, as described: 

**Blackjack:** During play, the player is given a card. Then, they will either click the button for "Hit", "Stand", "Split", or "Double Down", each with their own corresponding actions (be dealt a card, stay with their current hand, split their deck, or up the bet). When both the player and dealer choose “Stand”, the player with 21 or highest value hand under 21 will win. 

**Connect Four:** Starts off with seven columns of six buttons. When each player clicks a button, it changes to their respective colored disks. On the event that a player gets four in a row or a diagonal with their disks, they will win the game.

**Rock Paper Scissors Lizard Spock**: The players are given five options for this version of the game. Each choice has a corresponding button, and on the event when both players have clicked an option, their choices will be checked for a winning "Hand Shape", and that person will win the game.

**Tic Tac Toe:** This game is a three by three grid of buttons, and when each player clicks a button, either an X or O will mark their button press. When an X or O is three in a row or diagonal, that player wins the game.

**Wordle:** During play, player guesses five-letter words, when they press the confirmation button, they fire an event which causes squares on the game screen to change color depending on the game rules. The player keeps guessing until they guess the word correctly or they run out of guesses. 

### UML Diagram
<img src = "uml diagram.png" />
