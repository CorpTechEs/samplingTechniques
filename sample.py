import random

class SampleModel:
    def __init__(self):
        self.user_sample = []
        self.system_sample = []
        self.population = []

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
        user_score    = sum(member['point'] for member in self.user_sample)
        machine_score = sum(member['point'] for member in self.system_sample)

        if user_score > machine_score:
            return "User Wins", user_score, machine_score
        elif machine_score > user_score:
            return "System Wins", user_score, machine_score
        else:
            return "Draw", user_score, machine_score