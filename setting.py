import pygame

class setting:
    def __init__(self):
        self.image = pygame.image.load('images/Maps/FirstMap/03.bmp')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.character_speed = 5