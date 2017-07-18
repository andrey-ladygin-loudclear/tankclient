import cocos.collision_model as cm
from cocos import sprite

from objects.Gun import Gun


class Tank(sprite.Sprite):
    Gun = None
    gun_rotation = 0
    id = 0

    speed = 20

    old_position = (0, 0)
    velocity = (0, 0)

    maxBulletsHolder = 10
    bulletsHolder = 10
    timeForBulletsHolderReload = 3

    def __init__(self):
        spriteName = 'assets/tank/parts/E-100_1.png'
        spriteGunName = 'assets/tank/parts/E-100_2.png'
        self.Gun = Gun(spriteGunName)
        super(Tank, self).__init__(spriteName)

        self.scale = self.Gun.scale = 0.5

        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def _update_position(self):
        super(Tank, self)._update_position()
        self.Gun.position = self.position
        self.Gun.rotation = self.rotation + self.gun_rotation

        # self.rotation = 180
        # self.Gun.position = self.position
        # self.Gun.rotation = self.rotation + self.Gun.gun_rotation


    def heavy_fire(self):
        self.Gun.fireFirstWeapon()

    def fire(self):
        self.Gun.fireSecondWeapon()