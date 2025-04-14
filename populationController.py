# Model | Data Processing
import pygame
import math
import random
from population import PopulationModel
from leftpanel import LeftPanel

class PopulationController:
    def __init__(self, population_size):
        self.Population = PopulationModel(population_size)
        self.PopulationPanel = LeftPanel()
        self.population_size = population_size
        self.population = []

    def create_population(self):
        self.population = self.Population.generate_population()

    def draw_pop(self):
        self.PopulationPanel.draw()
        # Mock shapes for population going to model or controller
        for i in self.population:
            font = self.PopulationPanel.sysui.ui.font   # Reuse the existing UI font
            symbol_surface = font.render(i['shape'], True, i['color'])  # Black color text
            symbol_rect = symbol_surface.get_rect(center=(
                self.PopulationPanel.sysui.panel_padding + 30,
                self.PopulationPanel.sysui.panel_top + 30 + i['id'] + 1 * 60
            ))
            self.PopulationPanel.sysui.ui.screen.blit(symbol_surface, symbol_rect)
        pygame.display.update()