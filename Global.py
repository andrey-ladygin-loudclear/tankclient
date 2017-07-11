from repositories.Layers import Layers
from events.NetworkListener import NetworkListener
from objects.ScreenLayer import ScreenLayer


CurrentPlayer = None
CurrentScreen = ScreenLayer()
CurrentKeyboard = None
TankNetworkListenerConnection = NetworkListener('localhost', 1332)
CollisionManager = None
CurrentPlayerId = 0
GameLayers = Layers()
GameObjects = []


class Config:
    dimensions = {
        'x': 3000,
        'y': 1000,
    }


class NetworkDataCodes:
    TANK_CLASS = 't'
    FRACTION = 'f'
    GUN_ROTATION = 'g'
    POSITION = 'p'
    LAST_UPDATE_TIME = 'lt'
    ROTATION = 'r'
    TYPE = 'y'
    SRC = 's'
    ID = 'i'
    HEALTH = 'h'
    DAMAGE = 'd'
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
