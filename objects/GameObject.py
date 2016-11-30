from time import time

import cocos
from cocos import draw
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

        # Global.layers['test'] = []
        # x, y = position
        # w, h = (46//2, 46//2)
        # line1 = draw.Line((x - w, y - h), (x + w, y - h), (255,255,255,255))
        # line2 = draw.Line((x - w, y + h), (x + w, y + h), (255,255,255,255))
        # line3 = draw.Line((x + w, y + h), (x - w, y + h), (255,255,255,255))
        # line4 = draw.Line((x - w, y + h), (x + w, y - h), (255,255,255,255))
        # Global.layers['game'].add(line1)
        # Global.layers['game'].add(line2)
        # Global.layers['game'].add(line3)
        # Global.layers['game'].add(line4)

    def test(self, object):
        #Global.layers['panel'] = cocos.layer.Layer()

        position = object.get(Global.NetworkDataCodes.POSITION)

        for point in position:
            line = draw.Line(point[0], point[1], (255,255,255,255))
            #Global.layers['test'].add(line)

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