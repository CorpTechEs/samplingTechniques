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
SampleTechnique.model.set_population(PopulationPanel.population)
SampleTechnique.model.set_sample_size(SamplePanel.sample_size)
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
        controller.trigger_spin()
        controller.update()
        controller.check_spokes_for_collision()
        
        # did we finish a spin?
        spoke_idx = controller.check_for_spin_end() 
        print(f"spoke_idx: {spoke_idx}")
        if spoke_idx is not None:
            done = SampleTechnique.model.record_spin(int(spoke_idx.data.replace("Segment ", "")))
            if done:
                sample = SampleTechnique.model.get_sample()
                SamplePanel.set_sample(sample)
                SamplePanel.draw_samp()
                spoke_idx = None
    else:
        print("Select a sampling technique first!")
    
    controller.render_frame()

    # Rotate and draw the circle
    # controller.rotate_and_draw_circle()
    # Display debug info


    
    pygame.display.flip()
    controller.model.clock.tick(60)

pygame.quit()