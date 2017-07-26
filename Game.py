from cocos import director
import cocos.collision_model as cm
from cocos import layer
from cocos import scene
from pyglet.window import key

from events.NetworkListener import NetworkListener
from factories.TankFactory import TankFactory
from helpers import Global
from helpers.Layers import Layers
from helpers.Objects import Objects


def main():
    # Initialize the window.

    director.director.init(width=3000, height=960, do_not_scale=True, resizable=True)
    #director.director.init(do_not_scale=True, resizable=True, fullscreen=True)

    initGlobalParams()

    # Create a scene and set its initial layer.
    main_scene = scene.Scene(Global.GameLayers.game)
    main_scene.schedule(Global.GameLayers.game.buttonsHandler)

    director.director.on_resize = Global.GameLayers.game.resize
    # Play the scene in the window.
    director.director.run(main_scene)

def initGlobalParams():
    Global.CollisionManager = cm.CollisionManagerBruteForce()
    Global.GameLayers = Layers()
    Global.GameObjects = Objects()

    # Attach a KeyStateHandler to the keyboard object.
    Global.CurrentKeyboard = key.KeyStateHandler()
    director.director.window.push_handlers(Global.CurrentKeyboard)
    #scrollerHandler = layer.ScrollingManager()
    #Global.TankNetworkListenerConnection = NetworkListener('localhost', 1332)

    Global.GameLayers.init()



if __name__ == '__main__':
    main()
#https://books.google.com.ua/books?id=99lOCwAAQBAJ&pg=PA33&lpg=PA33&dq=collision+manager+rotate+object+python&source=bl&ots=Us6jMMADR2&sig=V8Q50LUWTPfLh6fbWQ1rZBi2u98&hl=ru&sa=X&ved=0ahUKEwiG2rKv2IzQAhWLhywKHarDB7oQ6AEIOzAE#v=onepage&q=collision%20manager%20rotate%20object%20python&f=false
