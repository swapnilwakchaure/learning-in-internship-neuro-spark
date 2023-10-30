# Milestone Project 1: Walkthrough Steps Workbook

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

def display_board(board):
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():

    marker = ''

    while marker not in ['X', 'O']:
        marker = input('Player 1: Do you want to be X or O: ')
        marker = marker.upper()

        if marker not in ['X', 'O']:
            print('Sorry, Invalid Input, Please Try Again')
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def win_check(board, mark):
    return (
        (board[0] == mark and board[1] == mark and board[2] == mark) or # for first row
        (board[3] == mark and board[4] == mark and board[5] == mark) or # for middle row
        (board[6] == mark and board[7] == mark and board[8] == mark) or # for last row
        (board[0] == mark and board[3] == mark and board[6] == mark) or # for first column
        (board[1] == mark and board[4] == mark and board[7] == mark) or # for middle column
        (board[2] == mark and board[5] == mark and board[8] == mark) or # for last column
        (board[0] == mark and board[4] == mark and board[8] == mark) or # for right diagonal
        (board[2] == mark and board[4] == mark and board[6] == mark) # for left diagonal
        )

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

import random

def choose_first():
    if random.ranint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for i in range(0, 9):
        if space_check(board, i):
            return False
    # IF BOARD IS FULL, THEN WE RETURN TRUE
    return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    
    position = 'WRONG'

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9): '))
    
    return position

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    pass

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

# 1. display_board(board)
# 2. player_input()
# 3. place_marker(board, marker, position)
# 4. win_check(board, mark)
# 5. choose_first()
# 6. space_check(board, position)
# 7. full_board_check(board)
# 8. player_choice(board)
# 9. replay()

print('Welcome to Tic Tac Toe')

board = ['X']*9
display_board(board)

