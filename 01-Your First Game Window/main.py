'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-03-31 20:48:47
@LastEditors: JackZhang
@LastEditTime: 2020-03-31 21:24:19
'''
# import module.
import pygame, sys
from pygame import Color

# set up custom game window size.
window_size = width, height = 400, 300

# initialize the pygame and create the main window.
pygame.init()
pygame.display.set_caption("pygame window")
screen = pygame.display.set_mode(window_size)

# set frame-per-second and the clock.
fps = 30
clock = pygame.time.Clock()

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
            if(event.key == pygame.K_ESCAPE):
                running = False

    # update

    # draw and render
    screen.fill(Color("yellow"))
    
    # flush screen.
    pygame.display.flip()
    # or pygame.display.update()

# quit game.
pygame.quit()
# sys.exit()

