from PodSixNet.Connection import ConnectionListener, connection

import Global
from events.Events import Events


class NetworkListener(ConnectionListener):
    events = Events()

    def __init__(self, host, port):
        self.Connect((host, port))

    def Network(self, data):
        #print(data)

        if(data.get('action') == Global.Actions.INIT):
            self.events.set_walls(data.get('walls'))

        if(data.get('action') == Global.Actions.UPDATE):
            self.events.update(data.get('objects'))
