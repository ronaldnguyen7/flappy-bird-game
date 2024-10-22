# Class to store all game settings for Flappy Bird
class Settings:

    def __init__(self):

        # Screen Settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Bird Settings
        self.jump_speed = 3
        self.jump_height = 25
        self.fall_speed = 2.5

        # Pipe Settings
        self.pipe_starting_x = 800
        self.pipe_speed = 2
        self.pipe_gap = 400
        
