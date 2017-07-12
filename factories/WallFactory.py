import Global
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class WallFactory:

    @staticmethod
    def get(id):
        for wall in Global.GameObjects:
            if wall.id == id:
                return wall

        return None