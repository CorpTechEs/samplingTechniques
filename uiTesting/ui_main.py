import pygame
from controller import Controller

pygame.init()

pygame.display.set_caption("Sampling UI")
clock = pygame.time.Clock()

controller = Controller(10)

def load_image(path, scale=None):
    img = pygame.image.load(path).convert_alpha()
    if scale:
        img = pygame.transform.scale(img, scale)
    return img

# background
bg = load_image("./uiTesting/bg.jpg", (controller.view.width, controller.view.height))

# panels population and sample
pop_panel = load_image("./uiTesting/pop_panel.png")
samp_panel = load_image("./uiTesting/sample_panel.png")

# sampling buttons
btn_srs = load_image("./uiTesting/srs_btn.png")
btn_sys = load_image("./uiTesting/sys_btn (2).png")
btn_cluster = load_image("./uiTesting/strati_btn (2).png")
btn_stratified = load_image("./uiTesting/cluster_btn.png")

# highlighted sampling buttons
btn_srs_2 = load_image("./uiTesting/srs_btn (2).png")
btn_sys_2 = load_image("./uiTesting/sys_btn.png")
btn_cluster_2 = load_image("./uiTesting/strati_btn.png")
btn_stratified_2 = load_image("./uiTesting/cluster_btn (2).png")

# action buttons
btn_populate = load_image("./uiTesting/populate_btn.png")
btn_challenge = load_image("./uiTesting/challenge_btn.png")

# highlighted action buttons
btn_populate_2 = load_image("./uiTesting/populate_btn (2).png")
btn_challenge_2 = load_image("./uiTesting/challenge_btn (2).png")

# verti bar 
vbar = load_image("./uiTesting/gbar.png")

# jar 
jarA = load_image("./uiTesting/JARa.png")
jarB = load_image("./uiTesting/JARb.png")
jarC = load_image("./uiTesting/JARc.png")
jarD = load_image("./uiTesting/JARd.png")


# Population Members
pop_member_1 = load_image("./uiTesting/circle_pop.png")                                     
pop_member_2 = load_image("./uiTesting/n_pop.png")                                     
pop_member_3 = load_image("./uiTesting/o_pop.png")                                     
pop_member_4 = load_image("./uiTesting/u_pop.png")                                     
pop_member_5 = load_image("./uiTesting/star_pop.png")                                     
pop_member_6 = load_image("./uiTesting/square_pop.png")                                     
pop_member_7 = load_image("./uiTesting/pentagon_pop.png")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    controller.view.screen.blit(bg, (0, 0))                     # draw background
    controller.view.screen.blit(pop_panel, (0, 200))            # draw Panles
    controller.view.screen.blit(samp_panel, (460, 200))         # draw Panles

    controller.view.screen.blit(btn_srs, (0, 75))               # draw btn srs
    controller.view.screen.blit(btn_sys, (200, 75))             # draw btn sys
    controller.view.screen.blit(btn_cluster, (380, 75))         # draw btn cluster
    controller.view.screen.blit(btn_stratified, (600, 75))      # draw btn stratified

    controller.view.screen.blit(btn_populate, (100, 670))       # draw btn populate
    controller.view.screen.blit(btn_challenge, (580, 670))      # draw btn challenge

    controller.view.screen.blit(pop_member_1, (50 + 0, 320))    # draw population members
    controller.view.screen.blit(pop_member_2, (50 + 25, 320))   # draw population members
    controller.view.screen.blit(pop_member_3, (50 + 50, 320))   # draw population members
    controller.view.screen.blit(pop_member_4, (50 + 75, 320))   # draw population members
    controller.view.screen.blit(pop_member_5, (50 + 100, 320))  # draw population members
    controller.view.screen.blit(pop_member_6, (50 + 125, 320))  # draw population members
    controller.view.screen.blit(pop_member_7, (50 + 150, 320))  # draw population members
    
    controller.view.screen.blit(jarA, (800, 575))  # draw jar
    controller.view.screen.blit(jarB, (800, 395))  # draw jar
    controller.view.screen.blit(jarC, (800, 200))  # draw jar
    controller.view.screen.blit(jarD, (800, 0))    # draw jar

    # screen.blit(vbar, (800, -10))  # drawing a verticle bar

    controller.update()
    controller.trigger_spin()
    controller.check_spokes_for_collision()
    controller.render_frame()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()