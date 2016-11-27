from time import time

from cocos.actions import MoveBy

import Global
from factories.AnimationFactory import AnimationFactory
from factories.BulletFactory import BulletFactory
from factories.TankFactory import TankFactory
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers
from objects.animations.ExplosionHeavyBulletAnimation import explosionHeavyBulletAnimation
from objects.animations.ExplosionStandartBulletAnimation import explosionStandartBulletAnimation
from objects.animations.heavyBulletFireAnimation import heavyBulletFireAnimation
from objects.animations.standartBulletFireAnimation import standartBulletFireAnimation
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class GameObject:
    def update(self, object):
        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.KVTank:
            self.updateTank(object, 'KVTank')

    def updateTank(self, object, tank_class):
        id = object.get(Global.NetworkDataCodes.ID)
        fraction = object.get(Global.NetworkDataCodes.FRACTION)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)
        gun_rotation = object.get(Global.NetworkDataCodes.GUN_ROTATION)

        tank = TankFactory.getOrCreate(id, fraction, position, tank_class)
        tank.update(position, rotation, gun_rotation)

    def fire(self, object):
        id = object.get(Global.NetworkDataCodes.ID)
        parent_id = object.get(Global.NetworkDataCodes.PARENT_ID)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)

        last_update_time = object.get(Global.NetworkDataCodes.LAST_UPDATE_TIME)
        last_update_time = float(last_update_time)

        angle_of_deflection = object.get(Global.NetworkDataCodes.ANGLE_OF_DEFLECTION)

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET:
            bullet = StandartBullet()

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:
            bullet = HeavyBullet()

        bullet.id = id
        bullet.parent_id = parent_id
        bullet.position = position
        bullet.start_position = position
        bullet.rotation = rotation
        bullet.last_update_time = last_update_time
        bullet.angle_of_deflection = angle_of_deflection

        firedTank = TankFactory.get(parent_id)

        if isinstance(bullet, StandartBullet):
            animation = standartBulletFireAnimation()
            animatiom_position = firedTank.Gun.standartFireAnimationPosition()
        else:
            animation = heavyBulletFireAnimation()
            animatiom_position = firedTank.Gun.heavyFireAnimationPosition()

        animation.appendAnimationToLayer(animatiom_position, rotation)

        BulletFactory.addToObjects(bullet)

        bullet.do(BulletMovingHandlers())
        #bullet.setMovengHendler()

    def destroy(self, object):
        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET or \
                        object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:
            id = object.get(Global.NetworkDataCodes.ID)
            position = object.get(Global.NetworkDataCodes.POSITION)
            bullet = BulletFactory.get(id)
            bullet.destroy()

            if isinstance(bullet, StandartBullet):
                animation = explosionStandartBulletAnimation()
            else:
                animation = explosionHeavyBulletAnimation()

            animation.appendAnimationToLayer(position, bullet.rotation)