import pygame
from controller import Controller
from populationController import PopulationController
from sampleController import SampleController
from sampleTController import SampleTechniqueController
from jarController import CollectionJarController

pygame.init()
controller = Controller(10)
PopulationPanel = PopulationController(population_size=50)
PopulationPanel.create_population()

SamplePanel = SampleController(sample_size=5)
SampleTechnique = SampleTechniqueController()
SampleTechnique.model.set_population(PopulationPanel.population)
SampleTechnique.model.set_sample_size(SamplePanel.sample_size)
Jars = CollectionJarController()
SampleMode = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        SampleTechnique.handle_event(event)
        PopulationPanel.PopulationPanel.handle_event(event)
        SamplePanel.SamplePanel.handle_event(event)

    controller.view.screen.blit(controller.view.bg, (0, 0))
    PopulationPanel.draw_pop()
    SamplePanel.SamplePanel.draw()
    SampleTechnique.draw()

    if SampleTechnique.model.locked:
        controller.update()
        controller.trigger_spin()
        
        if SampleTechnique.model.selected_technique == 'SRS':
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
        elif SampleTechnique.model.selected_technique == 'SYS':
            # did we finish a spin?
            spoke_idx = controller.check_for_spin_end()
            if spoke_idx is not None:
                SampleTechnique.model.locked = False
                sample = SampleTechnique.model.select_nth_term(int(spoke_idx.data.replace("Segment ", "")))
                SamplePanel.set_sample(sample)
                SamplePanel.ready_to_compare = True
                spoke_idx = None
        elif SampleTechnique.model.selected_technique == 'STRATIFIED':
            Jars.draw_jar()
            bias = "color" # find a way to allow he user to input the bias
            shape   = PopulationPanel.Population.group_by('shape')  # these elements need to appear in the respective jar
            color   = PopulationPanel.Population.group_by('color')  # these elements need to appear in the respective jar
            size    = PopulationPanel.Population.group_by('size')   # these elements need to appear in the respective jar
            shade   = PopulationPanel.Population.group_by('shade')  # these elements need to appear in the respective jar

            # did we finish a spin?
            spoke_idx = controller.check_for_spin_end()
            if spoke_idx is not None:
                mod_result = int(spoke_idx.data.replace("Segment ", "")) % 4

                if  mod_result == 0:
                    done = SampleTechnique.model.strat(shape)
                if mod_result == 1:
                    done = SampleTechnique.model.strat(shape)
                if mod_result == 2:
                    done = SampleTechnique.model.strat(shape)
                if mod_result == 3:
                    done = SampleTechnique.model.strat(shape)
                
                if done:
                    sample = SampleTechnique.model.get_sample()
                    SamplePanel.set_sample(sample)
                    SamplePanel.ready_to_compare = True
                    spoke_idx = None
                    done = None
                    SampleTechnique.model.locked = False

        elif SampleTechnique.model.selected_technique == 'CLUSTER':
            Jars.draw_jar()

            # did we finish a spin?
            spoke_idx = controller.check_for_spin_end()

            if spoke_idx is not None:
                result = int(spoke_idx.data.replace("Segment ", ""))
                done = SampleTechnique.model.record_spin_cluster(result, 4)
                print(done)
                if done:
                    sample = SampleTechnique.model.get_sample()
                    SamplePanel.set_sample(sample)
                    SamplePanel.ready_to_compare = True
                    spoke_idx = None
                    done = None
                    SampleTechnique.model.locked = False

    # else:
    #     print("Select a sampling technique first!")
    if SamplePanel.ready_to_compare:
        SamplePanel.draw_samp()
        SamplePanel.handle_event(event, PopulationPanel.population)
    
    # SamplePanel.draw_winner()
    
    controller.check_spokes_for_collision()
    controller.render_frame()
    
    pygame.display.flip()
    controller.model.clock.tick(60)

pygame.quit()