import pygame
from sysui import PanelUI

class Notification(PanelUI):
    def __init__(self):
        super().__init__()

    def draw_notification_bar(self, message, font):
        pygame.draw.rect(self.screen, (0, 255, 255), (0, 0, self.screen.get_width(), 40))  # Light blue bar
        text_surface = font.render(message, True, (0, 0, 0))
        self.screen.blit(text_surface, (10, 10))
