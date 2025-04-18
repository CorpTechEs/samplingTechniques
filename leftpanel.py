import pygame
from sysui import PanelUI

class LeftPanel(PanelUI):
    def __init__(self):
        super().__init__()

    def draw(self):
        self.left_rect = pygame.Rect(self.panel_padding, self.panel_top, self.panel_width, self.panel_height)
        pygame.draw.rect(self.screen, (190, 190, 190), self.left_rect, 3)
        self.pop_label = self.font.render("Population", True, (0, 0, 0))
        self.screen.blit(self.pop_label, self.pop_label.get_rect(center=(self.left_rect.centerx, self.left_rect.top - 20)))
