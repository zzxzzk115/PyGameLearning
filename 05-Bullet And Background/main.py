'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-03-31 20:48:47
@LastEditors: JackZhang
@LastEditTime: 2020-04-01 23:23:43
'''
# import module.
import pygame, sys, os
from pygame import Color
from game_config import *
from sprites import *
from bullet_controller import BulletController

class Game:
    def __init__(self):
        # initialize the pygame and create the main window.
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(TITLE)
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.running = True
        self.time = 0

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.bullet_controller = BulletController(self)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def pause(self):
        pass

    def update(self):
        self.time += 1
        if self.time >= MAX_TIME:
            self.time = 0
        print('time:' + str(self.time))
        print('group_count:' + str(len(self.all_sprites)))
        self.bullet_controller.update()
        self.all_sprites.update()

    def events(self):
        # process event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False

    def draw(self):
        # draw and render
        # self.screen.fill(Color("grey"))
        background = pygame.image.load(os.path.join(IMG_PATH, "bg.png"))
        self.screen.blit(background,(0,0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        # pygame.display.update()

    def show_splash_screen(self):
        pass

    def show_gameready(self):
        pass

    def show_gameover(self):
        pass

game = Game()
game.show_splash_screen()
while game.running:
    game.show_gameready()
    game.new()
    game.show_gameover()
pygame.quit()
