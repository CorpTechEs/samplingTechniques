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

        # === U-shaped Squares at Bottom, spread in center 50% ===
        for i in range(self.jars):
            x = self.u_area_start_x + i * (self.u_box_size + self.u_gap)
            # Draw U-shape (left, bottom, right)
            pygame.draw.line(self.screen, (0, 0, 0), (x, self.u_y_top), (x, self.u_y_top + self.u_box_size), 3)
            pygame.draw.line(self.screen, (0, 0, 0), (x, self.u_y_top + self.u_box_size), (x + self.u_box_size, self.u_y_top + self.u_box_size), 3)
            pygame.draw.line(self.screen, (0, 0, 0), (x + self.u_box_size, self.u_y_top), (x + self.u_box_size, self.u_y_top + self.u_box_size), 3)