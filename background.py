import pygame

class bg():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/Maps/FirstMap/03.1.bmp')
        self.rect = self.image.get_rect()

        self.battle_img = pygame.image.load('images/Maps/game_background_4/game_background_4.png')
        self.battle_rect = self.battle_img.get_rect()

    def bg(self):
        self.screen.blit(self.image, self.rect)

    def battle_bg(self):
        self.screen.blit(self.battle_img, self.battle_rect)