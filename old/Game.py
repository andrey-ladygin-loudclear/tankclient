from math import atan

import PodSixNet, time
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
from Global import Config, Layers, CurrentScreen, TankNetworkListenerConnection


class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(0, 0, 0, 255)
        self.schedule(self.update)

    def update(self, dt):
        PodSixNet.Connection.connection.Pump()

        if TankNetworkListenerConnection:
            TankNetworkListenerConnection.Pump()

def main():
    # Initialize the window.

    director.director.init(width=Config.dimensions['x'], height=Config.dimensions['y'], do_not_scale=True, resizable=True)
    #director.director.init(do_not_scale=True, resizable=True, fullscreen=True)
    Global.CollisionManager = cm.CollisionManagerBruteForce()

    #// SCROLLER  http://jpwright.net/writing/python-cocos2d-game-2/


    # Create a layer and add a sprite to it.
    Layers.game = Game()
    Layers.bullets = BatchNode()
    Layers.walls = BatchNode()
    Layers.backgrounds = BatchNode()
    Layers.tanks = BatchNode()

    Layers.game.add(Layers.backgrounds, z=0)
    Layers.game.add(Layers.bullets, z=1)
    Layers.game.add(Layers.walls)
    Layers.game.add(Layers.tanks)

    Layers.globalPanel = cocos.layer.Layer()
    Layers.game.add(Layers.globalPanel, z=1)

    CurrentScreen.init()

    # Create a scene and set its initial layer.
    main_scene = scene.Scene(Layers.game)

    # Attach a KeyStateHandler to the keyboard object.
    Global.CurrentKeyboard = key.KeyStateHandler()
    director.director.window.push_handlers(Global.CurrentKeyboard)

    # Play the scene in the window.
    director.director.run(main_scene)

if __name__ == '__main__':
    main()
#https://books.google.com.ua/books?id=99lOCwAAQBAJ&pg=PA33&lpg=PA33&dq=collision+manager+rotate+object+python&source=bl&ots=Us6jMMADR2&sig=V8Q50LUWTPfLh6fbWQ1rZBi2u98&hl=ru&sa=X&ved=0ahUKEwiG2rKv2IzQAhWLhywKHarDB7oQ6AEIOzAE#v=onepage&q=collision%20manager%20rotate%20object%20python&f=false
