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

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
