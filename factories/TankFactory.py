import Global
from objects.tanks.ETank import ETank
from objects.tanks.KVTank import KVTank


class TankFactory:

    @staticmethod
    def getOrCreate(object):
        tank = TankFactory.get(object.get('id'))
        fraction = object.get('fraction')

        if tank: return tank

        tank = TankFactory.createTankByClass(object.get('tankClass'))
        tank.id = object.get('id')

        if fraction == 'player':
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