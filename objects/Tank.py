import operator
from cocos import sprite
from cocos.rect import Rect


class Tank(sprite.Sprite):
    Gun = None
    canFire = True
    canHeavyFire = True
    new_position = (0, 0)
    old_position = (0, 0)

    def __init__(self, spriteName):
        super(Tank, self).__init__(spriteName)

    def getRectObject(self):
        x, y = self.position
        bottom_left_x = x - self.width // 2
        bottom_left_y = y - self.height // 2
        return Rect(bottom_left_x, bottom_left_y, self.width, self.height)

    def setGunSprite(self, spriteName):
        self.Gun = sprite.Sprite(spriteName)

    def getGunSprite(self):
        return self.Gun

    def setDefaultState(self):
        self.Gun.image_anchor = (self.Gun.image.width / 2, self.Gun.image.height / 2 + 20)
        self.scale = 0.5
        self.Gun.scale = 0.5
        self.rotation = 180
        self.Gun.offset_rotation = 0

    def getMoveBy(self, new_position):
        return tuple(map(operator.sub, self.position, new_position))


    def acceptFire(self):
        self.canFire = True

    def acceptHeavyFire(self):
        self.canHeavyFire = True