import pygame
import random
from pygame.sprite import Sprite

class Orcs(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/monsters/Orc/Idle/0_Orc_Idle_000.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, (self.screen_rect.width - self.rect.width))
        self.rect.y = random.randint(0, (self.screen_rect.height - self.rect.height))
