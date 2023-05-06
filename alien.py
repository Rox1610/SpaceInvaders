import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__ (self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien spaceship image and get its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (164.8, 92.7))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
