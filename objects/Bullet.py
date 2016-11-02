import math
import random
from threading import Timer

import pyglet

import cocos.collision_model as cm

from cocos import actions
from cocos import sprite
from cocos.actions import Action

import Global
from events.Explosion import Explosion
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers


class Bullet(sprite.Sprite):
    #startPosition = (0, 0)
    #scale = 1
    #damage = 10
    #damageRadius = 20
    #velocity = (0, 0)
    #fireLength = 1000

    def __init__(self, spriteName):
        super(Bullet, self).__init__(spriteName)

    def update_rotation(self, rotation):
        self.rotation = rotation - 90

    def update_position(self, x, y):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))

        x = x + self.bullets_fired_offset_x * sin_x + self.bullets_fired_offset_y * cos_x
        y = y - self.bullets_fired_offset_x * cos_x + self.bullets_fired_offset_y * sin_x

        angle_of_deflection = self.getAngleDeflection()
        self.position = (x, y)
        self.startPosition = (x, y)
        self.do(BulletMovingHandlers(self.speed, angle_of_deflection))

        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

        #animation = pyglet.image.load_animation('sprites/weapons/Explosion2.gif')
        #anim = sprite.Sprite(animation)
        #print(animation.get_duration())
        #anim.sprite_move_action = None
        #animation.(lambda x: Global.layers['game'])

        #animation.get_duration(lambda x: Global.layers['game'].remove(anim))

        #anim.position = (x, y)
        #Global.layers['game'].add(anim)

        anim_x = x + self.bullets_fired_animation_offset_x * sin_x + self.bullets_fired_animation_offset_y * cos_x
        anim_y = y - self.bullets_fired_animation_offset_x * cos_x + self.bullets_fired_animation_offset_y * sin_x

        animation = self.getFireAnimation()
        anim = self.getFireAnimationSprite(animation, anim_x, anim_y)
        Global.layers['game'].add(anim)
        #anim.do(removeAfterComplete())

        t = Timer(animation.get_duration(), lambda: Global.layers['game'].remove(anim))
        t.start()

        #montage Explosion2.gif -tile x1 -geometry +0+0 -alpha On -background "rgba(0,0,0,0.0)" -quality 100 test.png

        #animation = pyglet.image.load_animation('animation.gif')
        #frames = [frame.image for frame in animation.frames]

    def explosion(self):
        animation = self.getExplosionAnimation()
        anim = self.getExplosionAnimationSprite(animation)

        Global.layers['game'].add(anim)

        self.removeAnimation()

        t = Timer(animation.get_duration(), lambda: Global.layers['game'].remove(anim))
        t.start()

        return Explosion(self)

    def getExplosionAnimation(self):
        explosion = pyglet.image.load('sprites/weapons/bullet-explosion.png')
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


class SetBulletMovingHandlers(actions.Move):
    speed = 800

    def __init__(self):
        super(SetBulletMovingHandlers, self).__init__()
        self.r = random.randrange(-50, 50) / 10

    def step(self, dt):
        super(SetBulletMovingHandlers, self).step(dt)  # Run step function on the parent class.
        angle = self.target.rotation
        x = self.speed * math.cos(math.radians(angle - 180 + self.r))
        y = self.speed * math.sin(math.radians(angle + self.r))
        self.target.velocity = (x, y)
        x, y = self.target.position
        startX, startY = self.target.startPosition

        if self.getLength(x, y, startX, startY) > self.target.fireLength:
            self.target.explosion()

        if y > Global.dimensions['y'] or x > Global.dimensions['x']:
            Global.layers['bullets'].remove(self.target)
            Global.objects['bullets'].remove(self.target)

    def getLength(self, x1, y1, x2, y2):
        deltax = math.pow(x1 - x2, 2)
        deltay = math.pow(y1 - y2, 2)
        return math.sqrt(deltax + deltay)