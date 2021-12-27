# This program is a card game where 2 players are dealt 5 cards from a deck of
# 52 cards. The player with the most aces in their hand wins. If both players
# have the same amount of aces then the game restarts with a new deck of 
# shuffled cards.

import random

class Card:
    # An object in this class represents a single card in the game
    
    def __init__(self, rank, suit):
        # Initialize a card
        # - self is the Card to initialize
        # - rank is an int from 1-13
        # - suit is a string of one of the suits
        self.rank = rank
        self.suit = suit
        
    def get_rank(self):
        # Converts int of the rank into the word string of the rank
        # - self is the Card
        ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        rank = ranks[self.rank - 1]
        return rank
        
    def display(self):
        # Combines the rank and suit together creting the card
        # - self is the Card
        card = self.get_rank(), 'of', self.suit
        card = ' '.join(card)
        print(card)
    
class Deck:
    # An object of this class represents a deck in the game
    
    def __init__(self):
        # Initialize a deck
        # - self is the Deck to initialize
        self.deck = []   # empty string to add cards to 
        # gets all combinations of the suits and ranks and appends them to the
        # empty self.deck list
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for rank in range(13):
                # creates a card object
                cards = Card(rank, suit)
                self.deck.append(cards)
        
    def shuffle(self):
        # Shuffles deck and returns
        # - self is the deck
        random.shuffle(self.deck)
        return self.deck
          
    def deal(self):
        # Deals deck, one card at a time and removes that card from the deck
        # - self is the deck
        deck = self.shuffle()
        card = deck[0]
        self.deck.remove(card)   # this website helped me with knowing how to 
                                 # remove an item from a list                             
                    # https://note.nkmk.me/en/python-list-clear-pop-remove-del/
        return card
        
class Player:
    # An object of this class represents a player in the game
    
    def __init__(self):
        # Initialize a deck
        # - self is the Player to initialize
        self.player_hand = []
        self.player_aces = 0
        
    def add(self, card):
        # Adds cards to players hands
        # - self is the player
        # - card is the card string to be added
        self.player_hand.append(card)
        return self.player_hand
        
    def ace_cards(self):
        # Counts number of aces in the players hand
        # - self is the player
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            # creates a card object
            ace = Card(1, suit)
            ace = ace.get_rank()
        for i in range(5):
            if self.player_hand[i].get_rank() == ace:
                self.player_aces += 1
        return self.player_aces
        
    def display(self):
        # Displays players hand
        # - self is the player
        for card in self.player_hand:
            card.display()
        
def main():
    game_over = False
    # loop for game the continue if condition not met
    while not game_over:
        # creates a deck object
        deck1 = Deck()
        deck = deck1.shuffle()
    
        print('This is the hand of player 1:')
        # create a player object
        player1_cards = Player()  
        # loop for printing all cards in player 1's hand
        for i in range(5):
            card = deck1.deal()             
            player1_cards.add(card)
            
        player1_cards.display()

        print()
    
        print('This is the hand of player 2:')
        # creates a player object
        player2_cards = Player()
        # loop for printing all cards in player 2's hand
        for i in range(5):
            card = deck1.deal()
            player2_cards.add(card)  
            
        player2_cards.display()
            
        print()
    
        player1_aces = player1_cards.ace_cards() 
        player2_aces = player2_cards.ace_cards()     
        
        # prints number of aces each player has
        print("Number of ace cards in each player's hand:")
        if player1_aces == 1:
            print('Player 1 has ' + str(player1_aces) + ' ace')
        else:
            print('Player 1 has ' + str(player1_aces) + ' aces')
           
        if player2_aces == 1:
            print('Player 2 has ' + str(player2_aces) + ' ace')
        else:
            print('Player 2 has ' + str(player2_aces) + ' aces') 
                
        print()
        
        # prints winner based on who has more aces
        print('Result:')
        if player1_aces > player2_aces:
            print('Player 1 is the winner')
            game_over = True  # ends loop
        elif player1_aces < player2_aces:
            print('Player 2 is the winner')
            game_over = True  # ends loop
        else: 
            print('No winner, shuffle again')
            print()
        
main()