# Model | Data Processing
from sample import SampleModel
from rightpanel import RightPanel

class SampleController:
    def __init__(self, sample_size):
        self.Sample = SampleModel()
        self.SamplePanel = RightPanel()
        self.sample_size = sample_size
        self.sample = []
        self.spins_done = 0
        self.ready_to_compare = False
        self.population = []

    def draw_samp(self):
        # Mock shapes for population going to model or controller
        if len(self.sample) > 0:
            self.SamplePanel.scrollable_panel(self.sample)


    def set_sample(self, sample):
        self.Sample.add_user_sample(sample)
        self.sample = sample
    
    def record_user_spin(self, selected_value):
        if self.spins_done < self.expected_sample_size:
            self.Sample.add_user_sample(selected_value)
            self.spins_done += 1

        if self.spins_done == self.expected_sample_size:
            self.Sample.generate_system_sample(self.expected_sample_size)
            self.ready_to_compare = True

    def render(self, screen):
        user_sample, system_sample = self.SamplePanel.get_samples()
        self.SamplePanel.draw_samples(screen, user_sample, system_sample)

        if self.ready_to_compare:
            result, score_user, score_sys = self.SamplePanel.compare_samples()
            self.SamplePanel.draw_result(screen, f"{result} ({score_user} vs {score_sys})")

    def reset_sampling(self):
        self.spins_done = 0
        self.ready_to_compare = False
        self.Sample.clear_samples()

    def handle_event(self, event, pop):
        # 1) Pass to the view to catch go‑click
        self.SamplePanel.handle_event(event)

        # 2) If Go‑Against was clicked, do the compare
        if not self.SamplePanel.go_btn_clickable:
            # self.SamplePanel.go_btn_clickable = False
            self._run_go_sequence(pop)
    
    def draw_winner(self):
            self.SamplePanel.font.render(self.SamplePanel.label, True, (0, 0, 0))
            self.SamplePanel.screen.blit(self.SamplePanel.label, self.SamplePanel.pos)

    def _run_go_sequence(self, pop): 
        # Ensure user sample is complete
        user_sample = self.sample
        # if len(user_sample) < self.sample_size:
        #     print("Finish your sample first!")
        #     return

        # # 1) Machine draws its sample
        self.Sample.generate_system_sample(self.sample_size, pop)

        # 2) Compare
        winner, u_score, m_score = self.Sample.compare_samples()
        # 3) Display on screen
        self.SamplePanel.draw_result(f"{winner} wins ({u_score} vs {m_score})")
        print(f"{winner} wins ({u_score} vs {m_score})")
        # 4) Reset all MVC pieces after a short delay (or immediately)
        self.reset_sampling()
        # self.panel.reset_buttons()   # also resets result_text if you like