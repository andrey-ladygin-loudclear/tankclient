from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from pyglet.window import key


class TESTUserTankMovingHandlers(DefaultTankMovingHandlers):

    RIGHT = key.J
    LEFT = key.L
    UP = key.I
    DOWN = key.K
    GUN_LEFT = key.U
    GUN_RIGHT = key.O
    FIRE_HEAVY_GUN = key.B
    FIRE_LIGHT_GUN = key.N

    # step() is called every frame.
    # dt is the number of seconds elapsed since the last call.
    def step(self, dt):
        super(TESTUserTankMovingHandlers, self).step(dt) # Run step function on the parent class.
