import Global
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class BulletFactory:

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
        Global.objects['bullets'].append(bullet)
        Global.layers['bullets'].add(bullet)

    @staticmethod
    def get(id):
        for bullet in Global.objects['bullets']:
            if bullet.id == id:
                return bullet

        return None

    @staticmethod
    def createBulletByClass(bullet_class):
        if bullet_class == 'HeavyBullet':
            return HeavyBullet()

        if bullet_class == 'StandartBullet':
            return StandartBullet()