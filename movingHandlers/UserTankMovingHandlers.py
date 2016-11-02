from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from pyglet.window import key


class UserTankMovingHandlers(DefaultTankMovingHandlers):

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
        super(UserTankMovingHandlers, self).step(dt) # Run step function on the parent class.
