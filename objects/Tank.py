import operator
from cocos import sprite
from cocos.actions import MoveBy
from cocos.rect import Rect

import Global


class Tank(sprite.Sprite):
    Gun = None
    canFire = True
    canHeavyFire = True
    new_position = (0, 0)
    old_position = (0, 0)
    velocity = (0, 0)

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

    def update(self, object):
        self.rotation = object.get('rotation')
        self.Gun.rotation = object.get('gun_rotation')

        move_to = self.getMoveBy(object.get('position'))
        self.do(MoveBy(move_to, .1))
        self.Gun.do(MoveBy(move_to, .1))

    def setDefaultState(self):
        self.Gun.image_anchor = (self.Gun.image.width / 2, self.Gun.image.height / 2 + 20)
        self.scale = 0.5
        self.Gun.scale = 0.5
        self.rotation = 180
        self.Gun.gun_rotation = 0
        self.Gun.position = self.position
        self.Gun.rotation = self.rotation + self.Gun.gun_rotation

    def getMoveBy(self, new_position):
        curr_x, curr_y = self.position
        new_x, new_y = new_position
        return (new_x - curr_x, new_y - curr_y)

    def setStartPosition(self, position):
        self.position = position
        self.Gun.position = self.position

    def acceptFire(self):
        self.canFire = True

    def acceptHeavyFire(self):
        self.canHeavyFire = True

    def bullet_fire(self, bullet):
        print(bullet.position)
        Global.TankNetworkListenerConnection.Send({
            'action': Global.NetworkActions.TANK_FIRE,
            'type': bullet.type,
            'pos': bullet.position,
            'rotation': bullet.rotation,
            'id': self.id
        })