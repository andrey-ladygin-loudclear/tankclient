from cocos.actions import MoveBy

import Global
from factories.BulletFactory import BulletFactory
from factories.TankFactory import TankFactory


class GameObject:
    def update(self, object):
        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.KVTank:
            self.updateTank(object, 'KVTank')

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:
            self.updateBullet(object, 'HeavyBullet')

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET:
            self.updateBullet(object, 'StandartBullet')

    def updateTank(self, object, tank_class):
        id = object.get(Global.NetworkDataCodes.ID)
        fraction = object.get(Global.NetworkDataCodes.FRACTION)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)
        gun_rotation = object.get(Global.NetworkDataCodes.GUN_ROTATION)

        tank = TankFactory.getOrCreate(id, fraction, position, tank_class)
        tank.update(position, rotation, gun_rotation)

    def updateBullet(self, object, bullet_class):
        id = object.get(Global.NetworkDataCodes.ID)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)

        bullet = BulletFactory.getOrCreate(id, position, bullet_class)
        bullet.update(position, rotation)