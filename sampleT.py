class SampleTechniqueModel:
    def __init__(self):
        self.techniques = ["SRS", "SYS", "STRATIFIED", "CLUSTER"]
        self.selected_technique = None
        self.locked = False  # Becomes True once sampling begins
        self.population = []
        self.sample_size = 0
        self.sample_list = []

    def select_technique(self, technique):
        if not self.locked and technique in self.techniques:
            self.selected_technique = technique
            self.sample_list = []  # clear any prior records

    def lock(self):
        self.locked = True

    def reset(self):
        self.selected_technique = None
        self.locked = False
        self.sample_size = 0
        self.sample_list = []

    def get_current_technique(self):
        return self.selected_technique
    
    def set_population(self, population):
        """Initialize or reset the population."""
        self.population = population

    def set_sample_size(self, size):
        """Set the sample size."""
        self.sample_size = size

    def record_spin(self, spoke_number):
    # Call this after each wheel spin stops.
    # `spoke_number` should map directly to an index or ID in the population.
    # Returns:
    #     True if sampling is complete (sample_list length == sample_size), else False.

    # Only record if SRS is the chosen technique

        if self.selected_technique != "SRS":
            return False
        # Map spoke_number to population ID (assumes 1-to-1 mapping)
        try:
            member_id = self.population[spoke_number - 1]
        except (IndexError, TypeError):
            # Invalid spoke index
            print("Invalid spoke number or population not set.")
            return False
        if len(self.sample_list) < self.sample_size:
            # Append to the sample list
            self.sample_list.append(member_id)
            # Check if we've reached the desired sample size
        return True if len(self.sample_list) == self.sample_size else False
    
    def get_sample(self):
        """Return the current sample."""
        return self.sample_list
    


    