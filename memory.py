# This program is a memory game where you have to match 2 tiles with the same
# image. If the two tile images match then the tiles remain exposed, if not 
# they both return to their hidden form. The goal is to match all 16 tiles.

import pygame, random, time

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Memory')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 

# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      self.time_elapsed = 0
      
      # === game specific objects
      self.board_width = 5
      self.board_height = 4
      self.images = self.add_images()    
      self.board = self.create_board() 
      self.selected_tiles = []
      self.matched_tiles = []
       
   def add_images(self):
      # Adds all the images to a list and duplicates it to make 2 of each image
      # - self is the Game
      
      images = ['image1.bmp', 'image2.bmp', 'image3.bmp', 'image4.bmp', 
                'image5.bmp', 'image6.bmp', 'image7.bmp', 'image8.bmp',]
      # empty list to append images to
      all_images = []
      for i in range(len(images)):
         # appends each image to list
         all_images.append(images[i])
         # makes a duplicate and appends to list
         duplicate = images[i]
         all_images.append(duplicate)
      # shuffles the list to make images appear in random positions
      random.shuffle(all_images)
      return all_images
      
   def create_board(self):
      # Creates the tiles on the board
      # - self is the Game
      
      width = self.surface.get_width() // self.board_width
      height = self.surface.get_height() // self.board_height
      board = []
      counter = 0
      for row_index in range(self.board_width - 1):
         row = []
         for col_index in range(self.board_height):
            x = col_index * width
            y = row_index * height
            # creating a tile object with different x, y, and image each time
            tile = Tile(x, y, self.images[counter], self.surface)
            row.append(tile)
            counter += 1
         board.append(row) 
      return board 
 
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game 

      while not self.close_clicked:  # until player clicks close box
         self.handle_events()
         self.draw()  
         if self.continue_game:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with frames per second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONDOWN and self.continue_game:
            self.handle_mousedown(event)
            
   def handle_mousedown(self, event):
      # Handles what happens if the mouse button is pressed
      # - self is the Game
      # - event is the event.type object
      
      for row in self.board:
         for tile in row:
            # checks what tile the mouse clicked on and if it hasn't 
            # already been matched or clicked on twice in a row respectively
            if tile.select(event.pos) and tile not in self.matched_tiles and \
            tile not in self.selected_tiles:
               # makes the tile exposed
               tile.set_exposed()
               # appends it to a list for selected tiles
               self.selected_tiles.append(tile)
   
   def check_matching(self):
      # Checks if two tiles match
      # - self is the Game
      
      # tiles won't be compared until two tiles have been clicked on
      if len(self.selected_tiles) == 2: 
         # if the both of the names of their image files don't match
         if self.selected_tiles[0].get_image_name() != \
         self.selected_tiles[1].get_image_name(): 
            # sets them to hidden again after a pause
            time.sleep(0.5)
            for i in range(2):
               self.selected_tiles[i].set_hidden()
         else:            
            # if they match they are appended into a list for matched tiles
            for tile in self.selected_tiles:
               self.matched_tiles.append(tile)
         
         # removes both tiles from selected tiles list so that two new tiles 
         # can be compared
         for i in range(2):
            self.selected_tiles.remove(self.selected_tiles[0])
               
   def draw(self):
      # Draw all game objects.
      # - self is the Game
      
      self.surface.fill(self.bg_color) # clear the display surface first
      # displays the time elapsed on the screen
      self.show_time(self.time_elapsed)
      # draws each tile on the screen
      for row in self.board:
         for tile in row:  
            tile.draw()
            
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game 
      
      self.check_matching()
      self.time_elapsed = pygame.time.get_ticks()//1000
   
   def show_time(self, time):   
      # Shows elapsed time on the top right corner of the screen
      # - self is the Game
      # - time is an int from pygame.time.get_ticks()
      
      text_string = str(time)
      fontsize = 70
      fg_color = 'white'
      bg_color = 'black'
      time = pygame.font.SysFont('Ariel', fontsize, True) 
      text = time.render(text_string, True, fg_color, bg_color)
      top_right_corner = self.surface.get_width() - text.get_width()
      location = (top_right_corner, 0)
      self.surface.blit(text, location)         

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game
      
      # if all 16 tiles are in the match_tiles list the game will end
      if len(self.matched_tiles) == len(self.images):
         self.continue_game = False

class Tile:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, x, y, image_name, surface):
      # Initialize a Tile.
      # - self is the Tile to initialize
      # - x is the x coordinate of type int
      # - y is the y coordinate of type int
      # - image_name is a string of the image file name
      # - surface is the window's pygame.Surface object
      
      self.color = pygame.Color('black')
      self.border_width = 4
      self.surface = surface
      self.image_name = image_name
      self.image = pygame.image.load(self.image_name)
      width = self.image.get_width()
      height = self.image.get_height()      
      self.rect = pygame.Rect(x, y, width, height)
      self.exposed = False
      
   def draw(self):
      # Draws the tiles
      # - self is the Tile
      
      # if the tile is exposed it will draw the tile with an exposed image
      if self.exposed:
         pygame.draw.rect(self.surface,self.color,self.surface.blit(self.image, 
                                                self.rect), self.border_width) 
      # if not it will draw the tile with a question mark image
      else:
         pygame.draw.rect(self.surface,self.color,self.surface.blit(pygame.
                     image.load('image0.bmp'), self.rect), self.border_width)
         
   def select(self, pos):
      # Checks if mouse has collided with a tile
      # - self is the Tile
      # - pos is a tuple of x and y coordinates
      
      if self.rect.collidepoint(pos):
         return True
      
   def get_image_name(self):
      # Returns the image file name of a tile
      # - self if the Tile
      
      return self.image_name
   
   def set_exposed(self):
      # Sets a tile to exposed
      # - self is the Tile
      
      self.exposed = True
      
   def set_hidden(self):
      # Sets the tile to hidden
      # - self is the Tile
      
      self.exposed = False

main()