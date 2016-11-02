import Global
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class BulletFactory:

    @staticmethod
    def getOrCreate(object):
        bullet = BulletFactory.get(object.get('id'))

        if bullet: return bullet

        bullet = BulletFactory.createBulletByClass(object.get('bulletClass'))
        bullet.id = object.get('id')

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
        if bullet_class == 'heavyBullet':
            return HeavyBullet()

        if bullet_class == 'standartBullet':
            return StandartBullet()