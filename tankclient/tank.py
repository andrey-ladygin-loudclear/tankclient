import PodSixNet, time
from PodSixNet.Connection import connection
from time import sleep

# tell the client which server to connect to
#from TankNetworkListener import TankNetworkListener

import cocos
from cocos import director
import cocos.collision_model as cm
from cocos import scene
from cocos import sprite
from cocos.actions import Delay
from cocos.actions import MoveBy, Repeat
from cocos.batch import BatchNode
from pyglet.window import key

import settings
from bullets.Bullet import Bullet
from walls.brickWall import BrickWall

from bullets.standartBullet import StandartBullet


class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(0, 0, 0, 255)
        self.schedule(self.update)

    def update(self, dt):
        #self.player.cshape.center = self.player.position
        #MUST BE TANK

        #print(dt)

        connection.Pump()
        if settings.TankNetworkListenerConnection:
            settings.TankNetworkListenerConnection.Pump()

        # for bullet in settings.objects['bullets']:
        #     bullet.cshape.center = bullet.position
        #     collisions = settings.collision_manager.objs_colliding(bullet)
        #
        #     if collisions:
        #         for wall in settings.objects['walls']:
        #             if wall in collisions:
        #                 explosion = bullet.explosion()
        #                 explosion.checkDamageCollisions()
        #                 #cocos.director.director.pop()
        #                 break
        #
        # for wall in settings.objects['walls']:
        #     if wall.health <= 0:
        #         if wall in settings.layers['walls']: settings.layers['walls'].remove(wall)
        #         if wall in settings.objects['walls']: settings.objects['walls'].remove(wall)

def main():
    # Initialize the window.
    settings.init()

    director.director.init(width=settings.dimensions['x'], height=settings.dimensions['y'], do_not_scale=True, resizable=True)
    settings.collision_manager = cm.CollisionManagerBruteForce()

    # Create a layer and add a sprite to it.
    settings.layers['game'] = Game()
    settings.layers['bullets'] = BatchNode()
    settings.layers['walls'] = BatchNode()
    settings.layers['enemies'] = BatchNode()

    # Tank1 = ETank()
    # Tank1.do(UserTankMovingHandlers())
    #
    # settings.collision_manager.add(Tank1)
    #
    # settings.layers['game'].add(Tank1)
    # settings.layers['game'].add(Tank1.getGunSprite())
    # settings.objects['players'].append(Tank1)

    settings.layers['game'].add(settings.layers['bullets'], z=15)
    settings.layers['game'].add(settings.layers['walls'])
    settings.layers['game'].add(settings.layers['enemies'])


    # enemy = KVTank()
    # enemy.position = (800, 800)
    # enemy.do(EnemyTankMovingHandlers())
    # settings.collision_manager.add(enemy)
    # settings.objects['enemies'].append(enemy)
    # settings.layers['enemies'].add(enemy)
    # settings.layers['enemies'].add(enemy.getGunSprite())

    # for i in range(20):
    #     wall = BrickWall()
    #     wall.update_position(i*32, 500)
    #     settings.collision_manager.add(wall)
    #     settings.objects['walls'].append(wall)
    #     settings.layers['walls'].add(wall)
    #
    # for i in range(30):
    #     wall = BrickWall()
    #     wall.update_position(i*32 + 680, 500)
    #     settings.collision_manager.add(wall)
    #     settings.objects['walls'].append(wall)
    #     settings.layers['walls'].add(wall)


    for i in range(100):
        for j in range(50):
            wall = sprite.Sprite('sprites/walls/adesert_cracks_5x5.jpg')
            wall.position = (i*5 + 200, 800 + j*5)
            wall.scale = 1
            wall.cshape = cm.AARectShape(
                wall.position,
                wall.width // 2,
                wall.height // 2
            )
            #settings.collision_manager.add(wall)
            #settings.objects['walls'].append(wall)
            #settings.layers['walls'].add(wall)

    #animation = pyglet.image.load_animation('sprites/effects/nuke-ani.gif')
    #anim = sprite.Sprite(animation)
    #anim.position = (500, 500)
    #settings.layers['game'].add(anim)

    # Create a scene and set its initial layer.
    main_scene = scene.Scene(settings.layers['game'])

    # Attach a KeyStateHandler to the keyboard object.
    settings.keyboard = key.KeyStateHandler()
    director.director.window.push_handlers(settings.keyboard)

    # Play the scene in the window.
    director.director.run(main_scene)

    #settings.TankNetworkListener = TankNetworkListener('localhost', 1337)
   # while 1:
    #    connection.Pump()
    #    settings.TankServer.Pump()
    #gui.Send({'action' : 'send data 2'})

if __name__ == '__main__':
    main()

