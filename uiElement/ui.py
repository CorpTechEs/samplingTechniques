import pygame
from abc import ABC, abstractmethod

class UI(ABC):
    def __init__(self, width=1050, height=780):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 20)

    def create_text_label(self, text, pos):
        label = self.font.render(text, True, (0, 0, 0))
        return label, pos

    @abstractmethod
    def get_elements(self):
        """
        Should return elements to be blitted or drawn.
        Must be implemented by subclasses.
        """
        pass
