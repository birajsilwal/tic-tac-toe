import random


BOARD = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
GAME_IS_RUNNING = True
WINNER = None
CURRENT_PLAYER = 'X'
got_winner = False


# display the board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print('----------')
    print(board[3] + " | " + board[4] + " | " + board[5])
    print('----------')
    print(board[6] + " | " + board[7] + " | " + board[8])


# take user input and update board value
def take_input(board):
    user_input = int(input("Enter value from 1-9: "))
    board[user_input - 1] = CURRENT_PLAYER


# check row
def check_row(board):
    global WINNER
    if board[0] != '-' and board[0] == board[1] == board[2]:
        WINNER = board[0]
    elif board[3] != '-' and board[3] == board[4] == board[5]:
        WINNER = board[3]
    elif board[6] != '-' and board[6] == board[7] == board[8]:
        WINNER = board[7]
    # if there is a winner return true 
    if WINNER is not None:
        return True
            
            
# check column
def check_col(board):
    global WINNER
    if board[0] != '-' and board[0] == board[3] == board[6]:
        WINNER = board[0]
    elif board[1] != '-' and board[1] == board[4] == board[7]:
        WINNER = board[1]
    elif board[2] != '-' and board[2] == board[5] == board[8]:
        WINNER = board[2]
    # if there is a winner return true 
    if WINNER is not None:
        return True
    
    
# check diagonal
def check_diag(board):
    global WINNER
    if board[0] != '-' and board[0] == board[4] == board[8]:
        WINNER = board[0]
        return True
    elif board[6] != '-' and board[6] == board[4] == board[2]:
        WINNER = board[6]
        return True
    
    
# check tie
def check_tie(board):
    global GAME_IS_RUNNING
    if '-' not in board:
        print("*******") 
        print("Tie.") 
        display_board(board)
        GAME_IS_RUNNING = False


# check for winner
def check_winner(board):
    global GAME_IS_RUNNING
    global got_winner
    if check_row(board) or check_col(board) or check_diag(board):
        print("*******")
        print('Winner is ' + CURRENT_PLAYER) 
        display_board(board)
        GAME_IS_RUNNING = False
        got_winner = True


# switch user
def switch_user():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == 'X':
        CURRENT_PLAYER = 'O'
    else: 
        CURRENT_PLAYER = 'X'
        

# computer's turn
def computer_player(board):
    while CURRENT_PLAYER == 'O':
        num = random.randint(0, 8)
        if board[num] == '-':
            board[num] = 'O'
            switch_user()  # switch to human, this must be here to get out of while loop
        
        
# play game
def play():
    global GAME_IS_RUNNING
    global BOARD
    global  WINNER
    global got_winner
    while GAME_IS_RUNNING:    
        display_board(BOARD)
        
        if not got_winner:
            take_input(BOARD) # take input from user
            check_winner(BOARD)
            check_tie(BOARD)
            switch_user()  # switch to computer
            
        if not got_winner:
            computer_player(BOARD)
            check_winner(BOARD)
            check_tie(BOARD)
        

if __name__ == '__main__':
    print("Let's begin the game!\n")
    play()
