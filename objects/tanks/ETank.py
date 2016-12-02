from threading import Timer
import cocos.collision_model as cm

import Global
from objects.Tank import Tank
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class ETank(Tank):
    spriteName = 'assets/tank/parts/E-100_1.png'
    spriteGunName = 'assets/tank/parts/E-100_2.png'

    bulletFreezTime = 0.08
    heavyBulletFreezTime = 1

    speed_acceleration = 4
    max_speed = 70
    rotation_speed = 1.2
    gun_rotation_speed = 1.2

    def __init__(self):
        super(ETank, self).__init__(self.spriteName)
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

            bullet = HeavyBullet()
            bullet.rotation = self.Gun.getRotation() + self.Gun.getHeavyGunAngleDeflection()
            bullet.position = self.Gun.heavyFirePosition()

            self.bullet_fire(bullet)

            t = Timer(self.heavyBulletFreezTime, self.acceptHeavyFire)
            t.start()


    def fire(self):
        if self.canFire:
            self.canFire = False

            bullet = StandartBullet()
            bullet.rotation = self.Gun.getRotation() + self.Gun.getStandartGunAngleDeflection()
            bullet.position = self.Gun.standartFirePosition()

            self.bullet_fire(bullet)

            t = Timer(self.bulletFreezTime, self.acceptFire)
            t.start()