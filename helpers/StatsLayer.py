from threading import Timer

import cocos
import operator
import pyglet
from cocos.actions import MoveBy, FadeOut
from cocos.layer import ColorLayer
from pyglet.image import load_animation
from pyglet.sprite import Sprite

import Global


class StatsLayer:
    label = None

    def __init__(self):
        self.label = cocos.text.Label(
            '100',
            font_name='Helvetica',
            font_size=16,
            anchor_x='left',  anchor_y='top'
        )
        Global.GameLayers.globalPanel.add(self.label)

    def changleStatsPosition(self, x, y, width, height):
        self.label.position = (x, y + height)

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
        Global.GameLayers.globalPanel.add(label)
        label.do(MoveBy((0, 100), 2) | FadeOut(2))

        t = Timer(2000, lambda: Global.GameLayers.globalPanel.remove(label))
        t.start()