import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A Class To manage a ship"""
    def __init__(self , ai_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the ship image and get its rect
        self.image = pygame.image.load('AlienInvasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # start the ship at the bottom center of the screen
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flags , starting from ship Not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags"""
        # update the ship's x value , not the rect
        # Limit the movement of the ship when it reaches the edge of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x
        
    def _center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)