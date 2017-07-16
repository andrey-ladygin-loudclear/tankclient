import operator

import math
from threading import Timer
from time import time

import cocos
from cocos import sprite
from cocos.actions import MoveBy, Accelerate, Rotate, MoveTo, RotateTo
from cocos.rect import Rect
from threading import Timer
import cocos.collision_model as cm

from factories.BulletFactory import BulletFactory
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet
import Global

import Global
from objects.Gun import Gun
from objects.animations.standartBulletFireAnimation import standartBulletFireAnimation
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet

import cocos.collision_model as cm

class Tank(sprite.Sprite):
    Gun = None
    canFire = True
    canHeavyFire = True
    new_position = (0, 0)
    old_position = (0, 0)
    velocity = (0, 0)

    id = 0

    maxBulletsHolder = 10
    bulletsHolder = 10
    timeForBulletsHolderReload = 3

    def __init__(self, spriteName):
        super(Tank, self).__init__(spriteName)
        self.setGunSprite(self.spriteGunName)
        self.setDefaultState()
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def getRectObject(self):
        x, y = self.position
        bottom_left_x = x - self.width // 2
        bottom_left_y = y - self.height // 2
        return Rect(bottom_left_x, bottom_left_y, self.width, self.height)

    def setGunSprite(self, spriteName):
        self.Gun = Gun(spriteName)

    def getGunSprite(self):
        return self.Gun

    def update(self, position, rotation, gun_rotation):
        self.rotation = rotation
        move_to = self.getMoveBy(position)

        #self.Gun.rotation = gun_rotation

        action = RotateTo(gun_rotation, 0.2)
        self.Gun.do(action)

        print move_to

        self.do(MoveBy(move_to, 0.1))
        self.Gun.do(MoveBy(move_to, 0.1))

    def setDefaultState(self):
        self.Gun.image_anchor = (self.Gun.image.width / 2, self.Gun.image.height / 2 + 20)
        self.scale = 0.5
        self.Gun.scale = 0.5
        self.rotation = 180
        self.Gun.gun_rotation = self.rotation
        self.Gun.position = self.position
        self.Gun.rotation = self.rotation + self.Gun.gun_rotation

    def getMoveBy(self, new_position):
        curr_x, curr_y = self.position
        new_x, new_y = new_position
        return (new_x - curr_x, new_y - curr_y)

    def setStartPosition(self, position):
        self.position = position
        self.Gun.position = self.position

    def acceptFire(self):
        self.canFire = True

    def bulletsHolderReload(self):
        self.canFire = True
        self.bulletsHolder = self.maxBulletsHolder

    def acceptHeavyFire(self):
        self.canHeavyFire = True

    def bullet_fire(self, bullet):
        Global.TankNetworkListenerConnection.Send({
            'action': Global.NetworkActions.TANK_FIRE,
            'type': bullet.type,
            'pos': bullet.position,
            'rotation': bullet.rotation,
            'id': self.id
        })

    def heavy_fire(self, position=None, rotation=None, last_update_time=None):
        if self.canHeavyFire:
            self.canHeavyFire = False

            #id = 1

            # if not position: position = self.Gun.heavyFirePosition()
            # if not rotation: rotation = self.Gun.getRotation() + self.Gun.getHeavyGunAngleDeflection()
            # if not last_update_time: last_update_time = time()
            #
            # bullet = BulletFactory.create(HeavyBullet(), id, self, position, rotation, last_update_time)

            bullet = HeavyBullet()
            bullet.rotation = self.Gun.getRotation() + self.Gun.getHeavyGunAngleDeflection()
            bullet.position = self.Gun.heavyFirePosition()

            self.bullet_fire(bullet)

            t = Timer(self.heavyBulletFreezTime, self.acceptHeavyFire)
            t.start()


    def fire(self, position=None, rotation=None, last_update_time=None):
        if self.canFire:
            self.canFire = False
            self.bulletsHolder -= 1

            #id = 1

            bullet = StandartBullet()
            bullet.rotation = self.Gun.getRotation() + self.Gun.getStandartGunAngleDeflection()
            bullet.position = self.Gun.standartFirePosition()
            self.bullet_fire(bullet)

            # if not position: position = self.Gun.heavyFirePosition()
            # if not rotation: rotation = self.Gun.getRotation() + self.Gun.getHeavyGunAngleDeflection()
            # if not last_update_time: last_update_time = time()
            #
            # bullet = BulletFactory.create(StandartBullet(), id, self, position, rotation, last_update_time)

            if not self.bulletsHolder:
                t = Timer(self.timeForBulletsHolderReload, self.bulletsHolderReload)
                t.start()
                return

            t = Timer(self.bulletFreezTime, self.acceptFire)
            t.start()