class SampleTechniqueModel:
    def __init__(self):
        self.techniques = ["SRS", "SYS", "STRATIFIED", "CLUSTER"]
        self.selected_technique = None
        self.locked = False  # Becomes True once sampling begins

    def select_technique(self, technique):
        if not self.locked and technique in self.techniques:
            self.selected_technique = technique

    def lock(self):
        self.locked = True

    def reset(self):
        self.selected_technique = None
        self.locked = False

    def get_current_technique(self):
        return self.selected_technique