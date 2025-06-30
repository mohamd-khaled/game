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
        self.images = [pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_000.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_001.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_002.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_003.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_004.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_005.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_006.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_007.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_008.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_009.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_010.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('images/monsters/Orc/Slashing/0_Orc_Slashing_011.png'), (100, 100)),
            ]
        
        self.image_index = 0
        self.image = self.images[self.image_index]

        self.rect = self.image.get_rect()
        self.rect.midleft = (100, self.game.height // 2)

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



