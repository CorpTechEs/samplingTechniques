import pygame

class CollectionJarModel:
    def __init__(self, num_jars=4):
        self.num_jars = num_jars
        self.jars = {f"Jar_{i+1}": [] for i in range(num_jars)}

    def stratify(self, population, key_func):
        """
        Group population based on a key function.
        Example: key_func = lambda p: p['gender']
        """
        self.clear_jars()
        for member in population:
            key = key_func(member)
            if key not in self.jars:
                self.jars[key] = []
            self.jars[key].append(member)

    def cluster(self, population):
        """
        Randomly assign population into jars (clusters)
        """
        self.clear_jars()
        shuffled = population[:]
        random.shuffle(shuffled)
        for i, member in enumerate(shuffled):
            jar_id = f"Jar_{(i % self.num_jars) + 1}"
            self.jars[jar_id].append(member)

    def clear_jars(self):
        for key in self.jars:
            self.jars[key] = []

    def get_jar(self, jar_id):
        return self.jars.get(jar_id, [])

    def get_all_jars(self):
        return self.jars
