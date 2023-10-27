# Three Cup Monte Game

import random

# mylist = [1,2,3,4,5]
# random.shuffle(mylist)
# print(mylist)


# it shuffles the list
def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist

# it takes the input number from player
def player_guess():
    guess = ''
    while guess not in ['1','2','3']:
        guess = input('Pick a number from 1,2 or 3: ')
    return int(guess)

# it checkes player guess is correct or not
def check_guess(mylist,guess):
    if mylist[guess-1] == 'O':
        print("Correct !")
    else:
        print("Wrong Guess !")
    print(mylist)


# INITIAL LIST
mylist = [' ', 'O', ' ']

# SHUFFLE LIST
mylist = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mylist, guess)
