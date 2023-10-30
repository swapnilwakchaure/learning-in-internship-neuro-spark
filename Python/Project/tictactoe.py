# 1. 2 players should be able to play the game (both sitting at the same computer).
# 2. The board should be printed out every time a player make a move.
# 3. You should be able to accept user input of the player position and then place a symbol on the board.
# 4. We will use the "numpad" to match numbers to the grid on a tic tac toe board.
# ex. [1, 2, 3]
#     [4, 5, 6]
#     [7, 8, 9]
# 5. Creating your first full program is always a big leap, but you will come out the other end a much better programmer.


# def display_board(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)

# row1 = [' ',' ',' ']
# row2 = [' ',' ',' ']
# row3 = [' ',' ',' ']

# display_board(row1,row2,row3)


def user_input():
    
    choice = 'WRONG'
    acceptable_range = range(1, 10)
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input("Pick up your position: ")

        if choice.isdigit() == False:
            print('Sorry that is not a digit!')

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print('Sorry, you are out of acceptable range (1-9)')
    
    print(int(choice))


# Milestone Project 1: Walkthrough Steps Workbook
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# Some suggested tools before you get started:
# To take input from a user:

# player1 = input("Please pick a marker 'X' or 'O'")

# Note that input() takes in a string. If you need an integer value, use

# position = int(input('Please enter a number'))


# To clear the screen between moves:

# from IPython.display import clear_output
# clear_output()

# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:

# print('\n'*100)

# This scrolls the previous board up out of view. Now on to the program!




# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

def display_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(board)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():

    marker = 'WRONG'

    while marker not in ['X', 'O']:
        marker = input('Player 1: Do you want to be X or O: ')
        marker = marker.upper()

        if marker not in ['X', 'O']:
            print('Select between only X or O')
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

marker = player_input()
print('player: ',marker)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_marker(board, marker, position):
    board[position] = marker


player_marker(board, marker[0], 2)
display_board(board)

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def win_check(board, mark):
    return (
        (board[0] == mark and board[1] == mark and board[2] == mark) or # check for top row
        (board[3] == mark and board[4] == mark and board[5] == mark) or # check for middle row
        (board[6] == mark and board[7] == mark and board[8] == mark) or # check for last row
        (board[0] == mark and board[3] == mark and board[6] == mark) or # check for top column
        (board[1] == mark and board[4] == mark and board[7] == mark) or # check for middle column
        (board[2] == mark and board[5] == mark and board[8] == mark) or # check for last column
        (board[0] == mark and board[4] == mark and board[8] == mark) or # check for right diagonal
        (board[2] == mark and board[4] == mark and board[6] == mark) # check for left diagonal
    )


