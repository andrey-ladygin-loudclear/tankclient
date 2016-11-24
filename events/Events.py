from cocos.actions import MoveBy, Delay, Repeat
from factories.TankFactory import TankFactory
from factories.MovingHandlersFactory import MovingHandlersFactory
from factories.LayoutFactory import LayoutFactory
from factories.ObjectFactory import ObjectFactory
import Global

from factories.BulletFactory import BulletFactory
from objects.GameObject import GameObject
from objects.walls.brickWall import BrickWall


class Events():
    gameObject = GameObject()

    def tanks(self):
        if self.arguments.get('tanks'):
            for tank in self.arguments.get('tanks'):
                fraction = tank.get('fraction')
                type = tank.get('type')

                movingHandler = MovingHandlersFactory.getInstance(fraction)

                Tank = TankFactory.getInstance(type)
                Tank.do(movingHandler())

                Tank.position = (tank.get('x'), tank.get('y'))

                #Global.collision_manager.add(Tank1)

                LayoutFactory.addTank(Tank, fraction)
                ObjectFactory.addTank(Tank, fraction)

    def update(self, objects):
        for object in objects:
            self.gameObject.update(object)

        #     if object.get('type') == 'tank':
        #         self.updateTank(object)
        #     if object.get('type') == 'bullet':
        #         self.updateBullet(object)

    def updateTank(self, tank):
        fraction = tank.get('fraction')

        if not ObjectFactory.updateTank(tank):
            movingHandler = MovingHandlersFactory.getInstance(fraction)

            newTank = TankFactory.getInstance(tank)
            newTank.do(movingHandler())

            LayoutFactory.addTank(newTank, fraction)
            ObjectFactory.addTank(newTank, fraction)

    def updateBullet(self, bullet):
        if not ObjectFactory.updateBullet(bullet):
            newBullet = BulletFactory.getInstance(bullet)
            newBullet.rotation = bullet.get('rotation')
            newBullet.do(MoveBy(bullet.get('moveTo'), 1))

            LayoutFactory.addBullet(newBullet)
            ObjectFactory.addBullet(newBullet)

    def destroy(self, data):
        if type == 'wall':
            for wall in Global.objects['walls']:
                if wall.id == id:
                    Global.objects['walls'].remove(wall)
                    Global.layers['walls'].remove(wall)

        if type == 'bullet':
            for bullet in Global.objects['bullets']:
                if bullet.id == id:
                    Global.objects['bullets'].remove(bullet)
                    Global.layers['bullets'].remove(bullet)

    def set_walls(self, walls):
        for wall in walls:
            brick_wall = BrickWall()
            brick_wall.id = wall.get('id')
            brick_wall.update_position(wall.get('position'))

            Global.objects['walls'].append(brick_wall)
            Global.layers['walls'].add(brick_wall)
            Global.collision_manager.add(brick_wall)