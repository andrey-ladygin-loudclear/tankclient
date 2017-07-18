from helpers import Global
from movingHandlers.LocalTankMovingHandlers import LocalTankMovingHandlers
from objects.Tank import Tank


class TankFactory:

    @staticmethod
    def create():
        tank = Tank()
        tank.id = 1
        #tank.setStartPosition((100, 100))
        tank.do(LocalTankMovingHandlers())

        Global.GameObjects.addTank(tank)
        return tank

    @staticmethod
    def getOrCreate(id, fraction, position, tank_class):
        # print "Get Tank id: ", id, position
        tank = TankFactory.get(id)

        if tank: return tank

        tank = TankFactory.createTankByClass(tank_class)
        tank.id = id
        tank.setStartPosition(position)
       # tank.fireAnimation()

        # if fraction == Global.NetworkDataCodes.PLAYER:
        #     if tank.id == Global.CurrentPlayerId:
        #         tank.do(UserTankMovingHandlers())

        Global.GameLayers.addTank(tank)
        Global.GameObjects.append(tank)

        return tank

    @staticmethod
    def get(id):
        for tank in Global.GameObjects:
            if tank.id == id:
                return tank

        return None

    # @staticmethod
    # def createTankByClass(tank_class):
    #     if tank_class == 'ETank':
    #         return ETank()
    #
    #     if tank_class == 'KVTank':
    #         return KVTank()