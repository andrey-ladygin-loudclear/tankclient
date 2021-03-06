
import random

import pyglet

from cocos import sprite
from cocos.actions import Action

import Global
from objects.Bullet import Bullet


class HeavyBullet(Bullet):
    type = 'HeavyBullet'
    spriteName = 'assets/bullets/bullet-origin.png'
    startPosition = (0, 0)

    scale = 1
    damage = 10
    damageRadius = 20
    velocity = (0, 0)
    fireLength = 1000

    speed = 600

    def __init__(self):
        super(HeavyBullet, self).__init__(self.spriteName)

    def removeAnimation(self):
        if self in Global.layers['bullets']: Global.layers['bullets'].remove(self)
        if self in Global.objects['bullets']: Global.objects['bullets'].remove(self)
