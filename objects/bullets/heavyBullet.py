
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

    speed = 800

    bullets_fired_offset_x = 0
    bullets_fired_offset_y = 20

    bullets_fired_animation_offset_x = 0
    bullets_fired_animation_offset_y = 35

    def __init__(self):
        super(HeavyBullet, self).__init__(self.spriteName)

    def getAngleDeflection(self):
        return random.randrange(-50, 50) / 10

    def getFireAnimation(self):
        explosion = pyglet.image.load('assets/weapons/fire-heavy-gun.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 24)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        return pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .02, loop=False)

    def getFireAnimationSprite(self, animation, anim_x, anim_y):
        anim = sprite.Sprite(animation)
        anim.position = (anim_x, anim_y)
        anim.rotation = self.rotation - 90
        anim.scale = 0.2
        return anim

    def removeAnimation(self):
        if self in Global.layers['bullets']: Global.layers['bullets'].remove(self)
        if self in Global.objects['bullets']: Global.objects['bullets'].remove(self)

    def getExplosionAnimation(self):
        explosion = pyglet.image.load('assets/weapons/bullet-explosion.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 20)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        return pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .05, loop=False)

    def getExplosionAnimationSprite(self, animation):
        anim = sprite.Sprite(animation)
        anim.position = self.position
        anim.rotation = self.rotation - 90
        anim.image_anchor = (animation.get_max_width() / 2, animation.get_max_height() / 4)
        anim.scale = 0.5
        return anim

class removeAfterComplete(Action):
    def step(self, dt):
        super(removeAfterComplete, self).step(dt)