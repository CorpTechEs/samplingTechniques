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
Jars = CollectionJarController()

while True:
    controller.view.screen.fill((255, 255, 255))  # Black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        SampleTechnique.handle_event(event)

    PopulationPanel.draw_pop()
    SamplePanel.draw_samp()
    SampleTechnique.draw()
    Jars.draw_jar()

    if SampleTechnique.model.locked:
        controller.update()
    else:
        print("Select a sampling technique first!")

    # Rotate and draw the circle
    # controller.rotate_and_draw_circle()
    # Display debug info

    controller.check_spokes_for_collision()
    controller.render_frame()
    
    pygame.display.flip()
    controller.model.clock.tick(60)

pygame.quit()