'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-04-01 22:49:29
@LastEditors: JackZhang
@LastEditTime: 2020-04-02 13:55:35
'''
from sprites import Bullet, Enemy, Boss
from game_config import *
import random
import pygame, os

class BulletController:
    def __init__(self, game):
        self.game = game
        self.generate_rate = self.game.player.shoot_bullet_rate
        self.game.Timer.set_timer(GEN_BULLET, BULLET_GEN_DURATION)

    def generate_bullet(self):
        bullet = Bullet(self)
        self.game.all_sprites.add(bullet)
        self.game.player.shoot_bullet(bullet)

    def update(self):
        pass

class EnemyController:
    def __init__(self, game):
        self.game = game
        self.game.Timer.set_timer(GEN_ENEMY, ENEMY_GEN_DURATION)
        self.game.Timer.set_timer(GEN_BOSS,  BOSS_GEN_DURATION)
        
    def generate_enemy(self, typeid):
        enemy = None
        if typeid == 1:
            enemy = Enemy(self)
            enemy.rect.center = (random.randint(20, 300), -enemy.rect.height/2)
        elif typeid == 2:
            enemy = Boss(self)
            enemy.rect.center = (random.randint(20, 300), -enemy.rect.height/2)
        self.game.all_sprites.add(enemy)
        enemy.initiated = True
    
    def update(self):
        pass

    
