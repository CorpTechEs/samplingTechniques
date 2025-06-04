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
        item_spacing_y = 25
        font = pygame.font.SysFont("arial", 18, bold=True)
    
        if population:
            item_width = population[0]['shape'].image.get_width()
            item_height = population[0]['shape'].image.get_height()
    
            x = 0
            y = 0
    
            for item in population:
                if x + item_width > self.panel_width:
                    x = 0
                    y += item_height + item_spacing_y  # Move to next row if overflow

                self.scroll_surface.blit(item['shape'].image, (x, y))

                # Draw point below the shape
                point_text = font.render(str(item.get('point', 0)), True, (255, 255, 255))
                text_rect = point_text.get_rect(center=(x + item_width // 2, y + item_height + 10))
                self.scroll_surface.blit(point_text, text_rect)

                x += item_width + item_spacing_x  # ✔ Increase x for the next item on the row

                # if self.panel_name == "population":
                #     # Now blit the visible portion of scroll surface to screen
                #     visible_area1 = pygame.Rect(self.scroll_x, self.scroll_y, self.panel_width, self.panel_height - 210)
                #     self.screen.blit(self.scroll_surface, (self.panel_pop_x, self.panel_pop_y), area=visible_area1)

                # if self.panel_name == "sample":
                #     # Now blit the visible portion of scroll surface to screen
                #     visible_area = pygame.Rect(self.scroll_x, self.scroll_y, self.panel_width, self.panel_height - 210)
                #     self.screen.blit(self.scroll_surface, (self.panel_sample_x, self.panel_sample_y), area=visible_area)

        # Blit scroll surface based on panel name
        visible_area = pygame.Rect(self.scroll_x, self.scroll_y, self.panel_width, self.panel_height - 210)
        if self.panel_name == "population":
            self.screen.blit(self.scroll_surface, (self.panel_pop_x, self.panel_pop_y), area=visible_area)
        elif self.panel_name == "sample":
            self.screen.blit(self.scroll_surface, (self.panel_sample_x, self.panel_sample_y), area=visible_area)

    def handle_event(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y -= event.y * self.scroll_speed  # y is positive when scrolling up
            # Clamp scroll_y to valid range
            max_scroll = max(0, self.scroll_surface.get_height() - self.panel_height + 100)
            self.scroll_y = max(0, min(self.scroll_y, max_scroll))

    def draw_right_column_items(self, items):
        column_width  = int(0.08 * 1050)  # 8% of window width = 84
        column_height = int(0.10 * 780)   # not used directly here
        column_x = 1050 - column_width    # Start at far right
        column_y = column_height          # Top Y position

        # Draw the right column border
        column_rect = pygame.Rect(column_x, column_y, column_width, self.height)
        pygame.draw.rect(self.screen, (0, 0, 0), column_rect, 2)

        if not items:
            return

        item_spacing_x = 5
        item_spacing_y = 10  # Slightly larger to accommodate text below

        item_width = items[0]['shape'].image.get_width()
        item_height = items[0]['shape'].image.get_height()

        items_per_row = max(1, (column_width - item_spacing_x) // (item_width + item_spacing_x))

        x_start = column_x + 10
        x = x_start
        y = column_y

        font = pygame.font.SysFont("arial", 12)

        for index, item in enumerate(items):
            # Draw item shape
            self.screen.blit(item['shape'].image, (x, y))

            # Draw point value below the shape
            point_text = font.render(str(item.get('point', 0)), True, (255, 255, 255))
            text_rect = point_text.get_rect(center=(x + item_width // 2, y + item_height + 10))
            self.screen.blit(point_text, text_rect)

            # Move to next position
            if (index + 1) % items_per_row == 0:
                x = x_start
                y += item_height + item_spacing_y + 15  # 15px for text
            else:
                x += item_width + item_spacing_x

        # Display total points at the bottom
        total_points = sum(item.get('point', 0) for item in items)
        total_text = pygame.font.SysFont("arial", 15, bold=True).render(
            f"System Sample Points (beat this): {total_points}", True, (255, 255, 255)
        )
        text_rect = total_text.get_rect(bottomright=(column_x + column_width - 10, self.height - 10))
        self.screen.blit(total_text, text_rect)

