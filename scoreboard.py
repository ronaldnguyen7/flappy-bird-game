import pygame.font
from pygame.sprite import Group

from bird import Bird

# A class to manage scoring
class Scoreboard:
    
    # Initializing scoring assets
    def __init__(self, fb_game):
        self.fb_game = fb_game
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fb_game.settings
        self.stats = fb_game.stats

        # Font settings for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()
    
    # Turn the score into a rendered image
    def prep_score(self):
        score_str = "{:,}".format(int(self.stats.score))
        self.score_image = self.font.render(score_str, True,
        self.text_color, None)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.score_rect.top + 20

    # Draws scores to the screen
    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    # Turn the high score into a rendered image
    def prep_high_score(self):
        high_score_str = "{:,}".format(int(self.stats.high_score))
        self.high_score_image = self.font.render('High Score: ' + high_score_str, True,
            self.text_color, None)
        
        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 20

    # Check to see if there's a new high score
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()