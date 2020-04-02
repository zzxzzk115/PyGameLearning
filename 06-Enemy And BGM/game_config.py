'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-04-01 13:34:48
@LastEditors: JackZhang
@LastEditTime: 2020-04-02 13:56:45
'''
import os
import pygame

# path
GAME_PATH = os.path.dirname(__file__)
IMG_PATH = os.path.join(GAME_PATH, "img")
AUDIO_PATH = os.path.join(GAME_PATH, "audio")
# setup the title.
TITLE = "06-Enemy And BGM"
# setup custom game window size.
WINDOW_SIZE = WIDTH, HEIGHT = 336, 607
# set frame-per-second and the clock.
FPS = 60
# custom events
GEN_BULLET = pygame.USEREVENT
GEN_ENEMY = pygame.USEREVENT+1
GEN_BOSS  = pygame.USEREVENT+2
# gen rate
BULLET_GEN_DURATION = 180
ENEMY_GEN_DURATION  = 1000
BOSS_GEN_DURATION   = 5000