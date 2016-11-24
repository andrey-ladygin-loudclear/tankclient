import Global
from objects.animations.standartBulletFireAnimation import standartBulletFireAnimation
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class AnimationFactory:

    @staticmethod
    def createAnimationByBulletClass(bullet_class):
        if bullet_class == 'HeavyBullet':
            return HeavyBullet()

        if bullet_class == 'StandartBullet':
            return standartBulletFireAnimation()