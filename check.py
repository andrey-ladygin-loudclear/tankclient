from cocos import sprite
from cocos.director import director
import cocos

from objects.tanks.ETank import ETank

world_width = 3000
world_height = 1000
class NetworkMap(cocos.layer.ScrollableLayer):
    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height
        super(NetworkMap, self).__init__()
        #bg = cocos.layer.ColorLayer(170,170,0,255,width=500,height=500)
        self.px_width = world_width
        self.px_height = world_height
        #self.add(bg,z=0)
        tank = ETank()
        self.add(tank)


class TestScene(cocos.scene.Scene):
    def __init__(self):
        super(TestScene,self).__init__()

    def on_enter(self):
        director.push_handlers(self.on_cocos_resize)
        super(TestScene, self).on_enter()

    def on_cocos_resize(self, usable_width, usable_height):
        self.f_refresh_marks()

    def f_refresh_marks(self):
        pass

def main():
    director.init(world_width, world_height, do_not_scale=True)
    scene = TestScene()
    world_map = NetworkMap(world_width, world_height)
    scroller = cocos.layer.ScrollingManager()
    scroller.add(world_map)
    scene.add(scroller)
    director.run(scene)

if __name__ == '__main__': main()


class Tank(sprite.Sprite):
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
        self.setGunSprite(self.spriteGunName)
        self.setDefaultState()
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )