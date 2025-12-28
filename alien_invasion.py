import sys 
import pygame 

from settings import Settings
from time import sleep # So We Can pause for a moment when a ship is hit
from game_states import GameStates
from ship import Ship
from bullet import Bullet
from button import Button
from scoreboard import Scoreboard
from alien import Alien

class AlienInvasion:
    """Overall Class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, settings, and create game resources"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()  # Create settings object for game settings

        self.screen = pygame.display.set_mode((0,0,),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height  = self.screen.get_rect().height  # Set screen
        
        pygame.display.set_caption("Alien Invasion")
        
        # Create an instance to store game statistics
        # and create OBJ of scoring
        self.states = GameStates(self)
        self.sb  = Scoreboard(self)
                                
        self.ship = Ship(self) # Create ship object
        
        self.bullets = pygame.sprite.Group()# creates the group to holds the bullet in __init__()
        self.aliens = pygame.sprite.Group()
       
        self._create_fleet()

        # Start Alien Invasion in an active state
        #self.game_active = True
        
        # Start Alien Invasion in an inactive state
        self.game_active = False
        # Make Play Button
        self.play_button = Button(self , "Play!!")
        
        # Make Difficulty Buttons
        self.difficulty_levels()
        
    def difficulty_levels(self):
        """make button to select difficulty"""
        self.easy_button = Button(self , "Easy")
        self.medium_button = Button(self , "Medium")
        self.hard_button = Button(self , "Hard")
        
        # Positions of difficulty buttons
        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5 * self.play_button.rect.height)
        self.easy_button._update_msg_position()
        
        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5 * self.easy_button.rect.height)
        self.medium_button._update_msg_position()
        
        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5 * self.medium_button.rect.height)
        self.hard_button._update_msg_position()
        
        # Initialize the medium button to the highlighted color.
        self.medium_button.set_highlighted_color()
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_events()
            self.clock.tick(60)

    def _update_bullets(self):
        """update bullets positions and remove old bullets"""
        # update bullet position
        self.bullets.update()
        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        # check for any bullets that have hit aliens 
        # if so , get rid of the bullet and the aliens
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.states.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
        
            # Increase Levels
            self.states.level += 1
            self.sb.prep_level()
            
    def _update_aliens(self):
        """"Check if the fleet is at edge then update the positions of all the aliens"""
        self._check_fleet_edges()
        self.aliens.update()     
        
        # look for any alien _ ship collisions
        if pygame.sprite.spritecollideany(self.ship , self.aliens):
            self._ship_hit()
            
        # look for an alien that hit the bottom
        self._check_aliens_bottom()
        
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
            
    def _ship_hit(self):
        
        if self.states.ships_left > 0:
            # decrement ships_left & update scoreboard
            self.states.ships_left -= 1
            self.sb.prep_ships() 
        
            # get rid of any bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            
            # Recreate a fleet and center the ship
            self._create_fleet()
            self.ship._center_ship()
            
            # Pause the game for moment
            sleep(0.5)
        else:
            self.game_active = False
        
    def _check_events(self):
        """Respond to key_presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # When a key is pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # When the player Released The Key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # When the Player clicks on the mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self.check_difficulty_levels(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        """Start A New Game when player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset Settings
            self.settings.initialize_dynamic_settings()
            
            # Reset game statistics & Scoreboard
            self.states.reset_states()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            # Reset the game_active flag
            self.game_active = False
            
            # Hide Mouse Cursor
            pygame.mouse.set_visible(False)
            self._start_game()
            
    def check_difficulty_levels(self, mouse_pos):
        """set the difficulty levels"""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        
        if easy_button_clicked:
            self.settings.difficulty_level = 'easy'
            self.easy_button.set_highlighted_color()
            self.medium_button.set_base_color()
            self.hard_button.set_base_color()
        elif medium_button_clicked:
            self.settings.difficulty_level ='medium'
            self.easy_button.set_base_color()
            self.medium_button.set_highlighted_color()
            self.hard_button.set_base_color()
        elif hard_button_clicked:
            self.settings.difficulty_level = 'hard'
            self.easy_button.set_base_color()
            self.medium_button.set_base_color()
            self.hard_button.set_highlighted_color()
            
    def _start_game(self):
        
        # Reset game statistics
        self.states.reset_states()
        self.game_active = True
            
        # get rid of any bullets and aliens
        self.bullets.empty()
        self.aliens.empty()
            
        # Recreate a fleet and center the ship
        self._create_fleet()
        self.ship._center_ship()
        
        # Hide Mouse Cursor
        pygame.mouse.set_visible(False)
        
    def _check_keydown_events(self, event):
        """Responds To Key Presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif (event.key == pygame.K_p) and (not self.game_active):
            self._start_game()

    def _check_keyup_events(self, event):
        """Responds To Key Releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
        
    def _create_fleet(self):
        """Create the fleet of aliens""" 
        """Spacing between alines is one alien width and one alien height"""
        # make an alien
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        
        current_x  , current_y = alien_width , alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x , current_y)
                current_x += 2 * alien_width
            
            # Finished A Row ; reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height
            
    def _create_alien(self , x_position , y_position):
        # Create An Alien an Place it in the FLeet
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)
            
    def _check_fleet_edges(self):
        """Respond if an alien reaches an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
        
    def _change_fleet_direction(self):
        """drop entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # To change the direction multiply it by -1
        
    def _update_events(self):
        """update images on the screen & flip to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        
        self.aliens.draw(self.screen)
        
        # Draw the score INfo
        self.sb.show_score()
        
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
        
        # display the most recent screenshot
        pygame.display.flip()


if __name__ == "__main__":
    # Create an instance of the AlienInvasion class and run the game
    ai = AlienInvasion()
    ai.run_game()
