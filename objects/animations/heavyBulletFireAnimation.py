from threading import Timer

import pyglet
from cocos import sprite

import Global


class heavyBulletFireAnimation:

    def __init__(self):
        explosion = pyglet.image.load('assets/weapons/fire-heavy-gun.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 24)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        self.animation = pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .02, loop=False)
        self.anim = sprite.Sprite(self.animation)
        self.anim.scale = 0.2

    def getAnimation(self):
        return self.animation

    def getSprite(self, position, rotation):
        self.anim.position = position
        self.anim.rotation = rotation - 90
        return self.anim

    def appendAnimationToLayer(self, position, rotation):
        anim = self.getSprite(position, rotation)
        Global.layers['game'].add(anim)
        t = Timer(self.animation.get_duration(), lambda: Global.layers['game'].remove(anim))
        t.start()