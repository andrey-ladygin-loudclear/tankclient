from factories.TankFactory import TankFactory
from helpers import Global
from objects.Wall import Wall


class Events():

    def update(self, object):
        id = object.get(Global.NetworkDataCodes.ID)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)
        gun_rotation = object.get(Global.NetworkDataCodes.GUN_ROTATION)

        tank = TankFactory.getOrCreate(id)

        if id == Global.CurrentPlayerId: return

        tank.rotation = rotation
        tank.gun_rotation = gun_rotation
        tank.position = position

    def fire(self, object):
        id = object.get(Global.NetworkDataCodes.ID)
        parent_id = object.get(Global.NetworkDataCodes.PARENT_ID)
        position = object.get(Global.NetworkDataCodes.POSITION)
        rotation = object.get(Global.NetworkDataCodes.ROTATION)

        last_update_time = object.get(Global.NetworkDataCodes.LAST_UPDATE_TIME)
        last_update_time = float(last_update_time)

        tank = Global.GameObjects.getTank(parent_id)

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET:
            tank.Gun.weapon2.fire(id, position, rotation, last_update_time)

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:
            tank.Gun.weapon1.fire(id, position, rotation, last_update_time)

    def damage(self, object):
        id = object.get(Global.NetworkDataCodes.ID)
        dmg = object.get(Global.NetworkDataCodes.DAMAGE)

        tank = Global.GameObjects.getTank(id)
        Global.GameLayers.stats.damage(dmg, tank.position)

        if id == Global.CurrentPlayerId:
            health = object.get(Global.NetworkDataCodes.HEALTH)
            Global.GameLayers.stats.setHealth(health)

    def destroy(self, object):
        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.WALL:
            id = object.get(Global.NetworkDataCodes.ID)
            wall = Global.GameObjects.getWall(id)
            wall.destroy()

        if object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.STANDART_BULLET or \
                        object.get(Global.NetworkDataCodes.TYPE) == Global.NetworkDataCodes.HEAVY_BULLET:

            id = object.get(Global.NetworkDataCodes.ID)
            position = object.get(Global.NetworkDataCodes.POSITION)
            bullet = Global.GameObjects.getBullet(id)
            if not bullet: return

            print 'destroy'
            bullet.destroy(position)

    def set_walls(self, walls):
        for wall in walls:
            src = wall.get(Global.NetworkDataCodes.SRC).replace('assets/', 'assets/map/')
            brick_wall = Wall(src)

            type = wall.get(Global.NetworkDataCodes.TYPE)

            brick_wall.id = wall.get(Global.NetworkDataCodes.ID)

            x, y = wall.get(Global.NetworkDataCodes.POSITION)

            brick_wall.position = (x, y)
            brick_wall.type = type
            brick_wall.src = src

            Global.GameLayers.addWall(brick_wall, brick_wall.type)

            if brick_wall.type != 0 and brick_wall.type != 1:
                Global.GameObjects.addWall(brick_wall)