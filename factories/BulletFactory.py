import Global
from factories.AnimationFactory import AnimationFactory
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class BulletFactory:

    @staticmethod
    def create(bullet, id, tank, position, rotation, last_update_time):
        bullet.id = id
        bullet.parent_id = tank.id
        bullet.position = position
        bullet.start_position = position
        bullet.rotation = rotation
        bullet.last_update_time = last_update_time

        AnimationFactory.create(bullet, tank, rotation)
        BulletFactory.addToObjects(bullet)
        bullet.do(BulletMovingHandlers())
        return bullet






    @staticmethod
    def getOrCreate(id, position, rotation, bullet_class):
        bullet = BulletFactory.get(id)

        if bullet: return bullet

        bullet = BulletFactory.createBulletByClass(bullet_class)
        bullet.id = id
        bullet.position = position
        bullet.rotation = rotation

        BulletFactory.addToObjects(bullet)

        return bullet

    @staticmethod
    def addToObjects(bullet):
        Global.GameObjects.append(bullet)
        Global.GameLayers.addBullet(bullet)

    @staticmethod
    def get(id):
        for bullet in Global.GameObjects:
            if bullet.id == id:
                return bullet

        return None

    @staticmethod
    def createBulletByClass(bullet_class):
        if bullet_class == 'HeavyBullet':
            return HeavyBullet()

        if bullet_class == 'StandartBullet':
            return StandartBullet()