import random

import math
from cocos import actions

import Global

class BulletMovingHandlers(actions.Move):
    speed = 800
    angle_of_deflection = 0

    def __init__(self, speed, angle_of_deflection):
        super(BulletMovingHandlers, self).__init__()
        self.speed = speed
        self.angle_of_deflection = angle_of_deflection
        #self.r = random.randrange(-50, 50) / 10

    def step(self, dt):
        super(BulletMovingHandlers, self).step(dt)  # Run step function on the parent class.
        angle = self.target.rotation
        x = self.speed * math.cos(math.radians(angle - 180 + self.angle_of_deflection))
        y = self.speed * math.sin(math.radians(angle + self.angle_of_deflection))
        self.target.velocity = (x, y)
        x, y = self.target.position
        startX, startY = self.target.startPosition

        if self.getLength(x, y, startX, startY) > self.target.fireLength:
            self.target.explosion()

        if y > Global.dimensions['y'] or x > Global.dimensions['x']:
            Global.layers['bullets'].remove(self.target)
            Global.objects['bullets'].remove(self.target)

    def getLength(self, x1, y1, x2, y2):
        deltax = math.pow(x1 - x2, 2)
        deltay = math.pow(y1 - y2, 2)
        return math.sqrt(deltax + deltay)