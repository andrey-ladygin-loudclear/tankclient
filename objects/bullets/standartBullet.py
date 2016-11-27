
import random

import pyglet
import Global
from cocos import sprite
from cocos.actions import Action

from objects.Bullet import Bullet


class StandartBullet(Bullet):
    type = 'StandartBullet'
    spriteName = 'assets/bullets/bullet.png'
    startPosition = (0, 0)

    scale = 0.8
    damage = 1
    damageRadius = 5
    velocity = (0, 0)
    fireLength = 1000

    speed = 300

    def __init__(self):
        super(StandartBullet, self).__init__(self.spriteName)

    def getAngleDeflection(self):
        return random.randrange(-1000, 1000) / 100

    def removeAnimation(self):
        if self in Global.layers['bullets']: Global.layers['bullets'].remove(self)
        if self in Global.objects['bullets']: Global.objects['bullets'].remove(self)
