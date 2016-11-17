from PodSixNet.Connection import ConnectionListener, connection

import Global
from events.Events import Events


class NetworkBulletsListener(ConnectionListener):
    events = Events()

    def __init__(self, host, port):
        self.Connect((host, port))
        print(port)

    def Network(self, data):
        print(data)

        if(data.get('action') == Global.NetworkActions.UPDATE):
            self.events.update(data.get('objects'))

        if(data.get('action') == Global.NetworkActions.DESTROY):
            self.events.destroy(data.get('type'), data.get('id'))

    def Network_connected(self, data):
        print "connected to the server"

    def Network_error(self, data):
        print "error:", data['error'][1]

    def Network_disconnected(self, data):
        print "disconnected from the server"
