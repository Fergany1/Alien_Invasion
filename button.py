import pygame.font

class Button:
    def __init__(self , ai_game , msg):
        """Initializing To Button Attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        
        # Support a base color and a highlighted color.
        self.base_color = (0, 135, 0)
        self.highlighted_color = (0, 65, 0)
        
        # Store the message so we can call _prep_msg() when 
        #   the button color changes.
        self.msg = msg
        
        # Set Dimensions and Properties
        self.width, self.height = 200 , 50
        self.text_color = (255 , 255 , 255)
        self.button_color = (0 , 135 , 0)
        self.font = pygame.font.SysFont(None, 48) # None Argument to set default Font
        
        # Build Button Obj and center it
        self.rect = pygame.Rect (0 , 0 , self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # the button message needs to be prepped only once
        self._prep_msg()
        
        
        
    def _prep_msg(self):
        # turn text into rendered image & center text on the button
        # Boolean Argument (antialiasing make edges of the text smoother)
        self.msg_image = self.font.render(self.msg , True , self.text_color , self.button_color) 
     
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def _update_msg_position(self):
        """If the button has been moved, the text needs to be moved as well."""
        self.msg_image_rect.center = self.rect.center
        
    def set_highlighted_color(self):
        """Set the button to the highlighted color."""
        self.button_color = self.highlighted_color
        self._prep_msg()

    def set_base_color(self):
        """Set the button to the base color."""
        self.button_color = self.base_color
        self._prep_msg()

        
    def draw_button(self):
        self.screen.fill(self.button_color , self.rect)
        self.screen.blit(self.msg_image , self.msg_image_rect)
        
        