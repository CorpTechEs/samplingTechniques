# Model | Data Processing
import pygame
import math
class Model:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.angle = 0
        self.dt = 1 / self.FPS
        self.I = 0.25
        self.torque = 0
        self.angular_velocity = 0
        self.apply_torque = False
        self.force_applied = 0
        self.angular_acceleration = 0


    def update(self):
        # Angular physics
        self.angular_acceleration = self.torque / self.I
        self.angular_velocity += self.angular_acceleration * self.dt
        if self.angular_velocity < 0:
            self.angular_velocity = 0
            self.torque = 0
            self.angular_acceleration = 0
        self.angle += self.angular_velocity * self.dt

        if not self.apply_torque:
            self.torque -= 0.25 if self.angular_velocity > 0 else 0