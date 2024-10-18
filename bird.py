import pygame
from pygame.sprite import Sprite

# A class to manage the bird
class Bird(Sprite):

    # Initialize the Bird and set its starting position
    def __init__(self, fb_game):
        super().__init__()
        self.screen = fb_game.screen
        self.settings = fb_game.settings
        self.screen_rect = fb_game.screen.get_rect()

        self.image = pygame.image.load('images/bird.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.rect.x += 200

        self.y = float(self.rect.y)
        self.jumps = 0
        self.jumping = False

    # Update the bird's position
    def update(self):
        if self.falling() and self.y > 0:
            self.y -= self.settings.jump_speed
            self.jumps -= 1
        elif self.y < self.settings.screen_height - self.rect.height:
            self.y += self.settings.fall_speed

        if self.y > self.settings.screen_height - self.rect.height:
            self.y = self.settings.screen_height - self.rect.height

        self.rect.y = self.y

    # Draw the bird at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

    # Returns where the bird the falling or jumping
    def falling(self):
        return True if self.jumps > 0 else False
    
    # Resets jump counter
    def jump(self):
        self.jumps += self.settings.jump_height