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

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def place_marker(board, marker, position):
    board[position] = marker

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

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return x a string of which player went first.

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for i in range(0, 9):
        if space_check(board, i):
            return False
    return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose your next position from (1-9): '))
    return position-1

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    return input('Do you want to play again ? Yes or No: ').lower().startswith('y')

# tep 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

# 1. display_board(board)
# 2. marker1, marker2 = player_input() => (X, O) or (O, X)
# 3. place_marker(board,marker,position)
# 4. win_check(board, marker)
# 5. choose_first()
# 6. space_check(board, position)
# 7. full_board_check(board)
# 8. player_choice(board)
# 9. replay()

print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player 1 turn
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations ! Player 1 won the game')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 2'
        
        else:
            # Player 2 turn

            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations ! Player 2 won the game')
                break
            else:
                turn = 'Player 1'

    if not replay():
        break

