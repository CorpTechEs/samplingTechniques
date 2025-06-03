import pygame
from sysui import PanelUI

class RightPanel(PanelUI):
    def __init__(self):
        self.sample_panel = self.load_image("./uiElement/sample_panel.png")
        self.panel_width    = self.sample_panel.get_width()
        self.panel_height   = self.sample_panel.get_height()
        super().__init__(self.panel_width, self.panel_height, "sample")
        self.right_rect = None
        self.go_btn_clickable = True
        self.result_text  = None
        self.label, self.pos = None, None

        # New attributes for storing result
        self.winner = None
        self.user_score = 0
        self.system_score = 0

        self.btn_challenge = self.load_image("./uiElement/challenge_btn.png")
        self.btn_challenge_2 = self.load_image("./uiElement/challenge_btn (2).png")

    def draw(self):
        # panels population and sample
        self.screen.blit(self.sample_panel, (460, 200))

        self.right_rect = self.btn_challenge.get_rect(topleft=(580, 670))
        self.draw_btn()

    def draw_btn(self):
        self.screen.blit(self.btn_challenge, (580, 670))
        

    def handle_event(self, event):
            """
            Call this from your controller or main loop:
                sample_panel.handle_event(event)
            """
            if self.go_btn_clickable:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.right_rect and self.right_rect.collidepoint(event.pos):
                        self.go_btn_clickable = False  # Disable the button after click
                        # you can also set a flag here, e.g.:
                        # self.go_clicked = True


    def draw_samples(self, user_sample, system_sample=[]):
        # Draw user sample (red)
        for i, _ in enumerate(user_sample):
            rect = pygame.Rect(self.user_x, self.y + i * (self.box_size + self.gap), self.box_size, self.box_size)
            pygame.draw.rect(self.screen, (255, 102, 102), rect)
        
        # Draw system sample (blue)
        for i, _ in enumerate(system_sample):
            rect = pygame.Rect(self.system_x, self.y + i * (self.box_size + self.gap), self.box_size, self.box_size)
            pygame.draw.rect(self.screen, (102, 178, 255), rect)
    
    def draw_result_text(self, winner, u_score, m_score):
        if winner is not None:
            result = f"{winner} wins ({u_score} vs {m_score})"
            font = pygame.font.SysFont("arial", 15, bold=True)
            text = font.render(result, True, (0, 0, 0))  # Black text
            text_rect = text.get_rect(center=(self.width - 500, 25))  # Top-center of the panel
            self.screen.blit(text, text_rect)

    def set_winner(self, winner=None):
        self.winner = winner

    
    
