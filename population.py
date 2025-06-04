# Model | Data Processing
from collections import defaultdict
import random

class PopulationModel:
    def __init__(self, size, avators):
        self.size = size
        self.avators = avators
        self.legs = ['normal', 'zero', 'u', 'n']
        self.points = [1, 2, 3, 4, 5]
        self.population = [] # self.generate_population()
        self.clusters = []


    def generate_population(self):
        # shapes = self.shapes
        points = self.points
        avators = self.avators
        population = []

        for i in range(self.size):
          avatee = avators[random.choice(range(len(avators)))]
          population.append({
                'id': i,
                'shape': avatee,
                'color': avatee.color,
                'size': avatee.legs,
                'point': random.choice(points)
          })
        return population

    def get_population(self):
        return self.population

    def group_by(self, key):
        if key not in ['shape', 'color', 'size', 'shade']:
          raise ValueError(f"Invalid '{key}'. Use 'shape', 'color', 'size', or 'shade'.")
        grouped = defaultdict(list)
        for member in self.population:
          grouped[member[key]].append(member)
        return dict(grouped)

    def get_demographics_summary(self):
        summary = {
          'shape': defaultdict(int),
          'color': defaultdict(int),
          'size': defaultdict(int),
          'shade': defaultdict(int)
        }
        for member in self.population:
          for key in summary:
            summary[key][member[key]] += 1
        return {k: dict(v) for k, v in summary.items()}

    def generate_clusters(self, num_clusters):
      if num_clusters <= 0 or num_clusters > self.size:
        raise ValueError("Number of clusters cannot exceed population size.")
      shuffled = self.population[:]
      random.shuffle(shuffled)

      self.clusters = [[] for _ in range(num_clusters)]
      for i, member in enumerate(shuffled):
        self.clusters[i % num_clusters].append(member)
      return self.clusters
    
    def get_systematic_sample(self, start_index, k):
        if not (0 <= start_index < self.size):
            raise ValueError("Invalid start index or k value.")
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        sample = []
        index = start_index
        while index < len(self.population):
            if index >= len(self.population):
                break
            sample.append(self.population[index])
            index += k
        return sample
