import pygame
from pygame.sprite import Sprite
from settings import Settings 

class Bullet(Sprite):
    def __init__(self,ai_game):
        # Create a bullet Object at the ship position 
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # create a bullet rect (0,0) & set current position
        self.rect = pygame.Rect(0,0 , self.settings.bullet_width, self.settings.bullet_height)
        
        # set the position of the bullet to the position of the top of the ship 
        # so the bullet will look like it's been fired from the ship
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # store bullet position 
        self.y = self.rect.y
        
    # Move the bullet up by decreasing the y-coordinate   
    def update(self):
        """Move the bullet up the screen"""
        # update the bullet's y value
        self.y -= self.settings.bullet_speed 
        
        # update rect object from self.x and self.y
        self.rect.y = self.y # type: ignore
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect) # type: ignore

