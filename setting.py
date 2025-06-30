import pygame

class setting:
    def __init__(self):
        self.image = pygame.image.load('images/Maps/FirstMap/03.1.bmp')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.character_speed = 10 
        self.speed = -5 # Speed for fire attack
        self.charcter_helth = 100
        self.orc_helth = 100
        self.attack_damage = 20
        self.orc_attack_damage = 10
