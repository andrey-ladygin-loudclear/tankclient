import random

import math


class LightWeapon:
    standart_fire_offset_x = -20
    standart_fire_offset_y = 5
    standart_fire_animation_offset_x = -5
    standart_fire_animation_offset_y = 0

    gun = None

    def __init__(self, gun):
        self.gun = gun

    def getAngleDeflection(self):
        return random.randrange(-500, 500) / 100

    def firePosition(self):
        cos_x = math.cos(math.radians(self.gun.rotation - 180))
        sin_x = math.sin(math.radians(self.gun.rotation))
        x = self.gun.x + self.standart_fire_offset_x * sin_x + self.standart_fire_offset_y * cos_x
        y = self.gun.y - self.standart_fire_offset_x * cos_x + self.standart_fire_offset_y * sin_x
        return (x, y)

    def fireAnimationPosition(self):
        cos_x = math.cos(math.radians(self.gun.rotation - 180))
        sin_x = math.sin(math.radians(self.gun.rotation))
        x = self.gun.x + self.standart_fire_offset_x * sin_x + self.standart_fire_offset_y * cos_x
        y = self.gun.y - self.standart_fire_offset_x * cos_x + self.standart_fire_offset_y * sin_x
        anim_x = x + self.standart_fire_animation_offset_x * sin_x + self.standart_fire_animation_offset_y * cos_x
        anim_y = y - self.standart_fire_animation_offset_x * cos_x + self.standart_fire_animation_offset_y * sin_x
        return (anim_x, anim_y)
