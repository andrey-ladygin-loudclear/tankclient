import cocos
import cocos.collision_model as cm
from cocos import sprite
from cocos.layer import ColorLayer

from helpers import Global
from objects.Gun import Gun
from objects.animations.ExplosionTankAnimation import ExplosionTankAnimation
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation


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

    healthLayer = None

    def __init__(self, type):
        spriteName = 'assets/tank/parts/E-100_1.png'
        spriteGunName = 'assets/tank/parts/E-100_2.png'

        if type == 2:
            spriteName = 'assets/tank/parts/k1.png'
            spriteGunName = 'assets/tank/parts/K2.png'

        if type == 3:
            spriteName = 'assets/tank/parts/KV-2_1.png'
            spriteGunName = 'assets/tank/parts/KV-2_2.png'

        if type == 4:
            spriteName = 'assets/tank/parts/M-6_1.png'
            spriteGunName = 'assets/tank/parts/M-6_2.png'

        if type == 5:
            spriteName = 'assets/tank/parts/Pz.1.png'
            spriteGunName = 'assets/tank/parts/Pz.2.png'

        if type == 6:
            spriteName = 'assets/tank/parts/Pz.2-1.png'
            spriteGunName = 'assets/tank/parts/Pz.2-2.png'

        if type == 7:
            spriteName = 'assets/tank/parts/T34_1.png'
            spriteGunName = 'assets/tank/parts/T34_2.png'

        if type == 7:
            spriteName = 'assets/tank/parts/Tiger-II_1.png'
            spriteGunName = 'assets/tank/parts/Tiger-II_.png'

        self.Gun = Gun(spriteGunName, self)
        super(Tank, self).__init__(spriteName)

        self.initHealth()
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
        self.updateHealthPosition()

        # self.rotation = 180
        # self.Gun.position = self.position
        # self.Gun.rotation = self.rotation + self.Gun.gun_rotation

    def heavy_fire(self):
        self.Gun.fireFirstWeapon()

    def fire(self):
        self.Gun.fireSecondWeapon()

    def initHealth(self):
        self.healthLayer = cocos.sprite.Sprite('assets/50x5.png')
        self.updateHealthPosition()
        Global.GameLayers.globalPanel.add(self.healthLayer)

    def updateHealthPosition(self):
        x, y = self.position
        if self.healthLayer: self.healthLayer.position = (x - 5, y + 40)

    def setHealth(self, health):
        percent = max(health, 0) / 100.
        self.healthLayer.scale_x = percent

    def destroy(self):
        animation = ExplosionTankAnimation()
        animation.appendAnimationToLayer(self.position)
        if self in Global.GameObjects.getTanks(): Global.GameObjects.removeTank(self)
        Global.GameLayers.globalPanel.remove(self.healthLayer)
