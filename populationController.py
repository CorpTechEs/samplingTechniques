# Model | Data Processing
import pygame
import pygame.freetype
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
        xx = 0

        # Configuration: tweak these values to taste
        PADDING_X = self.PopulationPanel.panel_padding + 40
        PADDING_Y = self.PopulationPanel.panel_top + 40

        # Create a bigger emoji-capable font
        icon_font = pygame.freetype.SysFont("Segoe UI Emoji", self.PopulationPanel.ICON_FONT_SIZE)


        for idx, item in enumerate(self.population):
            # Render returns (surface, rect)
            symbol_surf, _ = icon_font.render(item['shape'], item['color'])

            # Position each icon in a vertical list, spaced out
            x = PADDING_X
            y = PADDING_Y + idx * self.PopulationPanel.VERTICAL_SPACING

            # Use get_rect() on the surface only
            symbol_rect = symbol_surf.get_rect(center=(x, y))

            # Blit onto the screen
            self.PopulationPanel.screen.blit(symbol_surf, symbol_rect)
            self.PopulationPanel.screen.blit(item['avators'], (50 + xx, 320))
            xx += 25
        
