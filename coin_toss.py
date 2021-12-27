# This program is a  coin toss game where 2 computer players guess the user
# inputs call. If they guess correctly they get a point there are 4 tries in 
# each round and whoever has the most points wins the round. Multiple rounds
# can be played.
import random

# Imports instructions text
filename = 'instructions.txt'
filemode = 'r' # read-only
file = open(filename, filemode)
instructions = file.read()
file.close()
print(instructions)

# Loops for if user wants to play again
play_again = True
player_1_wins = 0
player_2_wins = 0
ties = 0 
while play_again:   
    player1_total = 0
    player2_total = 0 
    player1_tosses = []
    player2_tosses = []
    # Loop that makes game run for only 4 times
    tries = 0
    while tries < 4:  
        # Picks random str from coins list
        coins = ['H', 'T']
        player_1_guess = (random.choice(coins))
        player_2_guess = (random.choice(coins))
 
 
        # Prompt user to input a call
        user_call = input('Heads or Tails ? Type H or T > ')
        
        # Variables for player wins if the player guesses match users call
        player_1_win = user_call.upper() == player_1_guess
        player_2_win = user_call.upper() == player_2_guess 
            
        # Prints what computer players have tossed
        print('Player 1 has tossed', player_1_guess)
        print('Player 2 has tossed', player_2_guess)
        
        # Prints winning players if tosses match users call add number of wins
        # into a variable
        if player_1_win:
            print('Player 1 wins')
            player1_total = player1_total + 1
        if player_2_win:
            print('Player 2 wins') 
            player2_total = player2_total + 1   
        
        # Appends both player coin tosses from all 4 tries in round into a 
        # sequence
        player1_tosses.append(player_1_guess)
        player2_tosses.append(player_2_guess)  
            
        # Ends while loop after 4 tries
        tries = tries + 1
        
    # Prints round stats for the round
    print('ROUND STATS')
    if player1_total > player2_total:
        player_1_wins = player_1_wins + 1
        print('Player 1 wins this round')
    if player1_total < player2_total:
        player_2_wins = player_2_wins + 1
        print('Player 2 wins this round')
    if player1_total == player2_total:
        ties = ties + 1
        print('The round is a tie')
    print('Player 1 points:', player1_total)
    print('Player 2 points:', player2_total)
    print('Player 1 tossed', player1_tosses)
    print('Player 2 tossed', player2_tosses)      
        
    # Prints number of times H H is found in sequence
    sequence1 = 0
    sequence2 = 0
    for index in range(len(player1_tosses)-1):
        if player1_tosses[index] == 'H' and player1_tosses[index+1] == 'H':
            sequence1 = sequence1 + 1
    for index in range(len(player2_tosses)-1):
        if player2_tosses[index] == 'H' and player2_tosses[index+1] == 'H':
            sequence2 = sequence2 + 1
    print('H H found in the player 1 sequence', sequence1, 'times') 
    print('H H found in the player 2 sequence', sequence2, 'times')
    
    # Prompts user to play again
    answer = input('Do you want to play another round? y/n > ')
    if answer.upper() != 'Y':
        play_again = False
# Prints out summary stats(stats from all rounds played)
print('SUMMARY STATS')
print('number of ties:', ties)
print('number of player 1 wins:', player_1_wins)
print('number of player 2 wins:', player_2_wins)
    
