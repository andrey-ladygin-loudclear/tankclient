from time import time

import cocos
from cocos import draw
from cocos.actions import MoveBy

import Global
from factories.AnimationFactory import AnimationFactory
from factories.BulletFactory import BulletFactory
from factories.TankFactory import TankFactory
from factories.WallFactory import WallFactory
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers
from objects.animations.ExplosionHeavyBulletAnimation import explosionHeavyBulletAnimation
from objects.animations.ExplosionStandartBulletAnimation import explosionStandartBulletAnimation
from objects.animations.heavyBulletFireAnimation import heavyBulletFireAnimation
from objects.animations.standartBulletFireAnimation import standartBulletFireAnimation
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class GameObject:
    testObjects = []

    def update(self, object):
        tank_class = 'KVTank'

        if object.get(Global.NetworkDataCodes.TYPE) != Global.NetworkDataCodes.KVTank:
            tank_class = 'ETank'

        self.updateTank(object, tank_class)

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

        for tobj in self.testObjects:
            self.testObjects.remove(tobj)
            Global.layers['panel'].remove(tobj)

        position = object.get(Global.NetworkDataCodes.POSITION)

        for point in position:
            line = draw.Line(point[0], point[1], (255,255,255,255))
            self.testObjects.append(line)
            Global.layers['panel'].add(line)

    def fire(self, object):
        id = object.get(Global.NetworkDataCodes.ID)
        parent_id = object.get(Global.NetworkDataCodes.PARENT_ID)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)

        last_update_time = object.get(Global.NetworkDataCodes.LAST_UPDATE_TIME)
        last_update_time = float(last_update_time)

        tank = TankFactory.get(parent_id)

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET:
            #tank.fire(position, rotation, last_update_time)
            bullet = BulletFactory.create(StandartBullet(), id, tank, position, rotation, last_update_time)

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:
            #tank.heavy_fire(position, rotation, last_update_time)
            bullet = BulletFactory.create(HeavyBullet(), id, tank, position, rotation, last_update_time)


    def damage(self, object):
        id = object.get(Global.NetworkDataCodes.ID)
        dmg = object.get(Global.NetworkDataCodes.DAMAGE)

        tank = TankFactory.get(id)
        Global.CurrentScreen.damage(dmg, tank.position)

        if id == Global.CurrentPlayerId:
            health = object.get(Global.NetworkDataCodes.HEALTH)
            Global.CurrentScreen.setHealth(health)

    def destroy(self, object):
        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.WALL:
            id = object.get(Global.NetworkDataCodes.ID)
            #position = object.get(Global.NetworkDataCodes.POSITION)
            wall = WallFactory.get(id)
            wall.destroy()

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET or \
                        object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:

            id = object.get(Global.NetworkDataCodes.ID)
            position = object.get(Global.NetworkDataCodes.POSITION)
            bullet = BulletFactory.get(id)

            #print 'destroy bullet', id

            if not bullet: return

            bullet.destroy()

            if isinstance(bullet, StandartBullet):
                animation = explosionStandartBulletAnimation()
            else:
                animation = explosionHeavyBulletAnimation()

            animation.appendAnimationToLayer(position, bullet.rotation)