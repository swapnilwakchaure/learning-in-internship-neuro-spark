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

# user_input()



# 1. mylist = [1, 2, 3]
# 2. user position = 2
# 3. user word = 'new'
# 4. output = [1, 'new', 3]
# 5. asking, do you want to play again ?
# 6. if 'yes' or 'y' then starts from step 2.

def player_position():

    position = 'WRONG'
    acceptable_range = range(1,4)
    within_range = False

    while position.isdigit() == False or within_range == False:
        position = input('Choose your position within 1, 2 or 3: ')

        if position.isdigit() == False:
            print('Sorry ! it is not a valid digit')
        
        if position.isdigit() == True:
            if int(position) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print('Please choose the position within range from 1, 2 and 3')

    return int(position)

def player_word():
    word = input('Enter your word: ')
    return word

def player_game(mylist, position, word):

    while mylist[position-1] in range(1, 4):
        position = player_position()
        word = player_word()
    
    mylist[position-1] = word
    print(mylist)

mylist = [1, 2, 3]
position = player_position()
word = player_word()

player_game(mylist, position, word)

