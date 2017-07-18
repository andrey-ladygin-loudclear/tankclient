from time import time

from PodSixNet.Connection import ConnectionListener, connection

#from events.Events import Events
from events.Events import Events
from helpers import Global


class NetworkListener(ConnectionListener):
    events = Events()

    def __init__(self, host, port):
        self.Connect((host, port))

    def Network(self, update):
        print time(), update

        if update.get('action') == Global.NetworkActions.INIT:
            if update.get('walls'):
                self.events.set_walls(update.get('walls'))

            if update.get('id'):
                Global.CurrentPlayerId = update.get('id')

        for data in update.get('data', []):

            if data.get('action') == Global.NetworkActions.UPDATE:
                self.events.gameObject.update(data)

            if data.get('action') == Global.NetworkActions.UPDATE_BATCH:
                for player_data in data.get('objects'):
                    self.events.gameObject.update(player_data)

            if data.get('action') == Global.NetworkActions.TEST:
                self.events.gameObject.test(data)

            if data.get('action') == Global.NetworkActions.TANK_FIRE:
                self.events.gameObject.fire(data)

            if data.get('action') == Global.NetworkActions.DAMAGE:
                self.events.gameObject.damage(data)

            if data.get('action') == Global.NetworkActions.DESTROY:
                self.events.gameObject.destroy(data)

    #https://www.youtube.com/watch?v=AdG_ITCFHDI EXPLODIONS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

    def Network_connected(self, data):
        print "connected to the server"

    def Network_error(self, data):
        print(data['error'])

    def Network_disconnected(self, data):
        print "disconnected from the server"
