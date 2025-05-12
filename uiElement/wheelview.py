import pygame
import math
from ui import UI

class WheelView(UI):
    def __init__(self, radius=130):
        super().__init__()
        self.radius = radius
        self.pointer_rect = pygame.Rect((395, 420), (10, 20))
        self.circle_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.circle_surface.fill((255,255,255))
        pygame.draw.circle(self.circle_surface, (0, 0, 0), (self.radius, self.radius), self.radius)

    def draw_spokes(self, num_spokes, center):
        for i in range(num_spokes):
            angle = (2 * math.pi / num_spokes) * i
            end_x = center[0] + self.radius * math.cos(angle)
            end_y = center[1] + self.radius * math.sin(angle)
            pygame.draw.line(self.circle_surface, (255, 0, 255), center, (end_x, end_y), 2)

    def get_elements(self, angular_velocity, last_spoke_hit):
        elements = []
        if last_spoke_hit and angular_velocity == 0:
            label, pos = self.create_text_label(f"Last Hit: {last_spoke_hit.data}", (10, 10))
            elements.append((label, pos))
        return elements

    def draw_pointer(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.pointer_rect, 2)
