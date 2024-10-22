import pygame
from pygame.sprite import Sprite

# A class to manage the bottom pipes
class BotPipe(Sprite):
    
    # Initialize the bottom and set its starting position
    def __init__(self, fb_game):
        super().__init__()
        self.screen = fb_game.screen
        self.settings = fb_game.settings

        # Load Bottom Pipe image + initialize rect
        self.image = pygame.image.load('images/botpipe.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen.get_rect().right 

        self.x = float(self.rect.x)

    # Returns true if the pipe is at the edge of the screen
    def check_edges(self):
        screen_rect = self.screen.get_get_rect()
        
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        else:
            return False

    # Moves the pipe left
    def update(self):
        self.x -= self.settings.pipe_speed
        self.rect.x = self.x