from threading import Timer

import cocos
from cocos.actions import MoveBy, FadeOut

import Global
from factories.TankFactory import TankFactory


class ScreenLayer:
    label = None

    def init(self):
        self.label = cocos.text.Label(
            '1000',
            font_name='Helvetica',
            font_size=16,
            anchor_x='left',  anchor_y='top'
        )
        self.label.position = 0, Global.Config.dimensions['y']
        Global.Layers.globalPanel.add(self.label)

        TankFactory.create()

    def setHealth(self, health):
        self.label.element.text = str(int(round(health)))

    def damage(self, damage, position):
        label = cocos.text.Label(
            '-' + str(int(round(damage))),
            font_name='Helvetica',
            font_size=10,
            color=(255, 0, 0, 255),
            anchor_x='center',  anchor_y='center'
        )
        label.position = position
        Global.Settings.layers.globalPanel.add(label)
        label.do(MoveBy((0, 100), 2) | FadeOut(2))

        t = Timer(2000, lambda: Global.Layers.layers.globalPanel.remove(label))
        t.start()

