
import random

import pyglet
import Global
from cocos import sprite
from cocos.actions import Action

from objects.Bullet import Bullet


class StandartBullet(Bullet):
    type = 'StandartBullet'
    spriteName = 'assets/bullets/bullet.png'

    scale = 0.8
    damage = 1
    damageRadius = 5
    velocity = (0, 0)
    fireLength = 1000

    speed = 300

    bullets_fired_offset_x = 6
    bullets_fired_offset_y = 20

    bullets_fired_animation_offset_x = 0
    bullets_fired_animation_offset_y = 5

    def __init__(self):
        super(StandartBullet, self).__init__(self.spriteName)

    def getAngleDeflection(self):
        return random.randrange(-100, 100) / 10

    def getFireAnimation(self):
        explosion = pyglet.image.load('assets/weapons/fire-small-gun.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 3)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        return pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .02, loop=False)

    def getFireAnimationSprite(self, animation, anim_x, anim_y):
        anim = sprite.Sprite(animation)
        anim.position = (anim_x, anim_y)
        anim.rotation = self.rotation - 90
        anim.scale = 0.2
        return anim

    def getExplosionAnimation(self):
        explosion = pyglet.image.load('assets/weapons/standart-bullet-explode.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 12)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        return pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .05, loop=False)

    def getExplosionAnimationSprite(self, animation):
        anim = sprite.Sprite(animation)
        anim.position = self.position
        anim.rotation = self.rotation - 90
        anim.image_anchor = (animation.get_max_width() / 2, animation.get_max_height() / 2)
        anim.scale = 0.1
        return anim

    def removeAnimation(self):
        if self in Global.layers['bullets']: Global.layers['bullets'].remove(self)
        if self in Global.objects['bullets']: Global.objects['bullets'].remove(self)

class removeAfterComplete(Action):
    def step(self, dt):
        super(removeAfterComplete, self).step(dt)
