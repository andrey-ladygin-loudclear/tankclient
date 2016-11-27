import math
from cocos import sprite


class Gun(sprite.Sprite):

    heavy_fire_offset_x = -20
    heavy_fire_offset_y = 0
    heavy_fire_animation_offset_x = -35
    heavy_fire_animation_offset_y = 0

    standart_fire_offset_x = -20
    standart_fire_offset_y = 5
    standart_fire_animation_offset_x = -5
    standart_fire_animation_offset_y = 0

    def __init__(self, spriteName):
        super(Gun, self).__init__(spriteName)

    def heavyFirePosition(self):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + self.heavy_fire_offset_x * sin_x + self.heavy_fire_offset_y * cos_x
        y = self.y - self.heavy_fire_offset_x * cos_x + self.heavy_fire_offset_y * sin_x
        return (x, y)

    def standartFirePosition(self):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + self.standart_fire_offset_x * sin_x + self.standart_fire_offset_y * cos_x
        y = self.y - self.standart_fire_offset_x * cos_x + self.standart_fire_offset_y * sin_x
        return (x, y)

    def heavyFireAnimationPosition(self):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + self.heavy_fire_offset_x * sin_x + self.heavy_fire_offset_y * cos_x
        y = self.y - self.heavy_fire_offset_x * cos_x + self.heavy_fire_offset_y * sin_x
        anim_x = x + self.heavy_fire_animation_offset_x * sin_x + self.heavy_fire_animation_offset_y * cos_x
        anim_y = y - self.heavy_fire_animation_offset_x * cos_x + self.heavy_fire_animation_offset_y * sin_x
        return (anim_x, anim_y)

    def standartFireAnimationPosition(self):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + self.standart_fire_offset_x * sin_x + self.standart_fire_offset_y * cos_x
        y = self.y - self.standart_fire_offset_x * cos_x + self.standart_fire_offset_y * sin_x
        anim_x = x + self.standart_fire_animation_offset_x * sin_x + self.standart_fire_animation_offset_y * cos_x
        anim_y = y - self.standart_fire_animation_offset_x * cos_x + self.standart_fire_animation_offset_y * sin_x
        return (anim_x, anim_y)

    def getRotation(self):
        return self.rotation - 90