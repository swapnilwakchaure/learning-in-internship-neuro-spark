
def display_mylist(mylist):
    print('Here is the current list: ')
    print(mylist)

# display_mylist(mylist)

def position_choice():
    
    position = 'WRONG'

    while position not in ['1', '2', '3']:

        position = input('Pick a position (1, 2, 3): ')

        if position not in ['1', '2', '3']:
            print("Sorry, Invalid Choice")
    
    return int(position)-1

# position = position_choice()

def replacement_choice(mylist, position):

    user_replacement = input('Type a string to place at position: ')

    mylist[position] = user_replacement

    return mylist

# replacement_choice(mylist, position)

def gameon_choice():
    choice = 'WRONG'

    while choice not in ['Y', 'N']:
        
        choice = input("Keep playing ? ['Y', 'N']: ")
        choice = choice.upper()

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose ['Y', 'N']")
    
    if choice == 'Y':
        return True
    else:
        return False


game_on = True
game_list = [1, 2, 3]

while game_on:

    display_mylist(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_mylist(game_list)

    game_on = gameon_choice()




