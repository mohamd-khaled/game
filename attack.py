import pygame
from pygame.sprite import Sprite

class attack(Sprite):
    
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

        self.rect.midleft = game.character.rect.midleft

        self.speed = self.setting.speed  # Speed in y direction if vertical (adjust if you want horizontal)

        self.animation_counter = 0  # To slow down animation frame updates

        self.x = float(self.rect.x)

    def update(self):
        # Move attack (you can change direction logic)
        self.rect.x += self.speed

        self.animation_counter += 1
        if self.animation_counter % 5 == 0:
            self.image_index = (self.image_index + 1) % len(self.attack_img)
            self.image = self.attack_img[self.image_index]
                                     
        if self.rect.bottom < 0:
            self.kill()
