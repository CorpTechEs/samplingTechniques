import pygame
from Spoke import Spoke
from model import Model
from wheelview import WheelView  # renamed UI import to WheelView

class Controller:
    def __init__(self, num_spokes):
        self.model = Model()
        self.view = WheelView()  # instantiate the specialized wheel view
        self.num_spokes = num_spokes
        self.spin_in_progress = False

        # Calculate center once
        self.center = (400, 560)

        # Initialize spokes
        self.spokes = [Spoke(i, num_spokes, self.view.radius) for i in range(num_spokes)]
        # Pre-draw static wheel spokes onto the circle surface
        self.view.draw_spokes(self.num_spokes, [400, 560])

        self.last_spoke_hit = None
        self.rect = None

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            # Apply a one-time torque when space is pressed
            self.model.apply_torque = True
            if self.model.apply_torque:
                self.model.force_applied = 0.3
                self.model.torque = self.model.force_applied * self.view.radius
                self.model.apply_torque = False

        self.model.update()
        self.check_spokes_for_collision()

    def lines_intersect(self, p1, p2, q1, q2):
        def ccw(a, b, c):
            return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])
        return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))

    def spoke_hits_rect(self, spoke_start, spoke_end, rect):
        rect_points = [rect.topleft, rect.topright, rect.bottomright, rect.bottomleft]
        rect_edges = [
            (rect_points[0], rect_points[1]),
            (rect_points[1], rect_points[2]),
            (rect_points[2], rect_points[3]),
            (rect_points[3], rect_points[0])
        ]
        for edge_start, edge_end in rect_edges:
            if self.lines_intersect(spoke_start, spoke_end, edge_start, edge_end):
                return True
        return False

    def check_spokes_for_collision(self):
        # Rotate and get current wheel rectangle
        rotated_surface = pygame.transform.rotate(self.view.circle_surface, self.model.angle)
        self.rect = rotated_surface.get_rect(center=self.center)

        # Check each spoke for collision against the pointer_rect in view
        for spoke in self.spokes:
            start, end = spoke.get_rotated_position(self.model.angle, self.rect.center)
            if self.spoke_hits_rect(start, end, self.view.pointer_rect):
                spoke.last_hit_time = pygame.time.get_ticks()
                self.last_spoke_hit = spoke

    def render_frame(self):
        # Draw rotated wheel
        rotated_surface = pygame.transform.rotate(self.view.circle_surface, self.model.angle)
        self.rect = rotated_surface.get_rect(center=self.center)
        self.view.screen.blit(rotated_surface, self.rect)

        # Draw pointer (shape)
        self.view.draw_pointer()

        # Collect UI elements (text labels, etc.)
        elements = self.view.get_elements(self.model.angular_velocity, self.last_spoke_hit)
        for label, pos in elements:
            self.view.screen.blit(label, pos)
        
    
    def trigger_spin(self):
        """"Call when user presses the space bar."""
        if not self.spin_in_progress and self.model.angular_velocity > 0:
            self.spin_in_progress = True

    def check_for_spin_end(self):
        """" Call after update and after collision check.
        Returns the index of the
        """

        if self.spin_in_progress and self.model.angular_velocity == 0:
            self.spin_in_progress = False
            if self.last_spoke_hit:
                return self.last_spoke_hit
        return None  # No spoke hit