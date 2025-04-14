# Model | Data Processing
import pygame
import math
import random
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
        self.SamplePanel.draw()
        
        # Mock shapes for population going to model or controller
        if len(self.sample) > 0:
            for i in self.sample:
                font = self.SamplePanel.sysui.ui.font   # Reuse the existing UI font
                symbol_surface = font.render(i['shape'], True, i['color'])  # Black color text
                symbol_rect = symbol_surface.get_rect(center=(
                    self.SamplePanel.sysui.panel_padding + 30,
                    self.SamplePanel.sysui.panel_top + 30 + i['id'] + 1 * 60
                ))
                self.SamplePanel.sysui.ui.screen.blit(symbol_surface, symbol_rect)
            pygame.display.update()

    def set_population(self, population):
        self.model.set_population(population)
    
    def record_user_spin(self, selected_value):
        if self.spins_done < self.expected_sample_size:
            self.model.add_user_sample(selected_value)
            self.spins_done += 1

        if self.spins_done == self.expected_sample_size:
            self.model.generate_system_sample(self.expected_sample_size)
            self.ready_to_compare = True

    def render(self, screen):
        user_sample, system_sample = self.model.get_samples()
        self.SamplePanel.draw_samples(screen, user_sample, system_sample)

        if self.ready_to_compare:
            result, score_user, score_sys = self.model.compare_samples()
            self.SamplePanel.draw_result(screen, f"{result} ({score_user} vs {score_sys})")

    def reset_sampling(self):
        self.spins_done = 0
        self.ready_to_compare = False
        self.model.clear_samples()