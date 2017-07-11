import Global
from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from movingHandlers.LocalTankMovingHandlers import LocalTankMovingHandlers
from movingHandlers.UserTankMovingHandlers import UserTankMovingHandlers
from objects.tanks.ETank import ETank
from objects.tanks.KVTank import KVTank


class TankFactory:

    @staticmethod
    def create():
        tank = ETank()
        tank.id = 1
        tank.setStartPosition((100, 100))
        #tank.do(UserTankMovingHandlers())
        tank.do(LocalTankMovingHandlers())
        Global.Layers.tanks.add(tank)
        Global.Layers.tanks.add(tank.getGunSprite())

    @staticmethod
    def getOrCreate(id, fraction, position, tank_class):
        tank = TankFactory.get(id)

        if tank: return tank

        tank = TankFactory.createTankByClass(tank_class)
        tank.id = id
        tank.setStartPosition(position)
       # tank.fireAnimation()

        if fraction == Global.NetworkDataCodes.PLAYER:
            if tank.id == Global.CurrentPlayerId:
                tank.do(UserTankMovingHandlers())

        Global.GameLayers.addTank(tank)
        Global.GameObjects.append(tank)

        return tank

    @staticmethod
    def get(id):
        for tank in Global.GameObjects:
            if tank.id == id:
                return tank

        return None

    @staticmethod
    def createTankByClass(tank_class):
        if tank_class == 'ETank':
            return ETank()

        if tank_class == 'KVTank':
            return KVTank()