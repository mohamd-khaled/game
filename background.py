import pygame

class bg():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/Maps/FirstMap/03.bmp')
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)