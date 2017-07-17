import math
from cocos import sprite
import cocos.collision_model as cm

import Global


class BrickWall(sprite.Sprite):
    spriteName = 'assets/walls/sprite_bricks_tutorial_1.png'
    health = 20
    id = 0

    def __init__(self, sprite):
        super(BrickWall, self).__init__(sprite)

    def update_position(self, position):
        self.position = position
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def damage(self, bullet):
        x, y = self.position
        x2, y2 = bullet.position
        deltax = math.pow(x - x2, 2)
        deltay = math.pow(y - y2, 2)
        delta = (deltax + deltay) / 3
        range = math.sqrt(max(delta / self.width, 1))
        #print('range: ' + str(range))
        #print('damage: ' + str(bullet.damage * bullet.damage / range ))
        self.health -= bullet.damage / range

    def destroy(self):
        if self in Global.GameObjects: Global.GameObjects.remove(self)
        if self in Global.GameLayers.walls: Global.GameLayers.removeWall(self)