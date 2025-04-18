import pygame
from sysui import PanelUI

class RightPanel(PanelUI):
    def __init__(self):
        super().__init__()

    def draw(self):
        self.right_rect = pygame.Rect(self.width - self.panel_padding - self.panel_width, self.panel_top, self.panel_width, self.panel_height)
        pygame.draw.rect(self.screen, (190, 190, 190), self.right_rect, 3)
        self.sample_label = self.font.render("Sample", True, (0, 0, 0))
        self.screen.blit(self.sample_label, self.sample_label.get_rect(center=(self.right_rect.centerx, self.right_rect.top - 20)))
        self.draw_btn()

    def draw_btn(self):
        # === GO AGAINST BUTTON (inside sample panel at bottom center) ===
        go_btn_width, go_btn_height = 100, 30
        go_btn_x = self.right_rect.centerx - go_btn_width // 2
        go_btn_y = self.right_rect.bottom - go_btn_height - 10
        pygame.draw.rect(self.screen, (0, 128, 255), (go_btn_x, go_btn_y, go_btn_width, go_btn_height))
        go_label = self.font.render("Go Against", True, (255, 255, 255))
        self.screen.blit(go_label, go_label.get_rect(center=(go_btn_x + go_btn_width // 2, go_btn_y + go_btn_height // 2)))



            # def draw_samples(self, screen, user_sample, system_sample):
            #     # Draw user sample (red)
            #     for i, _ in enumerate(user_sample):
            #         rect = pygame.Rect(self.user_x, self.y + i * (self.box_size + self.gap), self.box_size, self.box_size)
            #         pygame.draw.rect(screen, (255, 102, 102), rect)

            #     # Draw system sample (blue)
            #     for i, _ in enumerate(system_sample):
            #         rect = pygame.Rect(self.system_x, self.y + i * (self.box_size + self.gap), self.box_size, self.box_size)
            #         pygame.draw.rect(screen, (102, 178, 255), rect)

            # def draw_result(self, screen, result_text):
            #     text_surface = self.font.render(result_text, True, (0, 0, 0))
            #     screen.blit(text_surface, (400, 400))
