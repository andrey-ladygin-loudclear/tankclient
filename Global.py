from events.NetworkBulletsListener import NetworkBulletsListener
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

class NetworkActions:
    INIT = '1'
    TANK_MOVE = '2'
    UPDATE = '3'
    TANK_FIRE = '4'
    DESTROY = '5'
