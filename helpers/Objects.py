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

    def getTank(self, id):
        for tank in self.tanks:
            if tank.id == id: return tank

        return None

    def getTanks(self):
        return self.tanks

    def removeTank(self, tank):
        self.tanks.remove(tank)
        if tank in Global.GameLayers.tanks: Global.GameLayers.removeTank(tank)

    def addAnimation(self, anim):
        #self.globalPanel.add(anim)
        Global.GameLayers.addAnimation(anim)

    def addWall(self, wall):
        self.walls.append(wall)

    def getWalls(self):
        return self.walls

    def getWall(self, id):
        for wall in self.walls:
            if wall.id == id: return wall

        return None

    def removeWall(self, wall):
        self.walls.remove(wall)
        if wall in Global.GameLayers.walls: Global.GameLayers.removeWall(wall)

    def removeAnimation(self, anim):
        self.globalPanel.remove(anim)

    def addBullet(self, bullet):
        self.bullets.append(bullet)
        Global.GameLayers.addBullet(bullet)

    def getBullet(self, id):
        for bullet in self.bullets:
            if bullet.id == id: return bullet

        return None

    def removeBullet(self, bullet):
        self.bullets.remove(bullet)
        Global.GameLayers.addBullet(bullet)