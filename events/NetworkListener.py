from PodSixNet.Connection import ConnectionListener, connection

import Global
from events.Events import Events


class NetworkListener(ConnectionListener):
    events = Events()

    def __init__(self, host, port):
        self.Connect((host, port))

    def Network(self, data):
        #print('NetworkBulletsListener')

        if(data.get('action') == Global.NetworkActions.INIT):
            self.events.set_walls(data.get('walls'))

        if(data.get('action') == Global.NetworkActions.UPDATE):
            self.events.update(data.get('o'))

            events = data.get('events')

            if events:
                for event in events:
                    if(event.get('action') == Global.NetworkActions.DESTROY):
                        pass#self.events.destroy(event.get('type'), event.get('id'))

        if(data.get('action') == Global.NetworkActions.DESTROY):
            self.events.destroy(data.get('type'), data.get('id'))

    #https://www.youtube.com/watch?v=AdG_ITCFHDI EXPLODIONS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

    def Network_connected(self, data):
        print "connected to the server"

    def Network_error(self, data):
        print "error:", data['error'][1]

    def Network_disconnected(self, data):
        print "disconnected from the server"
