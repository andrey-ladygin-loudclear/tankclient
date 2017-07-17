from objects.Tank import Tank


class KVTank(Tank):
    spriteName = 'assets/tank/parts/KV-2_1.png'
    spriteGunName = 'assets/tank/parts/KV-2_2.png'

    bulletFreezTime = 0.1
    heavyBulletFreezTime = 3

    speed_acceleration = 4
    max_speed = 70
    rotation_speed = 1.2
    gun_rotation_speed = 1.2

    #damage = 10
    #damageRadius = 20
    #fireLength = 1000
    #bulletSpeed = 800

    def __init__(self):
        super(KVTank, self).__init__(self.spriteName)