import pygame
import sys
from background import bg
from setting import setting
from character import character
from orcs import Orcs

class game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting = setting()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height 
        self.bg = bg(self)
        self.character = character(self)
        self.character_group = pygame.sprite.Group()
        self.character_group.add(self.character)
        self.orcs = pygame.sprite.Group()
        self.orc()
        self.in_battle = False
        self.prev_char_pos = None
        self.prev_orc_positions = []
        self.collided_orc = None
        self.battle_sprites = pygame.sprite.Group()

    def Run_Game(self):

        while True:
            self.check_event()
            self.update_screen()
            self.character.update(self.in_battle)
            self.char_orc_collision()
            self.clock.tick(60)
            
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)

    def check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.character.moving_left = True

        elif event.key == pygame.K_UP:
            self.character.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.character.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.character.moving_left = False

        elif event.key == pygame.K_UP:
            self.character.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.character.moving_down = False

    def orc(self):
        for i in range(3):
            show_orc = Orcs(self)
            self.orcs.add(show_orc)


    def char_orc_collision(self):
        collision = pygame.sprite.spritecollide(self.character, self.orcs, True)
        if collision:
            for orcs in collision:
                self.prev_char_pos = self.character.rect.topleft
                self.prev_orc_positions = [(orc, orc.rect.topleft) for orc in self.orcs]
                self.collided_orc = collision[0]
                self.character_group.remove(self.character)
                self.character.rect.midright = (self.width - 100, self.height // 2)
                self.character.image = pygame.transform.flip(self.character.image, True, False)  # face left

                self.collided_orc.rect.midleft = (100, self.height // 2)
                self.battle_sprites.empty()
                self.battle_sprites.add(self.character)
                self.battle_sprites.add(self.collided_orc)
                self.in_battle = True   

    def update_screen(self):
        if self.in_battle:
            self.bg.battle_bg()
            self.battle_sprites.draw(self.screen)
        else:
            self.bg.bg()
            self.character_group.draw(self.screen)
            self.orcs.draw(self.screen)
        pygame.display.flip()       

if __name__ == '__main__':
    game = game()
    game.Run_Game()