class Layers:
    game = None
    globalPanel = None
    walls = []
    backgrounds = []
    bullets = []
    tanks = []

    def addTank(self, tank):
        self.tanks.add(tank)
        self.tanks.add(tank.getGunSprite())

    def addAnimation(self, anim):
        self.globalPanel.add(anim)

    def addWall(self, wall):
        self.walls.add(wall)

    def removeWall(self, wall):
        self.walls.add(wall)

    def removeAnimation(self, anim):
        self.globalPanel.add(anim)

    def addBullet(self, bullet):
        self.bullets.add(bullet)

    def removeBullet(self, bullet):
        self.bullets.remove(bullet)