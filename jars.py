import pygame
from sysui import PanelUI

class CollectionJar (PanelUI):
    def __init__(self, jars = 4):
        super().__init__()
        self.u_box_size = 60
        self.jars = jars
        self.u_gap = 40
        self.total_u_width = 4 * self.u_box_size + 3 * self.u_gap
        self.u_area_start_x = (self.width // 2) - (self.total_u_width // 2)
        self.u_y_top = self.panel_top + self.panel_height - self.u_box_size  # Align with bottom of panels

        self.jarA = self.load_image("./uiElement/JARa.png")
        self.jarB = self.load_image("./uiElement/JARb.png")
        self.jarC = self.load_image("./uiElement/JARc.png")
        self.jarD = self.load_image("./uiElement/JARd.png")

    def draw(self):
        self.screen.blit(self.jarA, (800, 575))  # draw jar
        self.screen.blit(self.jarB, (800, 395))  # draw jar
        self.screen.blit(self.jarC, (800, 200))  # draw jar
        self.screen.blit(self.jarD, (800, 0))    # draw jar