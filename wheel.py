class Wheel:
    def __init__(self, model):
        self.model = model
        self.radius = 100
        self.center = (self.radius, self.radius)
        self.num_spokes = 8
        self.last_spoke_hit = None