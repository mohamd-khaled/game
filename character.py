import pygame
from pygame.sprite import Sprite

class character(Sprite):
    def __init__(self, game):
        super().__init__()

        #getting screen dimensions and game setting
        self.screen = game.screen
        self.setting = game.setting
        self.screen_rect = game.screen.get_rect()

        #character moving images list
        self.images = [ pygame.image.load('images/characters/Mage/mage.png')    ,
            pygame.image.load('images/characters/Mage/Walk/walk1.png'),
            pygame.image.load('images/characters/Mage/Walk/walk2.png'),
            pygame.image.load('images/characters/Mage/Walk/walk3.png'),
            pygame.image.load('images/characters/Mage/Walk/walk4.png'),
            pygame.image.load('images/characters/Mage/WaLK/walk5.png'),
            pygame.image.load('images/characters/Mage/WaLK/walk6.png')
        ]

        self.move_images = self.images.copy()

        self.image = self.move_images[0] #idel character image
        self.rect = self.image.get_rect() #get character dimesions
        self.rect.center = self.screen_rect.center #get the center to put character in it

        #Flags to know the direction of movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        #Convert the position to float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Variables to control the frames of movement
        self.current_frame = 0
        self.frame_time = 0
        self.frame_delay = 100  # milliseconds between frames

        self.facing_right = True  # Start facing right

    #function to draw the character
    #def blitme(self):
    #    self.screen.blit(self.image, self.rect)

    #Updating the character position
    def update(self):
        moving = (self.moving_right or self.moving_left or self.moving_up or self.moving_down)
        
        #increase the position and determine the direction of movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.setting.character_speed
            if not self.facing_right:
                self.moving_direction(True)

        if self.moving_left and self.rect.left > 0:
            self.x -=self.setting.character_speed
            if self.facing_right:
                self.moving_direction(False)
            
        if self.moving_up and self.rect.top > 0:
            self.y -=self.setting.character_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y +=self.setting.character_speed

        #Reassign the the position
        self.rect.x = self.x
        self.rect.y = self.y

        #Update the image to make the movement 
        if moving:
            now = pygame.time.get_ticks()
            if now - self.frame_time > self.frame_delay:
                self.frame_time = now
                self.current_frame = (self.current_frame + 1) % len(self.move_images)
                self.image = self.move_images[self.current_frame]
        else:
            self.image = self.move_images[0]

    #Function to flip images when change direction of movement
    def moving_direction(self, face_right):
        self.facing_right = face_right
        if face_right:
            self.move_images = self.images.copy()
        else:
            self.move_images = [pygame.transform.flip(img, True, False) for img in self.images]
                

