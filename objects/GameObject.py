from cocos.actions import MoveBy

from factories.BulletFactory import BulletFactory
from factories.TankFactory import TankFactory


class GameObject:
    def update(self, object):
        if object.get('type') == 'tank':
            self.updateTank(object)

        if object.get('type') == 'bullet':
            self.updateBullet(object)

    def updateTank(self, object):
        tank = TankFactory.getOrCreate(object)
        tank.update(object)

    def updateBullet(self, object):
        bullet = BulletFactory.getOrCreate(object)
        bullet.update(object)