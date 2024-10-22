# Class to manage game stats and scoring
class GameStats:

    # Initializes game statisics
    def __init__(self, fb_game):
        self.settings = fb_game.settings
        self.reset_stats()

        self.game_active = True

        self.high_score = 0

    # Resets Score
    def reset_stats(self):
        self.score = 0
