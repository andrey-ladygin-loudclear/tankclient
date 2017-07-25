import cocos

from helpers import Global


class HealthHelper():
    healthLayer = None
    target = None

    def __init__(self, target):
        self.target = target
        self.healthLayer = cocos.sprite.Sprite('assets/50x5.png')
        self.updateHealthPosition()
        Global.GameLayers.globalPanel.add(self.healthLayer)

    def updateHealthPosition(self):
        x, y = self.target.position
        self.healthLayer.position = (x - 5, y + 40)

    def setHealth(self, health):
        percent = max(health, 0) / 100.
        self.healthLayer.scale_x = percent

    def destroy(self):
        Global.GameLayers.globalPanel.remove(self.healthLayer)