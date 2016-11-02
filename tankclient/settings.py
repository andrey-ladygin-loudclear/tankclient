from networkEvents.TankNetworkListener import TankNetworkListener


def init():
    global keyboard, dimensions, layers, objects, collision_manager, TankNetworkListenerConnection

    layers = {
        'game': None,
        'walls': [],
        'bullets': [],
        'enemies': [],
    }

    objects = {
        'walls': [],
        'bullets': [],
        'enemies': [],
        'players': [],
    }

    dimensions = {
        'x': 3000,
        'y': 1000,
    }

    #TankNetworkListenerConnection = None
    #TankServer = TankNetworkListener('localhost', 1337)
    #setConnection = ConnectionOnTankServer('localhost', 1331)
    TankNetworkListenerConnection = TankNetworkListener('localhost', 1332)
    keyboard = None
    collision_manager = None

class Actions():
    INIT = '1'
    TANK_MOVE = '2'
    UPDATE = '3'
    TANK_FIRE = '4'
