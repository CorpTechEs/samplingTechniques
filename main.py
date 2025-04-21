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
    SamplePanel.SamplePanel.draw()
    SampleTechnique.draw()
    Jars.draw_jar()

    if SampleTechnique.model.locked:
        controller.update()
        controller.trigger_spin()
        
        # did we finish a spin?
        spoke_idx = controller.check_for_spin_end() 
        if spoke_idx is not None:
            done = SampleTechnique.model.record_spin(int(spoke_idx.data.replace("Segment ", "")))
            if done:
                sample = SampleTechnique.model.get_sample()
                SamplePanel.set_sample(sample)
                SamplePanel.ready_to_compare = True
                spoke_idx = None
                done = None
                SampleTechnique.model.locked = False
    # else:
    #     print("Select a sampling technique first!")
    if len(SamplePanel.sample) == 5 and SamplePanel.ready_to_compare:
        SamplePanel.draw_samp()
        SamplePanel.handle_event(event, PopulationPanel.population)
    
    SamplePanel.draw_winner()
    
    controller.check_spokes_for_collision()
    controller.render_frame()
    
    pygame.display.flip()
    controller.model.clock.tick(60)

pygame.quit()