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
        self.screen = pygame.display.set_mode((self.setting.width, self.setting.height))
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height 
        self.bg = bg(self)
        self.character = character(self)
        self.orcs = pygame.sprite.Group()
        self.orc()


    def Run_Game(self):

        while True:
            self.check_event()
            self.update_screen()
            self.character.update()
            #self.char_orc_collision()
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

            
        
    def update_screen(self):
        self.bg.blitme()
        self.character.blitme()
        #self.character.draw(self.screen)
        self.orcs.draw(self.screen)
        pygame.display.flip()  

    """def char_orc_collision(self):
        collision = pygame.sprite.spritecollide(self.show_char, self.show_char, True)
        if collision:    
            for orcs in collision:
                orcs.kill()
                self.show_char.kill()"""    

if __name__ == '__main__':
    game = game()
    game.Run_Game()