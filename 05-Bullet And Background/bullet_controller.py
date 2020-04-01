'''
@Descripttion: 
@version: 
@Author: JackZhang
@Date: 2020-04-01 22:49:29
@LastEditors: JackZhang
@LastEditTime: 2020-04-01 23:22:57
'''
from sprites import Bullet

class BulletController:
    def __init__(self, game):
        self.game = game
        self.generate_rate = self.game.player.shoot_bullet_rate
        pass

    def generate_bullet(self):
        bullet = Bullet(self)
        self.game.all_sprites.add(bullet)
        self.game.player.shoot_bullet(bullet)

    def update(self):
        if self.game.time % self.generate_rate == 0:
            self.generate_bullet()