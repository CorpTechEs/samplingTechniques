# import pygame
# import math
# # View/ UI

# class UI:
#     def __init__(self):
#         self.width = 800
#         self.height = 800
#         self.radius = 100
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         self.font = pygame.font.Font(None, 20)
#         self.pointer_rect = pygame.Rect((395, 290),(10, 20))
#         self.circle_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
#         pygame.draw.circle(self.circle_surface, (255, 0, 0), (self.radius, self.radius), self.radius)
        
        
        
#         # pygame.draw.line(self.circle_surface, (0, 0, 0), (0, 0), (self.radius * 2, self.radius * 2), 2)

#     def draw_spoke(self, num_spokes, center):
        
#         # Draw 8 radii (spokes)
#         for i in range(num_spokes):
#             angles = (2 * math.pi / num_spokes) * i
#             end_x = center[0] + self.radius * math.cos(angles) # center[100, 100]
#             end_y = center[1] + self.radius * math.sin(angles)
#             # Draw the spoke on the circle surface 
#             pygame.draw.line(self.circle_surface, (255, 255, 0), center, (end_y, end_x), 2)

#     def create_text_label(self, text, pos):
#         label = self.font.render(text, True, (0, 0, 0))
#         return label, pos

#     def get_info_elements(self, angular_velocity, last_spoke_hit):
#         elements = []

#         # Pointer rectangle (still needs to be drawn, not blitted)
#         # We'll return it separately
#         pointer = ('rect', (0, 255, 0), 2)

#         # Add text label if condition is met
#         if last_spoke_hit and angular_velocity == 0:
#             label, pos = self.create_text_label(f"Last Hit: {last_spoke_hit.data}", (10, 10))
#             elements.append((label, pos))

#         return pointer, elements


import pygame
from abc import ABC, abstractmethod

class UI(ABC):
    def __init__(self, width=800, height=800):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 20)

    def create_text_label(self, text, pos):
        label = self.font.render(text, True, (0, 0, 0))
        return label, pos

    @abstractmethod
    def get_elements(self):
        """
        Should return elements to be blitted or drawn.
        Must be implemented by subclasses.
        """
        pass
