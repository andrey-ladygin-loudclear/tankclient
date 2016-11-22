import random

import math
from time import time

from cocos import actions

import Global

class BulletMovingHandlers(actions.Move):
    def __init__(self):
        super(BulletMovingHandlers, self).__init__()

    def step(self, dt):
        super(BulletMovingHandlers, self).step(dt)  # Run step function on the parent class.
        angle = self.target.rotation
        curr_x, curr_y = self.target.position
        time_delta = (time() - self.target.last_update_time)
        new_x = self.target.speed * time_delta * math.cos(math.radians(angle - 180 + self.target.angle_of_deflection)) + curr_x
        new_y = self.target.speed * time_delta * math.sin(math.radians(angle + self.target.angle_of_deflection)) + curr_y
        self.target._set_position((new_x, new_y))