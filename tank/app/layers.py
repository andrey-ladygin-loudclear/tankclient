import cocos
from cocos.batch import BatchNode

from helpers import Global
from helpers.GameLayer import GameLayer
from helpers.StatsLayer import StatsLayer

bullets = BatchNode()
walls = BatchNode()
backgrounds = BatchNode()
tanks = BatchNode()
stats = StatsLayer()
game = None

def layers_init(CurrentKeyboard):
    game = GameLayer(CurrentKeyboard)

class Layers:
    game = None
    globalPanel = None
    stats = None
    walls = []
    backgrounds = []
    bullets = []
    tanks = None

    def init(self):
        # Create a layer and add a sprite to it.
        self.game = GameLayer(Global.CurrentKeyboard)

        self.bullets = BatchNode()
        self.walls = BatchNode()
        self.backgrounds = BatchNode()
        self.tanks = BatchNode()

        self.game.add(self.backgrounds, z=0)
        self.game.add(self.bullets, z=1)
        self.game.add(self.walls)
        self.game.add(self.tanks)

        self.globalPanel = cocos.layer.Layer()
        self.game.add(self.globalPanel, z=1)

        self.stats = StatsLayer()

    def addTank(self, tank):
        self.tanks.add(tank)
        #self.tanks.add(tank.getGunSprite())
        self.tanks.add(tank.Gun)

    def removeTank(self, tank):
        self.tanks.remove(tank)
        self.tanks.remove(tank.Gun)

    def addAnimation(self, anim):
        self.globalPanel.add(anim)

    def addWall(self, wall, z):
        self.walls.add(wall, z=z)

    def removeWall(self, wall):
        self.walls.remove(wall)

    def removeAnimation(self, anim):
        if anim in self.globalPanel: self.globalPanel.remove(anim)

    def addBullet(self, bullet):
        self.bullets.add(bullet)

    def removeBullet(self, bullet):
        if bullet in self.bullets: self.bullets.remove(bullet)