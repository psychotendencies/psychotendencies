# This program is a pong game where 2 players press keys to move a paddle. The 
# players must guard their corresponding edge, preventing the ball from hitting
# it. If the ball bounces on opposite players edge they win a point. First 
# player to 11 points wins the game and the game ends.

import pygame

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Pong')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object 

      # === objects that are part of the game
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.close_clicked = False
      self.continue_game = True
      self.left_score = 0
      self.right_score = 0
      
      self.ball_radius = 5
      self.ball_center = [self.surface.get_width()//2, self.surface.get_height()//2]
      self.ball_velocity = [6, 2]
      self.ball = Ball('white', self.ball_radius, self.ball_center, 
                       self.ball_velocity, self.surface)
      self.left_paddle = Paddles('white', 100, 170, 10, 40, [0,0], 
                                 self.surface)
      self.right_paddle = Paddles('white', 390, 170, 10, 40, [0,0], 
                                  self.surface)
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         self.handle_events()
         self.draw()    
         if self.continue_game:
            self.update()
            self.game_over()
         
   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game
      
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         elif event.type == pygame.KEYDOWN:
            self.handle_keydown(event)  
         elif event.type == pygame.KEYUP:
            self.handle_keyup(event)
      pygame.display.flip()
      
   def handle_keydown(self, event):
      # Handles keys that are pressed down 
      # - self is the Game
      # - event is the event type

      paddle_speed = 9
      if event.key == pygame.K_q: # move up
         self.left_paddle.set_vertical_velocity(-paddle_speed)
      if event.key == pygame.K_a: # move down
         self.left_paddle.set_vertical_velocity(paddle_speed)
      if event.key == pygame.K_p: # move up
         self.right_paddle.set_vertical_velocity(-paddle_speed)
      if event.key == pygame.K_l: # move down
         self.right_paddle.set_vertical_velocity(paddle_speed)      
      
   def handle_keyup(self, event):
      # Handles keys that are up 
      # - self is the Game 
      # - event is the event type
      
      if event.key == pygame.K_q or event.key == pygame.K_a: 
         self.left_paddle.set_vertical_velocity(0)
      if event.key == pygame.K_p or event.key == pygame.K_l: 
         self.right_paddle.set_vertical_velocity(0)

   def draw(self):
      # Draw all game objects.
      # - self is the Game
      
      self.surface.fill(self.bg_color)  # clear the display surface first
      self.ball.draw()
      self.right_paddle.draw()
      self.left_paddle.draw()
      self.show_scores()
      pygame.display.update()  # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game
      
      self.ball.move()
      self.left_paddle.move()
      self.right_paddle.move()
      self.collide()
         
   def show_scores(self):
      # Displays scores on screen
      # - self is the Game
      
      fontsize = 70
      fg_color = 'white'
      bg_color = 'black'
      score = pygame.font.SysFont('Ariel', fontsize, True)      
      
      # displays score for player on left side
      if self.ball_radius + self.ball_center[0] >= self.surface.get_width():
         self.left_score += 1
      text_string = str(self.left_score)
      text = score.render(text_string, True, fg_color, bg_color)
      location = (0,0)
      self.surface.blit(text, location)         
         
      # displays score for player on right side
      if self.ball_center[0] <= self.ball_radius:
         self.right_score += 1
      text_string = str(self.right_score)
      text = score.render(text_string, True, fg_color, bg_color)
      x_location = self.surface.get_width() - text.get_width()
      location = (x_location, 0)
      self.surface.blit(text, location)      
      
   def game_over(self):
      # Check and remember if the game should continue
      # - self is the Game
      
      max_score = 11
      if self.left_score >= max_score or self.right_score >= max_score:
         self.continue_game = False
         return self.continue_game
      
   def collide(self):
      # Check if collision between ball and paddles occurs and reverses ball
      # velocity
      # - self is the Game
      
      if self.left_paddle.collide_with_ball(self.ball_center[0], 
                                            self.ball_center[1]):
         self.ball.collide_with_left_paddle()
      if self.right_paddle.collide_with_ball(self.ball_center[0], 
                                             self.ball_center[1]):
         self.ball.collide_with_right_paddle()
      
class Ball:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, color, radius, center, velocity, surface):
      # Initialize a Ball.
      # - self is the Ball to initialize
      # - color is the pygame.Color of the Ball
      # - radius is the int pixel radius of the Ball
      # - center is a list containing the x and y int
      #   coords of the center of the Ball      
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(color)
      self.radius = radius
      self.center = center
      self.velocity = velocity
      self.surface = surface
   
   def move(self):
      # Change the location of the Ball by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Ball
      
      size = (500,400)
      for i in range(0,2):
         self.center[i] = self.center[i] + self.velocity[i]
      for i in range(0,2):
         if self.center[i] < self.radius:
            # reached the minimum for this coordinate
            # right and bottom
            self.velocity[i] = - self.velocity[i] 
         if self.center[i] + self.radius > size[i]:
            # reached the maximum for this coordinate
            # left and top
            self.velocity[i] = - self.velocity[i]
   
   def draw(self):
      # Draw the dot on the surface
      # - self is the Ball
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
      
   def collide_with_right_paddle(self):
      # Reverses x velocity if it hits left side of right paddle
      # - self is the Ball
      
      if self.velocity[0] > 0:
         self.velocity[0] = - self.velocity[0]   
         
         
   def collide_with_left_paddle(self):
      # Reverses x velocity if it hits right side of left paddle
      # - self is the Ball
      
      if self.velocity[0] < 0:
         self.velocity[0] = - self.velocity[0]    

class Paddles:
   # An object in this class represents a Paddle that moves
   
   def __init__(self, color, x, y, width, height, velocity, surface):
      # Initialize a Paddle.
      # - self is the Paddle to initialize
      # - color is the pygame.Color of the dot
      # - x is the int coordinate of the outer most left point of the paddle
      # - y is the int coordinate of the of where the leftest part of
      #   paddle starts
      # - width is the int width of the paddle
      # - height is the int height of the paddle
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object
      
      self.color = pygame.Color(color)
      self.surface = surface    
      self.rect = pygame.Rect(x, y, width, height)
      self.velocity = velocity
      
   def set_vertical_velocity(self, vertical_distance):
      # Sets new vertical velocity for the Paddle
      # - self is the Paddle 
      # - vertical_distance is an int of the new vertical velocity
      
      self.velocity[1] = vertical_distance
  
   def move(self):
      # Moves the paddle such that paddle does not move outside the window
      # - self is the Paddle 
      
      # moves paddles in place 
      self.rect.move_ip(0, self.velocity[1])
      # stops paddle from going above top of screen
      if self.rect.top <= 0: 
         self.rect.top = 0
      # stops paddle from going below bottom of screen
      elif self.rect.bottom >= self.surface.get_height():
         self.rect.bottom = self.surface.get_height()
   
   def draw(self):
      # Draws the Paddle
      # - self is the Paddle
      
      pygame.draw.rect(self.surface, self.color, self.rect)
      
   def collide_with_ball(self, x, y):
      # Checks if x y coords are in the Paddle
      # - self is the Paddle
      # - x is an int of the ball x coords
      # - y is an int of the ball y coords
      
      collided = self.rect.collidepoint(x,y)
      return collided
             
main()