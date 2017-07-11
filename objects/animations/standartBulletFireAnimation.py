from threading import Timer

import pyglet
from cocos import sprite

import Global


class standartBulletFireAnimation:

    def __init__(self):
        explosion = pyglet.image.load('assets/weapons/fire-small-gun.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 3)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        self.animation = pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .02, loop=False)
        self.anim = sprite.Sprite(self.animation)
        self.anim.scale = 0.2

    def getAnimation(self):
        return self.animation

    def getSprite(self, position, rotation):
        # cos_x = math.cos(math.radians(self.rotation - 180))
        # sin_x = math.sin(math.radians(self.rotation))
        # x = x + self.bullets_fired_offset_x * sin_x + self.bullets_fired_offset_y * cos_x
        # y = y - self.bullets_fired_offset_x * cos_x + self.bullets_fired_offset_y * sin_x
        # anim_x = x + self.bullets_fired_animation_offset_x * sin_x + self.bullets_fired_animation_offset_y * cos_x
        # anim_y = y - self.bullets_fired_animation_offset_x * cos_x + self.bullets_fired_animation_offset_y * sin_x

        self.anim.position = position
        self.anim.rotation = rotation - 90
        return self.anim

    def appendAnimationToLayer(self, position, rotation):
        anim = self.getSprite(position, rotation)
        Global.Layers.game.add(anim)
        t = Timer(self.animation.get_duration(), lambda: Global.Layers.game.remove(anim))
        t.start()