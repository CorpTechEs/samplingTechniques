# Model | Data Processing
import pygame
import pygame.freetype
from sample import SampleModel
from rightpanel import RightPanel

class SampleController:
    def __init__(self, sample_size):
        self.Sample = SampleModel(sample_size)
        self.SamplePanel = RightPanel()
        self.sample_size = sample_size
        self.sample = []
        self.spins_done = 0
        self.ready_to_compare = False
        self.population = []

    def draw_samp(self):
        # Mock shapes for population going to model or controller
        if len(self.sample) > 0:
            # samp_x = self.SamplePanel.width - self.SamplePanel.panel_width - self.SamplePanel.panel_padding
            # panel_y = 180
            # for idx, item in enumerate(self.sample):
            #     pygame.draw.rect(self.SamplePanel.screen, (255, 100, 100), (samp_x + 30, panel_y + 30 + idx * 60, 30, 30))

            # … after drawing right_rect and sample_label …

            # 1) Prepare a proper emoji font
            icon_font = pygame.freetype.SysFont("Segoe UI Emoji",
                                                self.SamplePanel.ICON_FONT_SIZE)

            samp_x   = self.SamplePanel.width  - self.SamplePanel.panel_width - self.SamplePanel.panel_padding
            panel_y  = 180

            for idx, item in enumerate(self.sample):
                # render → (Surface, Rect)
                symbol_surf, _ = icon_font.render(item['shape'], item['color'])

                # position using your supplied offsets + consistent spacing
                x = samp_x + 30
                y = panel_y + 30 + idx * 60

                # get_rect on the surface—use topleft so it hugs your grid
                symbol_rect = symbol_surf.get_rect(topleft=(x, y))

                self.SamplePanel.screen.blit(symbol_surf, symbol_rect)

    def set_sample(self, sample):
        self.Sample.add_user_sample(sample)
        self.sample = sample
    
    def record_user_spin(self, selected_value):
        if self.spins_done < self.expected_sample_size:
            self.Sample.add_user_sample(selected_value)
            self.spins_done += 1

        if self.spins_done == self.expected_sample_size:
            self.Sample.generate_system_sample(self.expected_sample_size)
            self.ready_to_compare = True

    def render(self, screen):
        user_sample, system_sample = self.SamplePanel.get_samples()
        self.SamplePanel.draw_samples(screen, user_sample, system_sample)

        if self.ready_to_compare:
            result, score_user, score_sys = self.SamplePanel.compare_samples()
            self.SamplePanel.draw_result(screen, f"{result} ({score_user} vs {score_sys})")

    def reset_sampling(self):
        self.spins_done = 0
        self.ready_to_compare = False
        self.Sample.clear_samples()