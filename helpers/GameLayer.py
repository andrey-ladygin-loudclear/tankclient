import PodSixNet
import cocos
from pyglet.window import key

from events.NetworkListener import NetworkListener
from factories.TankFactory import TankFactory
from helpers import Global


class GameLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True
    help = None
    TankNetworkListenerConnection = None

    def __init__(self, CurrentKeyboard):
        super(GameLayer, self).__init__()
        self.schedule(self.update)
        self.CurrentKeyboard = CurrentKeyboard

        self.initHelpText()

    def update(self, dt):
        if not self.TankNetworkListenerConnection: return

        PodSixNet.Connection.connection.Pump()

        if self.TankNetworkListenerConnection:
            self.TankNetworkListenerConnection.Pump()

    def resize(self, width, height):
        self.viewPoint = (width // 2, height // 2)
        self.currentWidth = width
        self.currentHeight = height

    def buttonsHandler(self, dt):
        x_direction = self.CurrentKeyboard[key.NUM_4] - self.CurrentKeyboard[key.NUM_6]
        y_direction = self.CurrentKeyboard[key.NUM_5] - self.CurrentKeyboard[key.NUM_8]
        x, y = self.position

        if x_direction:
            x += x_direction * 20

        if y_direction:
            y += y_direction * 20

        if self.CurrentKeyboard[key.NUM_0]:
            x = y = 0

        if x_direction or y_direction:
            self.set_view(0, 0, self.currentWidth, self.currentHeight, x, y)

        if self.help:
            type = self.selectTank()
            if type: self.connectToServer(type)

        Global.GameLayers.stats.changleStatsPosition(-x, -y, self.currentWidth, self.currentHeight)
        self.setHelpPosition(-x, -y, self.currentWidth, self.currentHeight)

    def connectToServer(self, type):
        self.remove(self.help)
        self.help = None
        Global.TankNetworkListenerConnection = NetworkListener('localhost', 1332, type)
        self.TankNetworkListenerConnection = Global.TankNetworkListenerConnection

    def initHelpText(self):
        self.help = cocos.text.Label(
            self.getHelp(), font_name='Helvetica',
            font_size=16, anchor_x='center',  anchor_y='center'
        )
        self.add(self.help)

    def setHelpPosition(self, x, y, width, height):
        if self.help: self.help.position = (x + width//2, y + height//2)

    def getHelp(self):
        str = "1 - E 100,\n"
        str += '2 - KV 2,\n'
        str += '3 - M 6,\n'
        str += '4 - Pz-G,\n'
        str += '5 - Pz,\n'
        str += '6 - T34,\n'
        str += '7 - Tiger 2,\n'
        str += '8 - VK\n'
        return str

    def selectTank(self):
        type = self.CurrentKeyboard[key._1] * 1 + \
            self.CurrentKeyboard[key._2] * 2 + \
            self.CurrentKeyboard[key._3] * 3 + \
            self.CurrentKeyboard[key._4] * 4 + \
            self.CurrentKeyboard[key._5] * 5 + \
            self.CurrentKeyboard[key._6] * 6 + \
            self.CurrentKeyboard[key._7] * 7 + \
            self.CurrentKeyboard[key._8] * 8

        return type