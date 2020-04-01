'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-04-01 14:42:58
@LastEditors: JackZhang
@LastEditTime: 2020-04-01 23:22:50
'''
import pygame, os
from game_config import *
vec2 = pygame.math.Vector2

# base class defination
class FlyingObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = vec2(0, 0)
        self.position = vec2(0, 0)

# player class
class Player(FlyingObject):
    def __init__(self):
        FlyingObject.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_PATH, "player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT-self.rect.height)
        self.shoot_bullet_rate = 15

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] >= 1 and mouse_position[0] <= WIDTH-2 and mouse_position[1] >= 1 and mouse_position[1] < HEIGHT-2:
                self.rect.center = mouse_position
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        

    def shoot_bullet(self, bullet):
        bullet.rect.center = self.rect.center
        bullet.rect.bottom = self.rect.top
        bullet.initiated = True

# bullet class
class Bullet(FlyingObject):
    def __init__(self, controller):
        FlyingObject.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_PATH, "player_bullet.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.initiated = False
        self.controller = controller

    def update(self):
        if self.initiated:
            self.rect.y -= 5
        if self.rect.y < 0:
            self.destroy()
    
    def destroy(self):
        self.controller.game.all_sprites.remove(self)

    
