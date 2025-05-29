import pygame
from population import PopulationModel
from leftpanel import LeftPanel

class PopulationController:
    def __init__(self, population_size):
        self.PopulationPanel = LeftPanel()
        self.population_size = population_size
        self.Population = PopulationModel(population_size, [self.PopulationPanel.load_image("./uiElement/circle_pop.png"), 
                                                            self.PopulationPanel.load_image("./uiElement/n_pop.png"),
                                                            self.PopulationPanel.load_image("./uiElement/o_pop.png"),
                                                            self.PopulationPanel.load_image("./uiElement/u_pop.png"),
                                                            self.PopulationPanel.load_image("./uiElement/star_pop.png"),
                                                            self.PopulationPanel.load_image("./uiElement/square_pop.png"),
                                                            self.PopulationPanel.load_image("./uiElement/pentagon_pop.png"),
                                                        ])

    def create_population(self):
        self.population = self.Population.generate_population()

    def draw_pop(self):
        # First draw the panel background, borders, etc.
        self.PopulationPanel.draw()
        self.PopulationPanel.scrollable_panel(self.population)