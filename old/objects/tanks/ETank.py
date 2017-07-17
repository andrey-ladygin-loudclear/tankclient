from objects.Tank import Tank


class ETank(Tank):
    spriteName = 'assets/tank/parts/E-100_1.png'
    spriteGunName = 'assets/tank/parts/E-100_2.png'

    bulletFreezTime = 0.1
    heavyBulletFreezTime = 3

    speed_acceleration = 4
    max_speed = 70
    rotation_speed = 1.2
    gun_rotation_speed = 1.2

    def __init__(self):
        super(ETank, self).__init__(self.spriteName)