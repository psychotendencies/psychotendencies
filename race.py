# this program is a game where 2 players race along a lane that is 8 positions
# long. both players start a 0 and positions are determined by the roll of a 6 
# sided die. if a player gets to the same position of the other player the other
# player will be kicked to the beginning. the players must get the exact number
# in order to move to the end position. whoever reaches the end first wins.

import random
    
def roll_die(turn):
    # assigns a random number from 1-6 to the variable dice_roll and returns
    # - turn is the fourth operand of type bool
    dice_roll = random.randint(1,6)
    return dice_roll

def update_player_x_pos(player_x_pos, player_o_pos, dice_roll, end_of_lane):
    # updates player x's position in the lane
    # - player_x_pos is the first operand of type int
    # - player_o_pos is the second operand of type int
    # - dice_roll is the third operand of type int 
    # - end_of_lane is the fourth operand of type int
    
    # prompting user to press the enter key to roll the die
    input('Player x press enter to roll!')
    print('Player x rolled a', dice_roll) 
            
    if player_x_pos + dice_roll > end_of_lane:
        # prints if the dice roll added to player o's position is out of range
        print('The roll was too high, player x stays in this position')
       
    # kicks players o back to starting position if x and o are at the same
    # position
    elif player_x_pos + dice_roll == player_o_pos:
        print('x kicked the rival!')
        player_x_pos = player_o_pos
        player_o_pos = 0
        
    else:
        # updates player x position value depending on the dice roll value 
        player_x_pos = player_x_pos + dice_roll
        
    # returns value of positions of x and o
    return player_x_pos, player_o_pos

def update_player_o_pos(player_x_pos, player_o_pos, dice_roll, end_of_lane):
    # updates player o's position in the lane
    # - player_x_pos is the first operand of type int
    # - player_o_pos is the second operand of type int
    # - dice_roll is the third operand of type int 
    # - end_of_lane is the fourth operand of type int
    
    # prompting user to press the enter key to roll the die
    input('Player o press enter to roll!')
    print('Player o rolled a', dice_roll)
    
    if player_o_pos + dice_roll > end_of_lane:
        # prints if the dice roll added to player o's position is out of range
        print("The roll was too high, player o stays in this position")
        
    # kicks players x back to starting position if x and o are at the same
    # position       
    elif player_o_pos + dice_roll == player_x_pos:
        print("o kicked the rival!")
        player_o_pos = player_x_pos
        player_x_pos = 0
        
    else:
        # updates player o position value depending on the dice roll value         
        player_o_pos = player_o_pos + dice_roll
        
    # returns value of positions of x and o
    return player_x_pos, player_o_pos

def check_game_over(player_x_pos, player_o_pos, end_of_lane):
    # will return true, ending the game, if one of the players reach the last
    # poition in the lane
    # - player_x_pos is the first operand of type int
    # - player_o_pos is the second operand of type int 
    # - end_of_lane is the third operand of type int
    
    if player_x_pos == end_of_lane:
        # if player x reaches the last position in the lane
        print('Player x has won!')
        return True
    
    if player_o_pos == end_of_lane:
        # if player o reaches the last position in the lane
        print('Player o has won!')  
        return True

def opponent(turn):
    # returns opposite of what turn previously was 
    # - turn is the fourth operand of type bool
    if turn == True:
        return False
    else:
        return True
    
def display_state(player_x_pos, player_o_pos):
    # displays the lane with players positions
    # - player_x_pos is the first operand of type int
    # - player_o_pos is the second operand of type int  
    
    # index will be in range 0-7 as the lane is 8 spaces long
    lane = ['-', '-', '-', '-', '-', '-', '-', '-']
    for index in range(len(lane)):
        # if the value of player_x_pos is == the index an x will be printed 
        # at that index
        if player_x_pos == index:
            lane[index] = 'x'
        # if the value of player_o_pos is == the index an o will be printed 
        # at that index            
        elif player_o_pos == index:
            lane[index] = 'o'
    
    return lane
        
def main():    
    # prints opening lines that only print once
    print('Players begin in the starting position')  
    border = ('*' * 36) 
    print(border)
    print('update: * - - - - - - -')
    print(border)  
    
    # player positions start at 0 and will increase or reset depending on the
    # return values from def update_position()
    player_x_pos = 0
    player_o_pos = 0    

    # last position of lane is at index 7
    end_of_lane = 7
    
    # assigment for def opponent(), with turn being true at the start of the
    # game, player x will start first
    turn = True
    
    # while loop for looping the game until game_over == true
    game_over = False
    while not game_over:
        dice_roll = roll_die(turn) 
        
        # assigment so that player x and o's value changes everytime while in 
        # the loop
        if turn == True:
            player_x_pos, player_o_pos = update_player_x_pos(player_x_pos, 
            player_o_pos, dice_roll, end_of_lane)
        else:
            player_x_pos, player_o_pos = update_player_o_pos(player_x_pos, 
            player_o_pos, dice_roll, end_of_lane)            
        
        print(border)
        lane = display_state(player_x_pos, player_o_pos)
        print('update: ' + ' '.join(lane))
        print(border)
        
        # changing the value of turn when opponent function is called, 
        # switching the current player
        turn = opponent(turn)   
        
        # if def check_game_over() returns true game_over will == true, ending
        # the loop
        game_over = check_game_over(player_x_pos, player_o_pos, end_of_lane)
            
main()