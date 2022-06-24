import random
import pdb

# Global variables:
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Dictionary:
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# Single Card Class ===========================================
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # Gives integer:
        self.value = values[rank]
    
    # What do I want to return when I make an instance?
    def __str__(self):
        return self.rank + " of " + self.suit


# Deck Class ===================================================
# Using a class within another class
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()


# Player Class ===================================================
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # if you are adding multiple new cards:
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            # if you are adding single new card:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# War Game Logic =================================================
player_one = Player("One")
player_two = Player("Two")


# Setup New Game =================================================
new_deck = Deck()
new_deck.shuffle()

# Deal the cards out to each player:
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# Play the Game =================================================
game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    # Firstly, let's check if anyone lost:

    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    # Otherwise, the game is still on!

    # Start a new round and reset current cards "on the table" or "at battle field"
    player_one_battleCards = []
    # Each player deal a card into battle:
    player_one_battleCards.append(player_one.remove_one())
    
    player_two_battleCards = []
    # Each player deal a card into battle:
    player_two_battleCards.append(player_two.remove_one())
    
    # 
    at_war = True
    while at_war:
        # The last card dealt from both players are sent to battle shall fight

        # If Player One has higher card:
        if player_one_battleCards[-1].value > player_two_battleCards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_battleCards)
            player_one.add_cards(player_two_battleCards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_battleCards[-1].value < player_two_battleCards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_battleCards)
            player_two.add_cards(player_two_battleCards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break

            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_battleCards.append(player_one.remove_one())
                    player_two_battleCards.append(player_two.remove_one())

