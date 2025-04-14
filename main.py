import pygame
from controller import Controller
from populationController import PopulationController
from sampleController import SampleController
from sampleTController import SampleTechniqueController
from jarController import CollectionJarController

pygame.init()
controller = Controller(8)
PopulationPanel = PopulationController(population_size=10)
PopulationPanel.create_population()

SamplePanel = SampleController(sample_size=5)
SampleTechnique = SampleTechniqueController()
jars = CollectionJarController()


# def draw_ui(controller=controller):
#     screen = controller.UI.screen
#     font = controller.UI.font
#     screen.fill((255, 255, 255))  # White background

#     screen_width, screen_height = screen.get_size()

#     # Panel dimensions (25% each for population and sample)
#     panel_width = int(screen_width * 0.2)
#     panel_height = int(screen_height * 0.65)
#     panel_y = 180
#     padding = 10

#     # === Population Panel ===
#     pop_x = padding
#     pygame.draw.rect(screen, (200, 200, 200), (pop_x, panel_y, panel_width, panel_height), 3)
#     pop_label = font.render("Population", True, (0, 0, 0))
#     pop_label_rect = pop_label.get_rect(center=(pop_x + panel_width // 2, panel_y - 20))
#     screen.blit(pop_label, pop_label_rect)

#     # Mock shapes for population
#     for i in range(6):
#         pygame.draw.circle(screen, (100, 100, 255), (pop_x + 30, panel_y + 30 + i * 60), 15)

#     # === Sample Panel ===
#     samp_x = screen_width - panel_width - padding
#     pygame.draw.rect(screen, (200, 200, 200), (samp_x, panel_y, panel_width, panel_height), 3)
#     samp_label = font.render("Sample", True, (0, 0, 0))
#     samp_label_rect = samp_label.get_rect(center=(samp_x + panel_width // 2, panel_y - 20))
#     screen.blit(samp_label, samp_label_rect)

#     # Mock shapes for sample
#     for i in range(6):
#         pygame.draw.rect(screen, (255, 100, 100), (samp_x + 30, panel_y + 30 + i * 60, 30, 30))

#     # "Go Against" button inside the sample panel
#     go_btn_width = 100
#     go_btn_height = 30
#     go_btn_x = samp_x + panel_width // 2 - go_btn_width // 2
#     go_btn_y = panel_y + panel_height - go_btn_height - 10
#     pygame.draw.rect(screen, (0, 128, 255), (go_btn_x, go_btn_y, go_btn_width, go_btn_height), 0)
#     go_label = font.render("Go Against", True, (255, 255, 255))
#     screen.blit(go_label, (go_btn_x + 10, go_btn_y + 5))

#     # === Technique Buttons ===
#     techniques = ["SRS", "SYS", "STRATIFIED", "CLUSTER"]
#     for i, tech in enumerate(techniques):
#         btn_x = 160 + i * 120
#         btn_y = 100
#         pygame.draw.rect(screen, (0, 128, 255), (btn_x, btn_y, 100, 30), 2)
#         label = font.render(tech, True, (0, 0, 0))
#         label_rect = label.get_rect(center=(btn_x + 50, btn_y + 15))
#         screen.blit(label, label_rect)

#     # === Spin Circle ===
#     center_x = screen_width // 2
#     center_y = screen_height // 2 + 20
#     spin_radius = 80
#     pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), spin_radius, 3)
#     spin_label = font.render("Spin", True, (0, 0, 0))
#     spin_label_rect = spin_label.get_rect(center=(center_x, center_y + spin_radius + 20))
#     screen.blit(spin_label, spin_label_rect)

#     # === U-shaped Squares at Bottom, spread in center 50% ===
#     u_box_size = 60
#     u_gap = 40
#     total_u_width = 4 * u_box_size + 3 * u_gap
#     u_area_start_x = (screen_width // 2) - (total_u_width // 2)
#     u_y_top = panel_y + panel_height - u_box_size  # Align with bottom of panels

#     for i in range(4):
#         x = u_area_start_x + i * (u_box_size + u_gap)
#         # Draw U-shape (left, bottom, right)
#         pygame.draw.line(screen, (0, 0, 0), (x, u_y_top), (x, u_y_top + u_box_size), 3)
#         pygame.draw.line(screen, (0, 0, 0), (x, u_y_top + u_box_size), (x + u_box_size, u_y_top + u_box_size), 3)
#         pygame.draw.line(screen, (0, 0, 0), (x + u_box_size, u_y_top), (x + u_box_size, u_y_top + u_box_size), 3)

#     pygame.display.flip()

while True:
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
