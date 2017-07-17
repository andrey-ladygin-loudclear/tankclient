import math
import random

from objects.Gun import Gun


class LightWeapon(Gun):

    standart_fire_offset_x = -20
    standart_fire_offset_y = 5
    standart_fire_animation_offset_x = -5
    standart_fire_animation_offset_y = 0

    def getStandartGunAngleDeflection(self):
        return random.randrange(-500, 500) / 100

    def standartFirePosition(self):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + self.standart_fire_offset_x * sin_x + self.standart_fire_offset_y * cos_x
        y = self.y - self.standart_fire_offset_x * cos_x + self.standart_fire_offset_y * sin_x
        return (x, y)

    def standartFireAnimationPosition(self):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + self.standart_fire_offset_x * sin_x + self.standart_fire_offset_y * cos_x
        y = self.y - self.standart_fire_offset_x * cos_x + self.standart_fire_offset_y * sin_x
        anim_x = x + self.standart_fire_animation_offset_x * sin_x + self.standart_fire_animation_offset_y * cos_x
        anim_y = y - self.standart_fire_animation_offset_x * cos_x + self.standart_fire_animation_offset_y * sin_x
        return (anim_x, anim_y)