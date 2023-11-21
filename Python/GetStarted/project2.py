import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = { 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14 }


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.suit + ' of ' + self.rank
    
# two_hearts = Card('Hearts', 'Two')

# three_clubs = Card('clubs', 'Three')
 
# print(two_hearts.value)
# print(three_clubs.value)

# print(two_hearts.value < three_clubs.value)


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle_list(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# new_deck = Deck()
# new_deck.shuffle_list()
# my_card = new_deck.deal_one()
# print(my_card)
# print(new_deck.all_cards[-1])


class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of Multiple Card Objects
            self.all_cards.extend(new_cards)
        else:
            # For a Single Card Object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# new_player = Player('Jose')
# new_player.add_cards([my_card, my_card, my_card])
# print(new_player)






# GAME SETUP
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle_list()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# print(player_one)
# print(player_two)

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One wins!')
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    
    
    
    # while at_war:
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        
        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war.')
                print('PLAYER TWO WINS!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war.')
                print('PLAYER ONE WINS!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

