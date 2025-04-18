import pygame
from controller import Controller
from populationController import PopulationController
from sampleController import SampleController
from sampleTController import SampleTechniqueController
from jarController import CollectionJarController

pygame.init()
controller = Controller(10)
PopulationPanel = PopulationController(population_size=10)
PopulationPanel.create_population()

SamplePanel = SampleController(sample_size=5)
SampleTechnique = SampleTechniqueController()
jars = CollectionJarController()



while True:
    controller.UI.screen.fill((255, 255, 255))  # Black background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    PopulationPanel.draw_pop()
    SamplePanel.draw_samp()
    SampleTechnique.draw_btn()
    jars.draw_jar()
    # draw_ui()
    controller.update()

    # Rotate and draw the circle
    controller.rotate_and_draw_circle()
    # Display debug info

    controller.check_spokes_for_collision()
    controller.update_stats()
    
    pygame.display.flip()
    controller.Model.clock.tick(60)

pygame.quit()