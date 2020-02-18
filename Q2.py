import random
# Game Board
board=[0,1,2,3,4,5,6,7,8]
board_input=["","","","","O","","","",""]
def show():
    print("\n",board_input[0],"|",board_input[1],"|",board_input[2],"\n ---------- \n",board_input[3],"|",board_input[4],"|",board_input[5],"\n ---------- \n",board_input[6],"|",board_input[7],"|",board_input[8])

#Displaying Inputs
print("\t ### Tic-Tac-Toe ### \n You are Playing as X \n Enter the respective number for position of X")    
print("\n",board[0],"|",board[1],"|",board[2],"\n ---------- \n",board[3],"|",board[4],"|",board[5],"\n ---------- \n",board[6],"|",board[7],"|",board[8])

#Taking Input from Player
for i in range(4):
    player=int(input("Play your turn-->"))
    if player not in range(0,9):
        print("INVALID INPUT")
    elif player==4 :
        print("Already Occupied")
        continue
    opponent=random.randrange(0,9,1)                                   #Input from Computer
    if opponent==player :
        pass
    elif opponent==4 :
        pass
        continue
    board_input[player]="X"
    board_input[opponent]="O"
    show()

#Conditions for Winning and Losing
    if board_input[0]==board_input[1]==board_input[2]=="X":
        print("You Won the Game")
        break
    elif board_input[6]==board_input[7]==board_input[8]=="X":
        print("You Won the Game")
        break
    elif board_input[0]==board_input[3]==board_input[6]=="X":
        print("You Won the Game")
        break
    elif board_input[2]==board_input[5]==board_input[8]=="X":
        print("You Won the Game")
        break
    elif board_input[0]==board_input[1]==board_input[2]=="O":
        print("You Lost the Game")
        break
    elif board_input[6]==board_input[7]==board_input[8]=="O":
        print("You Lost the Game")
        break
    elif board_input[0]==board_input[3]==board_input[6]=="O":
        print("You Lost the Game")
        break
    elif board_input[2]==board_input[5]==board_input[8]=="O":
        print("You Lost the Game")
        break
    elif board_input[0]==board_input[4]==board_input[8]=="O":
        print("You Lost the Game")
        break
    elif board_input[2]==board_input[4]==board_input[6]=="O":
        print("You Lost the Game")
        break
    elif board_input[1]==board_input[4]==board_input[7]=="O":
        print("You Lost the Game")
        break
    elif board_input[3]==board_input[4]==board_input[5]=="O":
        print("You Lost the Game")
        break
