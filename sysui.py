from ui import UI

class SysUI:
    def __init__(self):
        self.ui = UI()
            
        # Layout constants
        self.panel_padding = 3
        self.panel_width = self.ui.width * 0.25 - 2 * self.panel_padding
        self.panel_height = self.ui.height * 0.7
        self.panel_top = 130
        self.center_x = self.ui.width // 2
        self.center_y = self.ui.height // 2 + 20