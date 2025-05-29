import pygame
from ui import UI

class PanelUI(UI):
    def __init__(self, image_width=0, panel_height=0, panel_name=None):
        super().__init__()
        # Layout constants
        self.panel_padding = 3
        self.panel_width = self.width * 0.25 - 2 * self.panel_padding
        self.panel_height = self.height * 0.7
        self.panel_top = 130
        self.center_x = self.width // 2
        self.center_y = self.height // 2 + 20
        self.ICON_FONT_SIZE = 20
        self.VERTICAL_SPACING = 25
        self.panel_name = panel_name

        # Scrollable surface setup
        self.scroll_x = 0
        self.scroll_y = 0
        self.scroll_speed = 10

        # Dimensions of the visible panel
        self.panel_pop_x = 50
        self.panel_pop_y = 320

        # Dimensions of the visible panel
        self.panel_sample_x = 500
        self.panel_sample_y = 320

        # Create a scrollable surface — large enough to contain overflow
        self.scroll_surface = pygame.Surface((image_width, panel_height), pygame.SRCALPHA)  # 2000px height for now


    def draw_btn(self, URL, position):
        self.screen.blit(URL, position)
    
    def get_elements(self):
        """
        Should return elements to be blitted or drawn.
        Must be implemented by subclasses.
        """    
        pass

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
    
            if self.panel_name == "population":
                # Now blit the visible portion of scroll surface to screen
                visible_area1 = pygame.Rect(self.scroll_x, self.scroll_y, self.panel_width, self.panel_height - 210)
                self.screen.blit(self.scroll_surface, (self.panel_pop_x, self.panel_pop_y), area=visible_area1)
            
            if self.panel_name == "sample":
                # Now blit the visible portion of scroll surface to screen
                visible_area = pygame.Rect(self.scroll_x, self.scroll_y, self.panel_width, self.panel_height - 210)
                self.screen.blit(self.scroll_surface, (self.panel_sample_x, self.panel_sample_y), area=visible_area)

    def handle_event(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y -= event.y * self.scroll_speed  # y is positive when scrolling up
            # Clamp scroll_y to valid range
            max_scroll = max(0, self.scroll_surface.get_height() - self.panel_height + 100)
            self.scroll_y = max(0, min(self.scroll_y, max_scroll))