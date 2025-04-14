import pygame
from jatgroupee import CollectionJarModel
from jars import CollectionJar

class CollectionJarController:
    def __init__(self):
        self.model = CollectionJarModel()
        self.view = CollectionJar()

    def apply_stratified_sampling(self, population, key_func):
        self.model.stratify(population, key_func)
        self.view.update(self.model.get_all_jars())

    def apply_cluster_sampling(self, population):
        self.model.cluster(population)
        self.view.update(self.model.get_all_jars())

    def clear(self):
        self.model.clear_jars()
        self.view.update(self.model.get_all_jars())

    def draw_jar(self):
        self.view.draw()
