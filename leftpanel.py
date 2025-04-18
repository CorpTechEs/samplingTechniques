import pygame
from sysui import SysUI

class LeftPanel:
    def __init__(self):
        self.sysui = SysUI()

    def draw(self):
        self.left_rect = pygame.Rect(self.sysui.panel_padding, self.sysui.panel_top, self.sysui.panel_width, self.sysui.panel_height)
        pygame.draw.rect(self.sysui.ui.screen, (190, 190, 190), self.left_rect, 3)
        self.pop_label = self.sysui.ui.font.render("Population", True, (0, 0, 0))
        self.sysui.ui.screen.blit(self.pop_label, self.pop_label.get_rect(center=(self.left_rect.centerx, self.left_rect.top - 20)))
        # pygame.display.update()
