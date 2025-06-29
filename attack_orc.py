import pygame
from pygame.sprite import Sprite

class attack_orc(Sprite):
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
        self.images = [pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_000.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_001.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_002.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_003.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_004.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_005.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_006.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_007.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_008.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_009.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_010.png'),
            pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_011.png'),
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



