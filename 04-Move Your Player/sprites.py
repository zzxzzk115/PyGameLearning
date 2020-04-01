'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-04-01 14:42:58
@LastEditors: JackZhang
@LastEditTime: 2020-04-01 18:15:39
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