import pygame
import math
# View/ UI

class UI:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.radius = 100
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 20)
        self.pointer_rect = pygame.Rect((395, 290),(10, 20))
        # self.screen.fill((255, 255, 255))
        self.circle_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.circle_surface, (255, 0, 0), (self.radius, self.radius), self.radius)
        # pygame.draw.circle(self.circle_surface, (255, 0, 0), (self.width // 2, self.height // 2 + 20), self.radius)
        pygame.draw.line(self.circle_surface, (0, 0, 0), (0, 0), (self.radius * 2, self.radius * 2), 2)
        
        # # Draw pointer
        # pygame.draw.rect(self.screen, (0, 255, 0), self.pointer_rect, 2)
        # pygame.display.update()

    def draw_spoke(self, num_spokes, center):
        
        # Draw 8 radii (spokes)
        for i in range(num_spokes):
            angles = (2 * math.pi / num_spokes) * i
            end_x = center[0] + self.radius * math.cos(angles)
            end_y = center[1] + self.radius * math.sin(angles)
            # Draw the spoke on the circle surface 
            pygame.draw.line(self.circle_surface, (255, 255, 255), center, (end_x, end_y), 2)

    def draw_text(self,text, pos):
        label = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(label, pos)


    def draw_info(self, torque, angular_velocity, angle, angular_acceleration, force_applied, radius, I, last_spoke_hit):
        # Display debug info
        # self.screen.fill((255, 255, 255))
        # self.draw_text(f"Torque: {torque:.2f} Nm", (10, 10))
        # self.draw_text(f"Angular Velocity: {angular_velocity:.2f} rad/s", (10, 30))
        # self.draw_text(f"Angle: {angle:.2f} rad", (10, 50))
        # self.draw_text(f"Angular Acceleration: {angular_acceleration:.2f} rad/s^2", (10, 70))
        # self.draw_text(f"Force Applied: {force_applied:.2f} N", (10, 90))
        # self.draw_text(f"Radius: {radius:.2f} m", (10, 110))
        # self.draw_text(f"Moment of Inertia: {I:.2f} kg*m^2", (10, 130))
        
        # Draw pointer
        pygame.draw.rect(self.screen, (0, 255, 0), self.pointer_rect, 2)

        if last_spoke_hit and angular_velocity == 0:
            self.draw_text(f"Last Hit: {last_spoke_hit.data}", (10, 10))
        
        # pygame.display.flip()

