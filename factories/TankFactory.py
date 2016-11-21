import Global
from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from movingHandlers.UserTankMovingHandlers import UserTankMovingHandlers
from objects.tanks.ETank import ETank
from objects.tanks.KVTank import KVTank


class TankFactory:

    @staticmethod
    def getOrCreate(id, fraction, position, tank_class):
        tank = TankFactory.get(id)

        if tank: return tank

        tank = TankFactory.createTankByClass(tank_class)
        tank.id = id
        tank.setStartPosition(position)
       # tank.fireAnimation()

        if fraction == Global.NetworkDataCodes.PLAYER:
            tank.do(UserTankMovingHandlers())
            Global.objects['players'].append(tank)
            Global.layers['game'].add(tank)
            Global.layers['game'].add(tank.getGunSprite())

        if fraction == 'enemy':
            Global.objects['enemies'].append(tank)
            Global.layers['enemies'].add(tank)
            Global.layers['enemies'].add(tank.getGunSprite())

        return tank

    @staticmethod
    def get(id):
        for player in Global.objects['players']:
            if player.id == id:
                return player

        for enemy in Global.objects['enemies']:
            if enemy.id == id:
                return enemy

        return None

    @staticmethod
    def createTankByClass(tank_class):
        if tank_class == 'ETank':
            return ETank()

        if tank_class == 'KVTank':
            return KVTank()