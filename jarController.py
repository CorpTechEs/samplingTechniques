import pygame
from jatgroupee import CollectionJarModel
from jars import CollectionJar

class CollectionJarController:
    def __init__(self):
        self.model = CollectionJarModel()
        self.view = CollectionJar()
        self.item_box_size = 40  # size of each image box
        self.jar_width = 180
        self.jar_height = 255
        self.padding = 10

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

    def display_items_inside_jars(self, categorized_population):
        jar_positions = {
            'circle': (800, 575),
            'star': (800, 395),
            'square': (800, 200),
            'pentagon': (800, 0),

            'u': (800, 575),
            'normal': (800, 395),
            'n': (800, 200),
            'zero': (800, 0),

            'u': (800, 575),
            'normal': (800, 395),
            'n': (800, 200),
            'zero': (800, 0),

            (0, 255, 255): (800, 575),
            (204, 0, 153): (800, 395),
            (255, 0, 0): (800, 200),
            (0, 0, 255): (800, 0),
        }

        for category, subcategories in categorized_population.items():

            for i, item in enumerate(subcategories):

                # Get jar position for the current category
                jar_x, jar_y = jar_positions[category]

                # Calculate grid layout
                cols = (self.jar_width - 2 * self.padding) // self.item_box_size
                rows = (self.jar_height - 2 * self.padding) // self.item_box_size
                max_items = cols * rows

                # Skip if more than max items (optional)
                if i >= max_items:
                    continue
                
                # Calculate position in the jar grid
                col = i % cols
                row = i // cols
                item_x = jar_x + self.padding + col * self.item_box_size
                item_y = jar_y + self.padding + row * self.item_box_size

                # Render the shape if it exists
                if "shape" in item:
                    shape_surface = item["shape"].image
                    self.view.screen.blit(shape_surface, (item_x, item_y))