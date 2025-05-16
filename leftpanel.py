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

        self.left_rect = pygame.Rect(self.panel_padding, self.panel_top, self.panel_width, self.panel_height)
        pygame.draw.rect(self.screen, (190, 190, 190), self.left_rect, 3)
        self.pop_label = self.font.render("Population", True, (0, 0, 0))
        self.screen.blit(self.pop_label, self.pop_label.get_rect(center=(self.left_rect.centerx, self.left_rect.top - 20)))
