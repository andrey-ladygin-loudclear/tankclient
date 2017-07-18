from helpers import Global


class Objects:
    game = None
    globalPanel = None
    walls = []
    backgrounds = []
    bullets = []
    tanks = []

    def addTank(self, tank):
        self.tanks.append(tank)
        Global.CollisionManager.add(tank)
        Global.GameLayers.addTank(tank)

    def addAnimation(self, anim):
        #self.globalPanel.add(anim)
        Global.GameLayers.addAnimation(anim)

    def addWall(self, wall):
        self.walls.add(wall)

    def removeWall(self, wall):
        self.walls.remove(wall)

    def removeAnimation(self, anim):
        self.globalPanel.remove(anim)

    def addBullet(self, bullet):
        self.bullets.append(bullet)
        Global.GameLayers.addBullet(bullet)

    def removeBullet(self, bullet):
        self.bullets.remove(bullet)
        Global.GameLayers.addBullet(bullet)