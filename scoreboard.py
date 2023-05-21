import pygame.font

# to create ships' group
from pygame.sprite import Group

from ship import Ship

class Scoreboard:

    def __init__(self, ai_game):
        # added to allow the creation of ships
        self.ai_game = ai_game

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the image of initial score
        self.prep_score()

        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    # transform the text to an image
    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " + "{:,}".format(rounded_score).replace(",", " ")
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    # draw the score, the level and ship left on the screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    # turn the high score into an image
    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High score: " + "{:,}".format(high_score).replace(",", " ")
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    # turn the level into an image
    def prep_level(self):
        level_str = "Lvl: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level
        self.level_rect = self.level_image.get_rect()
        # to display level below score:
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    # display the ship number left
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    # check to see if there's a new high score
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
