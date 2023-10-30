from base_state import BaseState

# inherits BaseState properties and functions
class GoHomeAndSleepUntilRested(BaseState):
    def __init__(self):
        super().__init__()
        self.current_location = "Home"
        self.agent_action = "Sleeping until rested"
        self.state_name = "GoHomeAndSleepUntilRested"



    

