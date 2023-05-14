class Settings:
    # Class for game settings

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.7
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.3
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
