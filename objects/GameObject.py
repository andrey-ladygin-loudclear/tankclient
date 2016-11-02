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
        tank.rotation = object.get('rotation')
        move_to = tank.getMoveBy(object.get('position'))
        tank.do(MoveBy(move_to, 1))

    def updateBullet(self, object):
        bullet = BulletFactory.getOrCreate(object)
        bullet.rotation = object.get('rotation')
        bullet.do(MoveBy(object.get('moveTo'), 1))