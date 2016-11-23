from time import time

from cocos.actions import MoveBy

import Global
from factories.BulletFactory import BulletFactory
from factories.TankFactory import TankFactory
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers


class GameObject:
    def update(self, object):
        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.KVTank:
            self.updateTank(object, 'KVTank')

    def fire(self, object):
        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET:
            type = 'StandartBullet'

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:
            type = 'HeavyBullet'

        self.createBullet(object, type)

    def updateTank(self, object, tank_class):
        id = object.get(Global.NetworkDataCodes.ID)
        fraction = object.get(Global.NetworkDataCodes.FRACTION)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)
        gun_rotation = object.get(Global.NetworkDataCodes.GUN_ROTATION)

        tank = TankFactory.getOrCreate(id, fraction, position, tank_class)
        tank.update(position, rotation, gun_rotation)

    def createBullet(self, object, bullet_class):
        id = object.get(Global.NetworkDataCodes.ID)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)

        last_update_time = object.get(Global.NetworkDataCodes.LAST_UPDATE_TIME)
        last_update_time = float(last_update_time)

        angle_of_deflection = object.get(Global.NetworkDataCodes.ANGLE_OF_DEFLECTION)

        bullet = BulletFactory.createBulletByClass(bullet_class)
        bullet.id = id
        bullet.position = position
        bullet.start_position = position
        bullet.rotation = rotation
        bullet.last_update_time = last_update_time
        bullet.angle_of_deflection = angle_of_deflection

        BulletFactory.addToObjects(bullet)

        bullet.do(BulletMovingHandlers())
        #bullet.setMovengHendler()
