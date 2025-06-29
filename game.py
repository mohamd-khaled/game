import pygame
import sys
from background import bg
from setting import setting
from character import character
from attack_char import attack_character
from fire import fire
from orcs import Orcs
from time import sleep

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
        self.loading = False
        self.prev_char_pos = None
        self.prev_orc_positions = []
        self.collided_orc = None
        self.battle_sprites = pygame.sprite.Group()
        self.loading_start_time = None
        self.fire = pygame.sprite.Group()
        self.attack_character = attack_character(self)
        self.turn = "player"  # or "orc"
        self.battle_active = False

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

        elif event.key == pygame.K_SPACE:
            if self.in_battle and self.turn == "player":
                self.start_attack()
                self.fire_attack()


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

    def fire_attack(self):
        new_attack = fire(self)
        self.fire.add(new_attack)


    def char_orc_collision(self):
        if not self.in_battle and not self.loading:
            collision = pygame.sprite.spritecollide(self.character, self.orcs, True)
            if collision:
                for orcs in collision:
                    self.collided_orc = collision[0]
                    self.character_group.remove(self.character)
                    self.battle_sprites.empty()
                    self.battle_sprites.add(self.character)
                    self.battle_sprites.add(self.collided_orc)
                    self.loading = True
                    self.loading_start_time = pygame.time.get_ticks()


    def start_attack(self):
        self.attack_character = attack_character(self)
        self.battle_sprites.add(self.attack_character)
        self.battle_sprites.remove(self.character)

    def update_screen(self):
        current_time = pygame.time.get_ticks()

        if self.loading:
            self.bg.loading_bg()

        # Wait 2 seconds, then transition
            if current_time - self.loading_start_time >= 1000:
                self.loading = False
                self.in_battle = True
                self.turn = "player"
                self.battle_active = True

        elif self.in_battle:
            self.bg.battle_bg()
            self.battle_sprites.draw(self.screen)

            self.fire.update()
            self.fire.draw(self.screen)

            for sprite in self.battle_sprites:
                if isinstance(sprite, attack_character):
                    sprite.update()
                    if sprite.animation_done:
                        self.battle_sprites.remove(sprite)
                        self.battle_sprites.add(self.character)
                        self.turn = "orc" 
            

        else:
            self.bg.bg()
            self.character_group.draw(self.screen)
            #self.orcs.draw(self.screen)
        pygame.display.flip()       

if __name__ == '__main__':
    game = game()
    game.Run_Game()