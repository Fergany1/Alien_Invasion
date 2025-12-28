class Settings:
    """A Class to store settings for alien Invasion"""

    def __init__(self):
        """initialize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        #self.ship_speed = 1.5
        
        # Bullet Settings
       # self.bullet_speed = 2
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
                
        # Alien settings
     #   self.alien_speed = 1.0  # Add this line to define alien speed
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        self.fleet_drop_speed = 20
        self.alien_points = 50
        
        # How Quickly the game speeds up
        self.speed_upscale = 1.1
        # How Quickly the points values increases
        self.score_scale = 1.5
        
        # Default Difficulty Level
        self.difficulty_level = 'medium'
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        if self.difficulty_level == 'easy':
            self.ship_speed = 1.5
            self.alien_speed = 0.5
            self.bullet_speed = 2
            self.bullets_allowed = 10
            self.ship_limit = 3
        elif self.difficulty_level == 'medium':
            self.ship_speed = 2.0
            self.alien_speed = 1.0
            self.bullet_speed = 3
            self.bullets_allowed = 5
            self.ship_limit = 2
        elif self.difficulty_level == 'hard':
            self.ship_speed = 2.5
            self.alien_speed = 1.5
            self.bullet_speed = 4
            self.bullets_allowed = 3
            self.ship_limit = 1
        # Scoring Settings
        self.alien_points = 50
        self.fleet_direction = 1  # 1 for right, -1 for left
            
    def increase_speed(self):
        """increase speed settings & Points Values"""
        self.ship_speed *= self.speed_upscale
        self.alien_speed *= self.speed_upscale
        self.bullet_speed *= self.speed_upscale
            
        self.fleet_drop_speed *= self.speed_upscale
            
        self.alien_points = int(self.alien_points * self.score_scale)
    
    def set_difficulty(self , difficulty):
        if difficulty == 'easy':
            print("easy")
        elif difficulty =='medium':
            pass
        elif difficulty == 'hard':
            pass
            
            
            