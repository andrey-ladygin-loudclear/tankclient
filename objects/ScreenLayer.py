import cocos

import Global


class ScreenLayer:
    label = None

    def init(self):
        self.label = cocos.text.Label(
            '100',
            font_name='Times New Roman',
            font_size=16,
            anchor_x='left',  anchor_y='top'
        )
        self.label.position = 0, Global.dimensions['y']
        Global.layers['panel'].add(self.label)

    def setHealth(self, health):
        self.label.element.text = str(int(round(health)))
