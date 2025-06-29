import pygame
from pygame.sprite import Sprite

class fire(Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.attack_img = [ pygame.image.load('images/characters/Mage/Fire/fire1.png'),
            pygame.image.load('images/characters/Mage/Fire/fire2.png'),
            pygame.image.load('images/characters/Mage/Fire/fire3.png'),
            pygame.image.load('images/characters/Mage/Fire/fire4.png'),
        ]

        self.image_index = 0
        self.image = self.attack_img[self.image_index]
        self.rect = self.image.get_rect()

        self.rect.left = game.character.rect.left
        self.rect.centery = game.character.rect.centery
        self.speed = self.setting.speed  # Speed in y direction if vertical (adjust if you want horizontal)

        self.animation_counter = 0  # To slow down animation frame updates


    def update(self):
        # Move attack (you can change direction logic)
        self.rect.x += self.speed

        self.animation_counter += 1
        if self.animation_counter % 5 == 0:
            self.image_index = (self.image_index + 1) % len(self.attack_img)
            self.image = self.attack_img[self.image_index]
                                     
        if self.rect.left < (0.8 * self.screen.get_rect().width):
            self.kill()
