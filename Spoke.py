import math

# Spoke class
class Spoke:
    def __init__(self, index, total_spokes, radius, data=None):
        self.index = index
        self.angle_offset = (2 * math.pi / total_spokes) * index
        self.radius = radius
        self.data = data if data else f"Segment {index + 1}"
        self.last_hit_time = -1  # Track when it last hit the pointer

    def get_rotated_position(self, base_angle, center):
        total_angle = self.angle_offset + base_angle
        dx = self.radius * math.cos(total_angle)
        dy = self.radius * math.sin(total_angle)
        start = center
        end = (center[0] + dx, center[1] + dy)
        return start, end