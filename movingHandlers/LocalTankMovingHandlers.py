import math

import operator
import cocos.collision_model as cm

from helpers import Global
from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from pyglet.window import key


class LocalTankMovingHandlers(DefaultTankMovingHandlers):

    RIGHT = key.RIGHT
    LEFT = key.LEFT
    UP = key.UP
    DOWN = key.DOWN
    GUN_LEFT = key.Q
    GUN_RIGHT = key.E
    FIRE_HEAVY_GUN = key.SPACE
    FIRE_LIGHT_GUN = key.W

    # step() is called every frame.
    # dt is the number of seconds elapsed since the last call.
    def step(self, dt):

        # UserTankMovingHandlers
        # super(DefaultTankMovingHandlers, self).step(dt) # Run step function on the parent class.
        super(DefaultTankMovingHandlers, self).step(dt) # Run step function on the parent class.

        turns_direction = Global.CurrentKeyboard[self.RIGHT] - Global.CurrentKeyboard[self.LEFT]
        moving_directions = Global.CurrentKeyboard[self.UP] - Global.CurrentKeyboard[self.DOWN]
        gun_turns_direction = Global.CurrentKeyboard[self.GUN_RIGHT] - Global.CurrentKeyboard[self.GUN_LEFT]

        self.target.rotation += turns_direction * 1.01
        self.target.gun_rotation += gun_turns_direction * 1.01

        self.target.velocity = (0,0)
        if moving_directions:
            speed = moving_directions * 20
            tank_rotation = self.target.rotation
            cos_x = math.cos(math.radians(tank_rotation + 180))
            sin_x = math.sin(math.radians(tank_rotation + 180))
            velocity = (speed * sin_x, speed * cos_x)
            self.target.velocity = velocity

        if Global.CurrentKeyboard[self.FIRE_LIGHT_GUN]:
            self.target.fire()

        if Global.CurrentKeyboard[self.FIRE_HEAVY_GUN]:
            self.target.heavy_fire()

        return
        self.addSpeed(moving_directions)

        # Set the object's velocity.
        self.setTankRotation(turns_direction, moving_directions)
        new_velocity = self.getVelocity()

        new_position = tuple(map(operator.add, self.target.position, new_velocity))

        if self.checkCollisionsWithObjects():
            self.target.velocity = (0, 0)
            self.target.position = self.target.old_position
        else:
            self.target.old_position = self.target.position

            if(self.target.position != new_position):
                Global.TankNetworkListenerConnection.Send({
                    'action': Global.NetworkActions.TANK_MOVE,
                    'pos': self.target.position,
                    'id': self.target.id
                })

            new_velocity = self.getVelocityByNewPosition(self.target.position, new_position)
            self.setNewVelocity(new_velocity)


        # SHOULD REDUCE SPEED IF NEXT POSITION IS WALL
        #self.setNewVelocity(new_velocity)
        self.setGunPosition()

        # Set the object's rotation
        self.setGunRotation(gun_turns_direction)
