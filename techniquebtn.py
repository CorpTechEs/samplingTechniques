import pygame
from sysui import PanelUI

class TechniqueButton(PanelUI):
    def __init__(self):
        super().__init__()
        self.techniques = [ "SRS", "SYS", "STRATIFIED", "CLUSTER"]
        
        self.technique_s = [ self.load_image("./uiElement/srs_btn.png"), 
                           self.load_image("./uiElement/sys_btn (2).png"), 
                           self.load_image("./uiElement/strati_btn (2).png"), 
                           self.load_image("./uiElement/cluster_btn.png")
                        ]

        self.technique_highlight = [ self.load_image("./uiElement/srs_btn (2).png"), 
                           self.load_image("./uiElement/sys_btn.png"), 
                           self.load_image("./uiElement/strati_btn.png"), 
                           self.load_image("./uiElement/cluster_btn (2).png")
                        ]
        
        self.selected_index = None
        self.rects = []  # Store button rectangles for interaction
        self.draw_btn()

    def draw_btn(self):
        """
        Draw all technique buttons and cache their rectangles.
        """
        pixel = [(0, 75), (200, 75), (380, 75), (600, 75)] 
        self.rects.clear()

        for i, tech in enumerate(self.techniques):
            btn_x = 160 + i * 120
            btn_y = 80
            rect = pygame.Rect(btn_x, btn_y, 100, 30)

            # Set colors based on selection state
            if self.selected_index == i:
                fill_color = (0, 200, 100)  # highlighted background
                border_color = (0, 0, 0)
            else:
                fill_color = (255, 255, 255)
                border_color = (0, 128, 255)

            # Draw button
            pygame.draw.rect(self.screen, fill_color, rect)
            pygame.draw.rect(self.screen, border_color, rect, 2)

            self.screen.blit(self.technique_s[i], pixel[i])           # draw btn

            # Draw label centered
            label = self.font.render(tech, True, (0, 0, 0))
            self.screen.blit(label, label.get_rect(center=rect.center))

            # Cache rect for click detection
            self.rects.append(rect)

    def get_button_rects(self):
        """
        Return cached button rectangles for controller collision checks.
        """
        return self.rects

    def highlight_selected(self, index):
        """
        Mark the given index as selected and redraw buttons.
        """
        self.selected_index = index
        self.draw_btn()

    def reset_buttons(self):
        """
        Clear selection highlights and redraw.
        """
        self.selected_index = None
        self.draw_btn()

    def handle_event(self, event):
        """
        Optional convenience method: handle click events within the view.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(self.rects):
                if rect.collidepoint(event.pos):
                    self.highlight_selected(i)
                    return (self.techniques[i], i)
        return None
