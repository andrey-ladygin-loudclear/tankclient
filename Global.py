from events.NetworkListener import NetworkListener


def init():
    global keyboard, dimensions, layers, objects, collision_manager, TankNetworkListenerConnection, BulletsNetworkListenerConnection, currentPlayerId

    layers = {
        'game': None,
        'panel': None,
        'walls': [],
        'bullets': [],
        'enemies': [],
        'test': [],
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
    ROTATION = 'r'
    TYPE = 'y'
    ID = 'i'
    HEALTH = 'h'
    PARENT_ID = 'pi'

    KVTank = 'k'
    PLAYER = 'p'
    TANK = 't'
    BULLET = 'b'
    STANDART_BULLET = 'sb'
    HEAVY_BULLET = 'hb'
    WALL = 'w'

class NetworkActions:
    INIT = '1'
    TANK_MOVE = '2'
    UPDATE = '3'
    TANK_FIRE = '4'
    DESTROY = '5'
    TEST = '6'
    DAMAGE = '7'
