import PodSixNet, time
from PodSixNet.Connection import connection
from time import sleep

# tell the client which server to connect to
#from TankNetworkListener import TankNetworkListener

import cocos
from cocos import director
import cocos.collision_model as cm
from cocos import scene
from cocos import sprite
from cocos.batch import BatchNode
from pyglet.window import key

import Global

class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(0, 0, 0, 255)
        self.schedule(self.update)

    def update(self, dt):
        connection.Pump()

        if Global.TankNetworkListenerConnection:
            Global.TankNetworkListenerConnection.Pump()

def main():
    # Initialize the window.
    Global.init()

    director.director.init(width=Global.dimensions['x'], height=Global.dimensions['y'], do_not_scale=True, resizable=True)
    Global.collision_manager = cm.CollisionManagerBruteForce()

    # Create a layer and add a sprite to it.
    Global.layers['game'] = Game()
    Global.layers['bullets'] = BatchNode()
    Global.layers['walls'] = BatchNode()
    Global.layers['enemies'] = BatchNode()
    Global.layers['test'] = BatchNode()

    Global.layers['game'].add(Global.layers['bullets'])
    Global.layers['game'].add(Global.layers['walls'])
    Global.layers['game'].add(Global.layers['enemies'])
    Global.layers['game'].add(Global.layers['test'])

    # Create a scene and set its initial layer.
    main_scene = scene.Scene(Global.layers['game'])

    # Attach a KeyStateHandler to the keyboard object.
    Global.keyboard = key.KeyStateHandler()
    director.director.window.push_handlers(Global.keyboard)

    # Play the scene in the window.
    director.director.run(main_scene)

if __name__ == '__main__':
    main()
#https://books.google.com.ua/books?id=99lOCwAAQBAJ&pg=PA33&lpg=PA33&dq=collision+manager+rotate+object+python&source=bl&ots=Us6jMMADR2&sig=V8Q50LUWTPfLh6fbWQ1rZBi2u98&hl=ru&sa=X&ved=0ahUKEwiG2rKv2IzQAhWLhywKHarDB7oQ6AEIOzAE#v=onepage&q=collision%20manager%20rotate%20object%20python&f=false
