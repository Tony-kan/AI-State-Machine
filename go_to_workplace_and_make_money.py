
from base_state import BaseState

# inherits BaseState properties and functions
class GotoWorkplaceAndMakeMoney(BaseState):
    def __init__(self):
        super().__init__()
        self.current_location = "Work Place"
        self.agent_action = "Making Money"
        self.state_name = "GotoWorkplaceAndMakeMoney"