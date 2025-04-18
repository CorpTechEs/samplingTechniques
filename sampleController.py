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
                font = self.SamplePanel.font   # Reuse the existing UI font
                symbol_surface = font.render(i['shape'], True, i['color'])  # Black color text
                symbol_rect = symbol_surface.get_rect(center=(
                    self.SamplePanel.panel_padding + 30,
                    self.SamplePanel.panel_top + 30 + i['id'] + 1 * 60
                ))
                self.SamplePanel.screen.blit(symbol_surface, symbol_rect)

    def set_sample(self, sample):
        self.Sample.add_user_sample(sample)
    
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