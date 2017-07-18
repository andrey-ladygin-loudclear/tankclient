import PodSixNet
import cocos
from pyglet.window import key

from factories.TankFactory import TankFactory


class GameLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True

    def __init__(self, CurrentKeyboard, TankNetworkListenerConnection):
        super(GameLayer, self).__init__()
        self.schedule(self.update)
        self.CurrentKeyboard = CurrentKeyboard
        self.TankNetworkListenerConnection = TankNetworkListenerConnection

    def update(self, dt):
        PodSixNet.Connection.connection.Pump()

        if self.TankNetworkListenerConnection:
            self.TankNetworkListenerConnection.Pump()

    def resize(self, width, height):
        self.viewPoint = (width // 2, height // 2)
        self.currentWidth = width
        self.currentHeight = height

    def buttonsHandler(self, dt):
        x_direction = self.CurrentKeyboard[key.LEFT] - self.CurrentKeyboard[key.RIGHT]
        y_direction = self.CurrentKeyboard[key.DOWN] - self.CurrentKeyboard[key.UP]
        x, y = self.position

        if x_direction:
            x += x_direction * 20

        if y_direction:
            y += y_direction * 20

        if x_direction or y_direction:
            self.set_view(0, 0, self.currentWidth, self.currentHeight, x, y)

        if self.CurrentKeyboard[key.SPACE]:
            self.set_view(0, 0, self.currentWidth, self.currentHeight, 0, 0)