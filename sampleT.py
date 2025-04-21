import random
class SampleTechniqueModel:
    def __init__(self):
        self.techniques = ["SRS", "SYS", "STRATIFIED", "CLUSTER"]
        self.selected_technique = None
        self.locked = False  # Becomes True once sampling begins
        self.population = []
        self.sample_size = 0
        self.sample_list = []
        self.sample_interval = None

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
    
    def select_nth_term(self, n):
        """
        Selects every nth term from the population, skipping index 0.
        """
        self.system_sample = [self.population[i] for i in range(1, len(self.population)) if (i + 1) % n == 0]
        return self.system_sample

    def strat(self, strata_lists):
        """
        For stratified sampling:
        - Compute group index: idx = num % len(strata_lists)
        - strata_lists is a list of lists, one per stratum
        - Return a random member from the selected stratum
        """
        strata_list = list(strata_lists.items())

        if not isinstance(strata_list, list) or not strata_list:
            print("[ERROR] strata_lists must be a non-empty list of lists.")
            return False

        if len(self.sample_list) < self.sample_size:
            member = random.choice(strata_list)
            self.sample_list.append(self.population[member[1][0]['id']])

        return len(self.sample_list) == self.sample_size
    