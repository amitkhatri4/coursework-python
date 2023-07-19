import random
import os.path
import json
random.seed()

board=['-' for x in range(9)] #creates list named board with 9 elements
player= "X"
computer= "O"  #x for player and 0 for computer 

def draw_board(board):
        print(" -------------")
        print(" |",board[0],"|",board[1],"|",board[2],"|")
        print(" -------------")
        print(" |",board[3],"|",board[4],"|",board[5],"|")
        print(" -------------")
        print(" |",board[6],"|",board[7],"|",board[8],"|")     #print horizontal line to seperate rows and coloumn
        print(" -------------")
        pass ##noting to do with code but is a place holder indicate that there is additional code in this function
    
    
def welcome(board):
    print('''Welcome to the Noughts and Crosses game!! #greeting and welcome function for user
Hope you enjoy it :) 
''')
    print("Given below is the board layout: ")
    draw_board(board)          #call to print current state of the of the board 
    print("")
    print("You can enter the number correspoding to square you want when prompted \n")

    
def initialise_board(board):
    for x in range(9):
            board[x]=" "
    return board


def get_player_move(board):
    try: #handle potential exceptions that may occur during execution of the code 
        move=int(input(''' Choose the number where you want to place X in the board: #
    1  2  3
    4  5  6
    7  8  9     
: ''')) #allow player to choose a move by entering a number representing the position on the board where they want to place their mark
    except ValueError:      
        print("Invalid Input, Try again!")
        get_player_move(board)  
    except:
        print("Invalid Input, Try again!")
        get_player_move(board) 
    move=move-1
    if board[move]==" ":
             board[move]=player
             draw_board(board)
    else:            
            print("The cell is occupied")
            return get_player_move(board)


def choose_computer_move(board): #board parameter represents the current state of the tic-tac-toe board.
        possibleMoves=[x for x, letter in enumerate(board) if letter==' ' ] #It iterates over each element letter and its corresponding index x in the board list.    
        move=random.choice(possibleMoves) #represents the position where the computer will make its move.
        board[move]=computer
        print("Its computers turn: ")
        import time
        time.sleep(1) #time module and adds a delay of 1 second using time.sleep(1) to create a pause before displaying the updated state 
        draw_board(board)

def check_for_win(board,mark):
        if board[0]==mark and board[1]==mark and board[2]==mark:
                return True
        elif board[0]==mark and board[3]==mark and board[6]==mark:
                return True
        elif board[0]==mark and board[4]==mark and board[8]==mark:
                return True
        elif board[1]==mark and board[4]==mark and board[7]==mark:
                return True
        elif board[2]==mark and board[5]==mark and board[8]==mark:
                return True
        elif board[3]==mark and board[4]==mark and board[5]==mark:
                return True
        elif board[6]==mark and board[7]==mark and board[8]==mark:
                return True
        elif board[2]==mark and board[4]==mark and board[6]==mark:
                return True
        else:              
                return False

def check_for_draw(board):
        for x in range(9):
                if board[x]==" ": #it checks if the element at the current index (x) of the board is an empty space character (" ").
                        return False            
        return True #The function returns True for a draw and False otherwise, indicating the outcome of the game.
                

                
def play_game(board):
        board=initialise_board(board) #initialise_board function, which sets up the initial state of the tic-tac-toe board.
        draw_board(board)       
        while True: #game continues until one of the return statements is executed within the loop.
                get_player_move(board)
                if check_for_win(board,"X"):
                        return 1 #If the player has won, the function returns 1, indicating a win.
                if check_for_draw(board):
                        return 0 #if  there are no more moves and no winner, the function returns 0.
                choose_computer_move(board)
                if check_for_win(board,"O"):
                        return -1 #If the computer has won, the function returns -1, indicating a win.
                if check_for_draw(board):
                        return 0 #If the game is a draw, the function returns 0.
def menu():
        print("------Menu------")
        choice=input(''' Enter one of the following options:
 1 - Play the game
 2 - Save your score in the leaderboard
 3 - Load and display the Leaderboard
 q - End the program

 : ''')
        return choice

def load_scores(): #function named load_scores that doesn't take any parameters.
        lboard={} #This line creates an empty dictionary named lboard. 
        with open("leaderboard.txt","r") as f: #This line opens the file named "leaderboard.txt" in read mode ("r") using a file object f. 
                for line in f: #read each line of file
                        (key, values)= line.split() #line splits each line of the file into two parts: key and values. 
                        lboard[key]=values
        return lboard  #returns the populated lboard dictionary back to the caller of the load_scores function.

def save_score(score): #defines a function called save_score that takes a parameter called score
        player_name=input("Enter your name: ") #prompts the user to enter their name using the input() function and stores it in the variable player_name.
        with open("leaderboard.txt","w") as f: #opens the file "leaderboard.txt" in "append" mode using the open() function with the "a" argument. 
                f.write(player_name+" "+str(score)+"\n") #creates a new line in the file with the player's name and score.
        return 

def display_leaderboard(lboard): #line defines a function named display_leaderboard that takes one parameter: lboard
        print("\n\t---*Leaderboard*---\n")
        print("\tName\t\tScore")
        print("\t-----\t\t-----") #lines print the header or title of the leaderboard in a formatted manner
        for name, score in lboard.items():
                print(f"name:{name}, {score}") #These lines iterate over each key-value pair in the lboard dictionary using the items() method.



              
                
        
        


        

   
        
        
    


    



    
    
    
    


           
    


