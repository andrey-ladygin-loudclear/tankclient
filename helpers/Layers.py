import cocos
from cocos.batch import BatchNode

from helpers import Global
from helpers.GameLayer import GameLayer


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
        self.game = GameLayer(Global.CurrentKeyboard, Global.TankNetworkListenerConnection)

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

        print 'INIT'

        #self.stats = StatsLayer()

    def addTank(self, tank):
        self.tanks.add(tank)
        #self.tanks.add(tank.getGunSprite())
        self.tanks.add(tank.Gun)

    def addAnimation(self, anim):
        self.globalPanel.add(anim)

    def addWall(self, wall):
        self.walls.add(wall)

    def removeWall(self, wall):
        self.walls.remove(wall)

    def removeAnimation(self, anim):
        self.globalPanel.remove(anim)

    def addBullet(self, bullet):
        self.bullets.add(bullet)

    def removeBullet(self, bullet):
        self.bullets.remove(bullet)