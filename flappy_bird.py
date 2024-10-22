import sys

import pygame
import random

from settings import Settings
from bird import Bird
from bot_pipe import BotPipe
from top_pipe import TopPipe
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

# Class to manage game assets and behavior
class FlappyBird:

    def __init__(self):
        # Initializes all game assets
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        self._set_background_image()
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.pipes = pygame.sprite.Group()
        self._create_pipe()

        self.bird = Bird(self)

        self.play_button = Button(self, "Try Again")
        self.scoring_index = 0
    
    # Starts the game loop
    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.sb.prep_score()
                self.bird.update()
                self.pipes_update()

            self._update_screen()

    # Updates images on the screen, and flip to the new screen
    def _update_screen(self):
        self._set_background_image()

        # Draw the pipes
        self._draw_pipes()

        # Draw bird
        self.bird.blitme()
        
        # Draws the score
        self.sb.draw_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
    
    # Respond to keypresses and mouse events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

        self.top.rect.y = random.randint(-400, -100)
        self.bot.rect.y = self.top.rect.y + 750

        self.pipes.add(self.top, self.bot)

    # Draws pairs of pipes
    def _draw_pipes(self):
        for pipe in self.pipes:
            self.screen.blit(pipe.image, pipe.rect)

    # Moves pipes and Checks whether or not the bird has passed a pipe
    def pipes_update(self):
        for pipe in self.pipes:
            pipe.update()
        
        last_pipe = self.pipes.sprites()[-1]
        if last_pipe.rect.x < (self.settings.pipe_starting_x - self.settings.pipe_gap):
            self._create_pipe()

        
        if self.pipes.sprites()[self.scoring_index].rect.bottomright < self.bird.rect.bottomleft:
            print(self.stats.score)
            self.scoring_index += 1
            self.stats.score = self.scoring_index/2
        
        self._check_bird_pipes_collisions()

    # Checks to see if the bird has collided with a pipe
    def _check_bird_pipes_collisions(self):
        collisions = pygame.sprite.spritecollide(self.bird, self.pipes, False)

        if collisions:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.sb.prep_score()
            self.sb.check_high_score()

    # Resets the game when the player clicks Try Again
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            # Reset the game statistics.
            self.stats.reset_stats()
            self.bird.jumps = 0
            self.stats.game_active = True
            self.scoring_index = 0

            # Empty pipes, reset bird
            self.pipes.empty()
            self._create_pipe()
            self.bird.reset_height()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

# Starts game
if __name__ == '__main__':
    fb = FlappyBird()
    fb.run_game()