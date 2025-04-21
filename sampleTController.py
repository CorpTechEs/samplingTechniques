import pygame
from sampleT import SampleTechniqueModel
from techniquebtn import TechniqueButton

class SampleTechniqueController:
    def __init__(self):
        self.model = SampleTechniqueModel()
        self.view = TechniqueButton()

    def handle_event(self, event):
        """
        Process a pygame event: handle clicks and any future events (e.g., hover).
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._handle_click(event)

    def _handle_click(self, event):
        """
        Select a technique if unlocked and a button was clicked.
        """
        btn = None

        if self.model.locked:
            return

        btn = self.view.handle_event(event)
        if btn is not None:
            self.model.select_technique(btn[0])
            self.lock_selection()
            return btn
    

    def lock_selection(self):
        """Prevent further selection."""
        self.model.lock()

    def reset(self):
        """Reset the model and clear the view selection."""
        self.model.reset()
        self.view.reset_buttons()

    def draw(self):
        """
        Draw the technique buttons to the screen.
        """
        self.view.draw_btn()

    def record_spin(self, spoke_number):
        """
        Record the spin result.
        """
        return self.model.record_spin(spoke_number)
    
    def get_sample(self):
        return self.model.get_sample()

