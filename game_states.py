from settings import Settings

class GameStates:
    """Track Statistics of a game"""
    def __init__(self , ai_game):
        self.settings = ai_game.settings        
        self.reset_states()
        # High score should never be reset
        self.high_score = 0
        
        
    def reset_states(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1