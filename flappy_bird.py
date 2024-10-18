import sys

import pygame

from settings import Settings
from bird import Bird
from bot_pipe import BotPipe
from top_pipe import TopPipe

# Class to manage game assets and behavior
class FlappyBird:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_height, self.settings.screen_height))
        self._set_background_image()
        self._create_pipe()

        self.bird = Bird(self)
    
    # Starts the game loop
    def run_game(self):
        while True:
            self._check_events()
            self.bird.update()
            self.pipes_update()
            self._update_screen()

    # Updates images on the screen, and flip to the new screen.
    def _update_screen(self):
        self._set_background_image()

        # Draw the pipes
        self._draw_pipes()
        self.bird.blitme()

        pygame.display.flip()
    
    # Respond to keypresses and mouse events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    # Handles key presses 
    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bird.jump()

    # sets background image for the game
    def _set_background_image(self):
        background_image = pygame.image.load('images/background.png')
        self.screen.blit(background_image, (0, 0))

    # Create a pair of pipes
    def _create_pipe(self):
        self.top = TopPipe(self)
        self.bot = BotPipe(self)

        self.top.rect.y = -200
        self.bot.rect.y = 600

    def _draw_pipes(self):
        self.screen.blit(self.top.image, self.top.rect)
        self.screen.blit(self.bot.image, self.bot.rect)

    def pipes_update(self):
        self.bot.update()
        self.top.update()

# Make a game instance, and run the game.
if __name__ == '__main__':
    fb = FlappyBird()
    fb.run_game()