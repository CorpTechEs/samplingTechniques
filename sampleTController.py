import pygame
from sampleT import SampleTechniqueModel
from techniquebtn import TechniqueButton

class SampleTechniqueController:
    def __init__(self):
        self.model = SampleTechniqueModel()
        self.view = TechniqueButton()

    def handle_click(self, pos):
        if self.model.locked:
            return

        for i, rect in enumerate(self.view.get_button_rects()):
            if rect.collidepoint(pos):
                selected = self.model.techniques[i]
                self.model.select_technique(selected)
                self.view.highlight_selected(i)
                print(f"Selected technique: {selected}")
                break

    def lock_selection(self):
        self.model.lock()

    def reset(self):
        self.model.reset()
        self.view.reset_buttons()
    
    def draw_btn(self):
        self.view.draw_btn()
