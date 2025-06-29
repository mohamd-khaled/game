import pygame
from pygame.sprite import Sprite

class attack_character(Sprite):
    def __init__(self, game):
        super().__init__()

        #getting screen dimensions and game setting
        self.game = game
        self.screen = game.screen
        self.setting = game.setting
        self.screen_rect = game.screen.get_rect()

        self.attacking = False
        self.attack_index = 0
        self.attack_counter = 0

        #character moving images list
        self.images = [pygame.transform.flip(pygame.image.load('images/characters/Mage/Attack/attack1.png'), True, False),
            pygame.transform.flip(pygame.image.load('images/characters/Mage/Attack/attack2.png'), True, False),
            pygame.transform.flip(pygame.image.load('images/characters/Mage/Attack/attack3.png'), True, False),
            pygame.transform.flip(pygame.image.load('images/characters/Mage/Attack/attack4.png'), True, False),
            pygame.transform.flip(pygame.image.load('images/characters/Mage/Attack/attack5.png'), True, False),
            pygame.transform.flip(pygame.image.load('images/characters/Mage/Attack/attack6.png'), True, False),
            pygame.transform.flip(pygame.image.load('images/characters/Mage/Attack/attack7.png'), True, False),
        ]

        
        self.image_index = 0
        self.image = self.images[self.image_index]

        self.rect = self.image.get_rect()
        self.rect.midbottom = game.character.rect.midbottom

        self.animation_counter = 0
        self.animation_done = False

    def update(self):
        if not self.animation_done:
            self.animation_counter += 1
            if self.animation_counter % 5 == 0:
                self.image_index += 1
                if self.image_index < len(self.images):
                    self.image = self.images[self.image_index]
                else:
                    self.animation_done = True
                    self.kill()



