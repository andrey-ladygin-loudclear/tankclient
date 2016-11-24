from events.NetworkListener import NetworkListener


def init():
    global keyboard, dimensions, layers, objects, collision_manager, TankNetworkListenerConnection, BulletsNetworkListenerConnection

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

    TankNetworkListenerConnection = NetworkListener('localhost', 1332)
    # BulletsNetworkListenerConnection = NetworkBulletsListener('localhost', 1333)
    keyboard = None
    collision_manager = None

class NetworkDataCodes:
    TANK_CLASS = 't'
    FRACTION = 'f'
    GUN_ROTATION = 'g'
    POSITION = 'p'
    LAST_UPDATE_TIME = 'lt'
    ANGLE_OF_DEFLECTION = 'aod'
    ROTATION = 'r'
    TYPE = 'y'
    ID = 'i'
    PARENT_ID = 'pi'

    KVTank = 'k'
    PLAYER = 'p'
    TANK = 't'
    BULLET = 'b'
    STANDART_BULLET = 'sb'
    HEAVY_BULLET = 'hb'

class NetworkActions:
    INIT = '1'
    TANK_MOVE = '2'
    UPDATE = '3'
    TANK_FIRE = '4'
    DESTROY = '5'
