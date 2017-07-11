class Objects:
    id = 0
    objects = []

    def addObject(self, object, id=None):
        object.id = self.id
        self.objects.add(tank)
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