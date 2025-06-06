import pygame
from controller import Controller
from populationController import PopulationController
from sampleController import SampleController
from sampleTController import SampleTechniqueController
from jarController import CollectionJarController
from button import ImageButton
from notification import Notification

pygame.init()
pop_set         = False
sample_set      = False
system_sample   = []
pop_size        = 0
sample_size     = 0
winner, u_score, m_score = None, 0, 0
controller      = Controller(0)
PopulationPanel = PopulationController(population_size=pop_size)
PopulationPanel.create_population()

SamplePanel = SampleController(sample_size=sample_size)
SampleTechnique = SampleTechniqueController()
SampleTechnique.model.set_population(PopulationPanel.population)
SampleTechnique.model.set_sample_size(SamplePanel.sample_size)
Jars = CollectionJarController()
SampleMode = None
inputBtn = ImageButton()
notificationBar = Notification()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not inputBtn.modal_active:
            SampleTechnique.handle_event(event)
            PopulationPanel.PopulationPanel.handle_event(event)
            SamplePanel.SamplePanel.handle_event(event)
        inputBtn.handle_event(event)
        # Just after inputBtn.handle_event(event)
        if not inputBtn.modal_active and inputBtn.inputs:
            if "Population" in inputBtn.inputs:
                pop_size        = inputBtn.inputs["Population"]
                controller      = Controller(pop_size)
                PopulationPanel = PopulationController(population_size=pop_size)
                PopulationPanel.create_population()
                SampleTechnique.model.set_population(PopulationPanel.population)
                pop_set = True

            if "Sample" in inputBtn.inputs:
                sample_size = inputBtn.inputs["Sample"]
                SamplePanel = SampleController(sample_size=sample_size)
                SampleTechnique.model.set_sample_size(SamplePanel.sample_size)
                sample_set = True

            if "Jars" in inputBtn.inputs:
                # If you want to do anything special with jars in the future
                pass
            
            if pop_set and sample_set:
                SamplePanel.Sample.generate_system_sample(sample_size, SampleTechnique.model.population)
                system_sample   = SamplePanel.Sample.system_sample
                pop_set         = False
                sample_set      = False

            inputBtn.inputs.clear()  # Reset after applying

    controller.view.screen.blit(controller.view.bg, (0, 0))
    PopulationPanel.draw_pop()
    SamplePanel.SamplePanel.draw()
    SampleTechnique.draw()
    notificationBar.draw_notification_bar("")
    inputBtn.draw()
    if system_sample:
        SamplePanel.SamplePanel.draw_right_column_items(system_sample)

    if SampleTechnique.model.locked and (pop_size > 0 and sample_size > 0):
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
            bias = "size" # find a way to allow he user to input the bias
            # shape   = PopulationPanel.Population.group_by('shape')  # these elements need to appear in the respective jar
            # color   = PopulationPanel.Population.group_by('color')  # these elements need to appear in the respective jar
            # size    = PopulationPanel.Population.group_by('size')   # these elements need to appear in the respective jar
            # head    = PopulationPanel.Population.group_by('head')  # these elements need to appear in the respective jar
            discrimiation   = PopulationPanel.Population.group_by(bias)  # these elements need to appear in the respective jar
            

            Jars.display_items_inside_jars( discrimiation )

            # did we finish a spin?
            spoke_idx = controller.check_for_spin_end()
            if spoke_idx is not None:
                mod_result = int(spoke_idx.data.replace("Segment ", "")) % 4

                if  mod_result == 0:
                    done = SampleTechnique.model.strat(discrimiation)
                if mod_result == 1:
                    done = SampleTechnique.model.strat(discrimiation)
                if mod_result == 2:
                    done = SampleTechnique.model.strat(discrimiation)
                if mod_result == 3:
                    done = SampleTechnique.model.strat(discrimiation)
                
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
        SamplePanel.handle_event(event)

    if SamplePanel.SamplePanel.winner_ready:
        SamplePanel.SamplePanel.draw_result_text(SamplePanel.winner, SamplePanel.u_score, SamplePanel.m_score)
        SamplePanel.reset_sampling()
    
    # SamplePanel.draw_winner()
    
    controller.check_spokes_for_collision()
    controller.render_frame()

    
    pygame.display.flip()
    controller.model.clock.tick(60)

pygame.quit()