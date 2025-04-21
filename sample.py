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


    def generate_system_sample(self, sample_size, pop):
        """
        Manually build a system‐generated sample by picking random indices.
        Guarantees no duplicates and never goes out of bounds.
        """
        pop_len = len(pop)
        if sample_size > pop_len:
            print(f"[ERROR] Cannot sample {sample_size} from population of {pop_len}")
            self.system_sample = []
            return

        self.system_sample   = []
        selected_indices     = set()

        # Keep drawing until we have exactly sample_size items
        while len(self.system_sample) < sample_size:
            # randrange(0, pop_len) will always be in [0, pop_len-1]
            idx = random.randrange(pop_len)
            if idx in selected_indices:
                continue  # skip duplicates

            selected_indices.add(idx)
            self.system_sample.append(pop[idx])


    def get_samples(self):
        return self.user_sample, self.system_sample

    def compare_samples(self):

        # You can define your comparison logic here; for now, we'll use length or dummy scoring
        user_score    = sum(member['point'] for member in self.user_sample)
        machine_score = sum(members['point'] for members in self.system_sample)

        if user_score > machine_score:
            return "User Wins", user_score, machine_score
        elif machine_score > user_score:
            return "System Wins", user_score, machine_score
        else:
            return "Draw", user_score, machine_score