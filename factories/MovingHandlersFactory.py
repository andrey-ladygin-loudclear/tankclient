from movingHandlers.EnemyTankMovingHandlers import EnemyTankMovingHandlers
from movingHandlers.UserTankMovingHandlers import UserTankMovingHandlers


class MovingHandlersFactory:

    @staticmethod
    def getInstance(fraction):
        if fraction == 'player':
            return UserTankMovingHandlers

        if fraction == 'enemy':
            return EnemyTankMovingHandlers