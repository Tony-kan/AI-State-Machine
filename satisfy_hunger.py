
from base_state import BaseState

# inherits BaseState properties and functions
class SatisfyHunger(BaseState):
    def __init__(self):
        super().__init__()
        self.current_location = "Restaurant"
        self.agent_action = "Satisfying Hunger"
        self.state_name = "SatisfyHunger"