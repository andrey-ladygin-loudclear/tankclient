from events.NetworkListener import NetworkListener


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

    TankNetworkListenerConnection = NetworkListener('localhost', 1332)
    keyboard = None
    collision_manager = None

class Actions:
    INIT = '1'
    TANK_MOVE = '2'
    UPDATE = '3'
    TANK_FIRE = '4'
