from population import PopulationModel
from leftpanel import LeftPanel
from avator import Avatar

class PopulationController:
    def __init__(self, population_size):
        self.PopulationPanel = LeftPanel()
        self.population_size = population_size
        self.avatars = [
            Avatar(self.PopulationPanel.load_image("./uiElement/circle_pop.png"), "circle", (204, 0, 153), 'normal'),
            Avatar(self.PopulationPanel.load_image("./uiElement/n_pop.png"), "circle", (0, 255, 255), 'u'),
            Avatar(self.PopulationPanel.load_image("./uiElement/o_pop.png"), "circle", (204, 0, 153), 'zero'),
            Avatar(self.PopulationPanel.load_image("./uiElement/u_pop.png"), "circle", (0, 255, 255), 'n'),
            Avatar(self.PopulationPanel.load_image("./uiElement/star_pop.png"), "star", (0, 0, 255), 'normal'),
            Avatar(self.PopulationPanel.load_image("./uiElement/square_pop.png"), "square", (255, 0, 0), 'normal'),
            Avatar(self.PopulationPanel.load_image("./uiElement/pentagon_pop.png"), "pentagon", (204, 0, 153), 'normal'),
        ]
        self.Population = PopulationModel(population_size, self.avatars)

    def create_population(self):
        self.population = self.Population.generate_population()

    def draw_pop(self):
        # First draw the panel background, borders, etc.
        self.PopulationPanel.draw()
        self.PopulationPanel.scrollable_panel(self.population)