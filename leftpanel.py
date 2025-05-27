import pygame
from sysui import PanelUI

class LeftPanel(PanelUI):
    def __init__(self):
        super().__init__()
        self.pop_panel = self.load_image("./uiElement/pop_panel.png")
        self.btn_populate = self.load_image("./uiElement/populate_btn.png")
        self.btn_populate_2 = self.load_image("./uiElement/populate_btn (2).png")


    def draw(self):
        # panels population and sample
        self.screen.blit(self.pop_panel, (0, 200))
        self.draw_btn(self.btn_populate, (100, 670))