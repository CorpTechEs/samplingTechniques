import pygame
from sysui import PanelUI

class LeftPanel(PanelUI):
    def __init__(self):
        super().__init__()
        self.pop_panel = self.load_image("./uiElement/pop_panel.png")
        self.btn_populate = self.load_image("./uiElement/populate_btn.png")
        self.btn_populate_2 = self.load_image("./uiElement/populate_btn (2).png")
        self.panel_width    = self.pop_panel.get_width()
        self.panel_height   = self.pop_panel.get_height()

        # Scrollable surface setup
        self.scroll_x = 0
        self.scroll_y = 0
        self.scroll_speed = 10

        # Dimensions of the visible panel
        self.panel_x = 50
        self.panel_y = 320

        # Create a scrollable surface — large enough to contain overflow
        self.scroll_surface = pygame.Surface((self.panel_width, self.panel_height), pygame.SRCALPHA)  # 2000px height for now


    def draw(self):
        # panels population and sample
        self.screen.blit(self.pop_panel, (0, 200))
        self.draw_btn(self.btn_populate, (100, 670))

    def scrollable_panel(self, population):
        self.scroll_surface.fill((0, 0, 0, 0))  # clear scroll surface
        item_spacing_x = 5
        item_spacing_y = 5
    
        if population:
            item_width = population[0]['shape'].get_width()
            item_height = population[0]['shape'].get_height()
    
            x = 0
            y = 0
    
        for item in population:
            if x + item_width > self.panel_width:
                x = 0
                y += item_height + item_spacing_y  # Move to next row if overflow
            
            self.scroll_surface.blit(item['shape'], (x, y))
            x += item_width + item_spacing_x  # ✔ Increase x for the next item on the row
    
        # Now blit the visible portion of scroll surface to screen
        visible_area = pygame.Rect(self.scroll_x, self.scroll_y, self.panel_width - 100, self.panel_height - 210)
        self.screen.blit(self.scroll_surface, (self.panel_x, self.panel_y), area=visible_area)

    def handle_event(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y -= event.y * self.scroll_speed  # y is positive when scrolling up
            # Clamp scroll_y to valid range
            max_scroll = max(0, self.scroll_surface.get_height() - self.panel_height + 100)
            self.scroll_y = max(0, min(self.scroll_y, max_scroll))