from threading import Timer

import cocos.collision_model as cm

import Global
from objects.Tank import Tank
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class KVTank(Tank):
    spriteName = 'assets/tank/parts/KV-2_1.png'
    spriteGunName = 'assets/tank/parts/KV-2_2.png'

    bulletFreezTime = 0.08
    heavyBulletFreezTime = 1

    speed_acceleration = 4
    max_speed = 70
    rotation_speed = 1.2
    gun_rotation_speed = 1.2

    #damage = 10
    #damageRadius = 20
    #fireLength = 1000
    #bulletSpeed = 800

    def __init__(self):
        super(KVTank, self).__init__(self.spriteName)
        self.setGunSprite(self.spriteGunName)
        self.setDefaultState()
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def heavy_fire(self):
        if self.canHeavyFire:
            self.canHeavyFire = False

            x, y = self.Gun.position

            bullet = HeavyBullet()
            bullet.update_rotation(self.Gun.rotation)
            bullet.update_position(x, y)

            self.bullet_fire(bullet)

            t = Timer(self.heavyBulletFreezTime, self.acceptHeavyFire)
            t.start()


    def fire(self):
        if self.canFire:
            self.canFire = False

            x, y = self.Gun.position

            bullet = StandartBullet()
            bullet.update_rotation(self.Gun.rotation)
            bullet.update_position(x, y)

            self.bullet_fire(bullet)

            t = Timer(self.bulletFreezTime, self.acceptFire)
            t.start()