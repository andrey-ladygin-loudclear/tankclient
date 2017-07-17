import Global

class LayoutFactory:

    @staticmethod
    def addTank(tank, fraction):
        Global.GameLayers.addTank(tank)

    @staticmethod
    def addBullet(bullet):
        Global.layers['bullets'].add(bullet)


    @staticmethod
    def updateTank(tank):
        if tank.get('fraction') == 'player':
            for player in Global.layers['game']:
                if player['id'] == tank.get('id'):
                    player.position = tank.get('position')
                    return True

        if tank.get('fraction') == 'enemy':
            for enemy in Global.layers['enemies']:
                if enemy['id'] == tank.get('id'):
                    enemy.position = tank.get('position')
                    return True

        return False