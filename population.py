# Model | Data Processing
import pygame
import math
import random

class PopulationModel:
    def __init__(self, size):
        self.size = size
        self.shapes = ['⚫','◾','⬜','⬛','◼️','◽','🟫','🟨','🟩','⏹️','🔺','🔻','🔽','🔼','◀️','▶️', '⚪', '🟤','🟣','⭕','⏺️','🔲','▪️','▫️','◻️']
        self.colors = [(255, 20, 147), (0, 191, 255), (152, 255, 152),(255, 165, 0), (255, 255, 102), (0, 0, 0), (255, 255, 255), (148, 0, 211)]
        self.shades = ['light', 'dark']
        self.sizes = ['small', 'medium']
        self.population = self.generate_population()
        self.clusters = []

    def generate_population(self):
        shapes = self.shapes
        colors = self.colors
        shades = self.shades
        sizes = self.sizes
        population = []

        for i in range(self.size):
          population.append({
                'id': i,
                'shape': random.choice(shapes),
                'color': random.choice(colors),
                'size': random.choice(sizes),
                'shade': random.choice(shades)
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
