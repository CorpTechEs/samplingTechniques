import pygame
from sysui import PanelUI
 
class ImageButton(PanelUI):
    def __init__(self):
        super().__init__()
        self.image = self.load_image("./uiElement/challenge_btn (2).png")  # This is a loaded Pygame surface (e.g., from pygame.image.load)
        self.rect = self.image.get_rect(topleft=(920,0))
        self.callback = self.draw_modal  # Function to call on click
        self.modal_active = False
        self.input_text = ""
        self.input_active = False
        self.responses = {}  # Store selected dropdown + typed value
        self.inputs = {}  # e.g., {"Population": 50, "Sample": 5}

        # Dropdown data
        self.dropdown_options = ["Jars", "Sample", "Population"]
        self.dropdown_selected = None  # None means no selection yet
        self.dropdown_open = False
        
        # Dropdown box rect (positioned above input box)
        self.dropdown_rect = pygame.Rect(250, 130, 300, 40)
        self.input_rect = pygame.Rect(250, 180, 300, 40)

    def draw(self):
        self.draw_btn(self.image, (920,0))

        # Draw the modal if active
        if self.modal_active:
            self.draw_modal()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.modal_active:
                self.modal_active = True
                self.input_text = ""
                self.dropdown_selected = None
                self.dropdown_open = False
                return  # Don't process further to avoid accidental clicks

            if self.modal_active:
                # Dropdown click
                if self.dropdown_rect.collidepoint(event.pos):
                    self.dropdown_open = not self.dropdown_open
                    return

                # Dropdown option click
                if self.dropdown_open:
                    for i, option_rect in enumerate(self.get_dropdown_option_rects()):
                        if option_rect.collidepoint(event.pos):
                            self.dropdown_selected = self.dropdown_options[i]
                            self.dropdown_open = False
                            return

                # Input field activation
                if self.input_rect.collidepoint(event.pos):
                    self.input_active = True
                else:
                    self.input_active = False

        if self.modal_active and event.type == pygame.KEYDOWN:
            if self.input_active:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if self.dropdown_selected:
                        self.responses[self.dropdown_selected] = self.input_text
                        print(f"Submitted: {self.dropdown_selected} = {self.input_text}")
                    if self.dropdown_selected and self.input_text.isdigit():
                        self.inputs[self.dropdown_selected] = int(self.input_text)
                        print(f"Saved: {self.dropdown_selected} = {self.input_text}")
                    self.input_text = ""
                    self.input_active = False
                    self.dropdown_selected = None
                    self.dropdown_open = False
                    self.modal_active = False

                else:
                    if event.unicode.isprintable():
                        self.input_text += event.unicode


    def draw_modal(self):
        # Dim background
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        # Modal box
        modal_rect = pygame.Rect(200, 100, 400, 350)
        pygame.draw.rect(self.screen, (255, 255, 255), modal_rect, border_radius=10)

        # Dropdown
        pygame.draw.rect(self.screen, (220, 220, 220), self.dropdown_rect, border_radius=5)
        dropdown_text = self.dropdown_selected or "Select an option"
        text_surface = self.font.render(dropdown_text, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.dropdown_rect.x + 10, self.dropdown_rect.y + 10))

        arrow_center = (self.dropdown_rect.right - 20, self.dropdown_rect.y + self.dropdown_rect.height // 2)
        if self.dropdown_open:
            pygame.draw.polygon(self.screen, (0, 0, 0), [
                (arrow_center[0] - 8, arrow_center[1] + 3),
                (arrow_center[0] + 8, arrow_center[1] + 3),
                (arrow_center[0], arrow_center[1] - 4),
            ])
        else:
            pygame.draw.polygon(self.screen, (0, 0, 0), [
                (arrow_center[0] - 8, arrow_center[1] - 3),
                (arrow_center[0] + 8, arrow_center[1] - 3),
                (arrow_center[0], arrow_center[1] + 4),
            ])

        if self.dropdown_open:
            for i, rect in enumerate(self.get_dropdown_option_rects()):
                pygame.draw.rect(self.screen, (240, 240, 240), rect)
                option_text = self.font.render(self.dropdown_options[i], True, (0, 0, 0))
                self.screen.blit(option_text, (rect.x + 10, rect.y + 10))

        # Input field
        # Change color based on focus
        input_color = (180, 220, 255) if self.input_active else (200, 200, 200)
        pygame.draw.rect(self.screen, input_color, self.input_rect, border_radius=5)

        # Optional: Add a border
        pygame.draw.rect(self.screen, (100, 100, 255) if self.input_active else (160, 160, 160), self.input_rect, width=2, border_radius=5)
        input_surface = self.font.render(self.input_text, True, (0, 0, 0))
        self.screen.blit(input_surface, (self.input_rect.x + 10, self.input_rect.y + 10))

        # Display submitted responses
        y_offset = self.input_rect.bottom + 20
        for key, val in self.responses.items():
            entry = f"{key}: {val}"
            response_surface = self.font.render(entry, True, (0, 0, 0))
            self.screen.blit(response_surface, (modal_rect.x + 20, y_offset))
            y_offset += 30

    def get_dropdown_option_rects(self):
        rects = []
        option_height = self.dropdown_rect.height
        for i in range(len(self.dropdown_options)):
            r = pygame.Rect(
                self.dropdown_rect.x,
                self.dropdown_rect.bottom + i * option_height,
                self.dropdown_rect.width,
                option_height
            )
            rects.append(r)
        return rects

