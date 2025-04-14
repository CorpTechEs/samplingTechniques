import pygame
from sysui import SysUI

class TechniqueButton:
    def __init__(self):
        self.sys = SysUI()
        self.techniques = ["SRS", "SYS", "STRATIFIED", "CLUSTER"]
        self.is_hovered = False
        self.draw_btn()

    def draw_btn(self):
        for i, tech in enumerate(self.techniques):
            btn_x = 160 + i * 120
            btn_y = 80  # pushed down
            pygame.draw.rect(self.sys.ui.screen, (0, 128, 255), (btn_x, btn_y, 100, 30), 2)
            label = self.sys.ui.font.render(tech, True, (0, 0, 0))
            self.sys.ui.screen.blit(label, label.get_rect(center=(btn_x + 50, btn_y + 15)))

    def get_button_rects(self):
        return self.rects

    def highlight_selected(self, index):
        self.selected_index = index
        self.draw_btn()

    def reset_buttons(self):
        self.selected_index = None
        self.draw_btn()