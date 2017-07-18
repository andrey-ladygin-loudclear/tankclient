import cocos.collision_model as cm
from cocos import sprite


class Tank(sprite.Sprite):
    Gun = None
    canFire = True
    canHeavyFire = True
    new_position = (0, 0)
    old_position = (0, 0)
    velocity = (0, 0)

    id = 0

    maxBulletsHolder = 10
    bulletsHolder = 10
    timeForBulletsHolderReload = 3

    def __init__(self):
        spriteName = 'assets/tank/parts/E-100_1.png'
        spriteGunName = 'assets/tank/parts/E-100_2.png'

        super(Tank, self).__init__(spriteName)

        self.Gun = sprite.Sprite(spriteGunName)
        #self.setGunSprite(spriteGunName)
        #self.setDefaultState()
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )