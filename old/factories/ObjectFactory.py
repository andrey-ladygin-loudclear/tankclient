from cocos.actions import MoveBy
import Global

class ObjectFactory:

    @staticmethod
    def addTank(tank, fraction):

        if fraction == 'player':
            Global.objects['players'].append(tank)

        if fraction == 'enemy':
            Global.objects['enemies'].append(tank)

    @staticmethod
    def addBullet(bullet):
        Global.objects['bullets'].append(bullet)

    @staticmethod
    def getBullet(id):
        for bullet in Global.objects['bullets']:
            if bullet.id == id:
                return bullet

    @staticmethod
    def updateBullet(bullet):
        bulletObject = ObjectFactory.getBullet(bullet.get('id'))


        if bulletObject:
            bulletObject.rotation = bullet.get('rotation')
            bulletObject.do(MoveBy(bullet.get('moveTo'), 1))
            return True

        return False

    @staticmethod
    def updateTank(tank):
        NPC = ObjectFactory.getNPC(tank.get('id'))

        if NPC:
            NPC.new_position = tank.get('position')
            return True

        return False

    @staticmethod
    def getNPC(id):
        for player in Global.objects['players']:
            if player.id == id:
                return player

        for enemy in Global.objects['enemies']:
            if enemy.id == id:
                return enemy

        return None