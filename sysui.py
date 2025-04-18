from ui import UI

class PanelUI(UI):
    def __init__(self):
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
    
    def get_elements(self):
        """
        Should return elements to be blitted or drawn.
        Must be implemented by subclasses.
        """
        # elements = []
        # if last_spoke_hit and angular_velocity == 0:
        #     label, pos = self.create_text_label(f"Last Hit: {last_spoke_hit.data}", (10, 10))
        #     elements.append((label, pos))
        # return elements
    
        pass