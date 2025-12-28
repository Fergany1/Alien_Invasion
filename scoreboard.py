import pygame.font
from pygame.sprite import Group, Sprite

from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        """Initializing the Scoreboard"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.states = ai_game.states
        
        # Font settings for  Scoring Info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        """Turn score into a rendered image."""
        round_score = round(self.states.score , -1)
        score_str = f"{round_score :,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Position the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """ Turn High Score Into Rendered Image"""
        high_score = round(self.states.high_score , -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str , True ,
                                                 self.text_color, self.settings.bg_color)
        
        # Center High Score at the Top Of the Screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def check_high_score(self):
        """Check If There's a NEW high score"""
        if self.states.score >  self.states.high_score:
            self.states.high_score = self.states.score
            self.prep_high_score()
            
    def prep_level(self):
        """Turn the level text into a render object"""
        level_str = str(self.states.level)
        self.level_image = self.font.render(level_str , True , 
                                             self.text_color, self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """Show How many ships are left"""
        self.ships = Group()
        for ship_num in range(self.states.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_num * ship.rect.width # Set each ship next to each other 10 pixels
            ship.rect.y = 10
            self.ships.add(ship)
            
        
        
    def show_score(self):
        """Draw the Score on the screen"""
        self.screen.blit(self.score_image , self.score_rect)
        self.screen.blit(self.high_score_image , self.high_score_rect)
        self.screen.blit(self.level_image , self.level_rect)
        self.ships.draw(self.screen)