from time import time

from PodSixNet.Connection import ConnectionListener, connection

import Global
from events.Events import Events


class NetworkListener(ConnectionListener):
    events = Events()

    def __init__(self, host, port):
        self.Connect((host, port))

    def Network(self, data):
        if data.get('action') == Global.NetworkActions.INIT:
            self.events.set_walls(data.get('walls'))
            Global.currentPlayerId = data.get('id')

        if data.get('action') == Global.NetworkActions.UPDATE:
            self.events.gameObject.update(data)

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
