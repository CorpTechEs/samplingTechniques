import random

class SampleModel:
    def __init__(self, population):
        self.user_sample = []
        self.system_sample = []
        self.population = population

    def set_population(self, population):
        self.population = population

    def add_user_sample(self, member):
        self.user_sample = member

    def clear_samples(self):
        self.user_sample = []
        self.system_sample = []

    def generate_system_sample(self, sample_size):
        if len(self.population) >= sample_size:
            self.system_sample = random.sample(self.population, sample_size)

    def get_samples(self):
        return self.user_sample, self.system_sample

    def compare_samples(self):
        # You can define your comparison logic here; for now, we'll use length or dummy scoring
        score_user = sum(self.user_sample)
        score_system = sum(self.system_sample)

        if score_user > score_system:
            return "User Wins", score_user, score_system
        elif score_system > score_user:
            return "System Wins", score_user, score_system
        else:
            return "Draw", score_user, score_system