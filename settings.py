class Settings: 
    """ A class to store all settings for allien Invasion."""

    def __init__(self):
        """ Initialize the games settings. """
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # White color
        self.bg_color = (255,255,255)

        #Ship settings
        self.ship_speed = 1.5
