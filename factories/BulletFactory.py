import Global
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class BulletFactory:

    @staticmethod
    def getOrCreate(object):
        bullet = BulletFactory.get(object.get('id'))

        if bullet: return bullet

        bullet = BulletFactory.createBulletByClass(object.get('typeClass'))
        bullet.id = object.get('id')
        bullet.position = object.get('position')

        Global.objects['bullets'].append(bullet)
        Global.layers['bullets'].add(bullet)

        return bullet

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