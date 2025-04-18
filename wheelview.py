import math
import pygame
from sysui import SysUI
from Spoke import Spoke

class WheelView:
    """
    View component for rendering the spinning wheel (circle & spokes).
    """
    def __init__(self, sysui: SysUI, num_spokes: int, radius: float = None):
        self.sysui = sysui
        self.ui = sysui.ui

        # Wheel geometry
        self.num_spokes = num_spokes
        # Allow override of radius; default to UI panel area
        self.radius = radius or min(self.ui.width, self.ui.height) * 0.25
        self.center = (self.ui.width // 2, self.ui.height // 2)

        # Prepare off-screen surface for the wheel
        size = int(self.radius * 2)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA)

        # Initialize spokes
        self.spokes = [Spoke(i, num_spokes, self.radius) for i in range(num_spokes)]

    def draw(self, angle: float):
        """
        Draw the wheel with current rotation angle.

        Args:
            angle (float): Current rotation in radians.
        """
        # Clear the wheel surface
        self.surface.fill((0, 0, 0, 0))  # transparent fill

        # Draw the wheel circle
        pygame.draw.circle(
            self.surface,
            (200, 50, 50),
            (self.radius, self.radius),
            int(self.radius)
        )

        # Draw each spoke
        for spoke in self.spokes:
            start, end = spoke.get_rotated_position(angle, (self.radius, self.radius))
            pygame.draw.line(
                self.surface,
                (255, 255, 255),
                start,
                end,
                2
            )

        # Rotate entire surface for display
        angle_deg = math.degrees(angle)
        rotated_surface = pygame.transform.rotate(self.surface, -angle_deg)
        rotated_rect = rotated_surface.get_rect(center=self.center)

        # Blit to main screen
        self.ui.screen.blit(rotated_surface, rotated_rect)

    def get_spoke_lines(self, angle: float):
        """
        Return the start/end positions of all spokes at the given angle on screen.
        Useful for collision detection.
        """
        lines = []
        for spoke in self.spokes:
            start_local, end_local = spoke.get_rotated_position(angle, (self.radius, self.radius))
            # Translate local to screen coordinates
            sx, sy = self.center
            start = (sx - self.radius + start_local[0], sy - self.radius + start_local[1])
            end = (sx - self.radius + end_local[0], sy - self.radius + end_local[1])
            lines.append((start, end))
        return lines
