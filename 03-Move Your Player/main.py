'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-03-31 20:48:47
@LastEditors: JackZhang
@LastEditTime: 2020-04-01 13:13:50
'''
# import module.
import pygame, sys, os
from pygame import Color

# set-up path
game_path = os.path.dirname(__file__)
img_path = os.path.join(game_path, "img")
# print(game_path, img_path)

# set up custom game window size.
window_size = width, height = 336, 607

# initialize the pygame and create the main window.
pygame.init()
pygame.display.set_caption("02-Show Your First Sprite")
screen = pygame.display.set_mode(window_size)

# set frame-per-second and the clock.
fps = 30
clock = pygame.time.Clock()

# class Player extends class pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_path, "player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

# you should add all the sprites you want to show on the screen to the pygame.sprite.Group.
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# a flag.
running = True

# game's main loop.
while running:
    # keep fps
    clock.tick(fps)

    # process event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                player.rect.y -= 1

    # update
    all_sprites.update()
    # draw and render
    screen.fill(Color("grey"))
    all_sprites.draw(screen)

    # flush screen.
    pygame.display.flip()
    # or pygame.display.update()

# quit game.
pygame.quit()
# sys.exit()

