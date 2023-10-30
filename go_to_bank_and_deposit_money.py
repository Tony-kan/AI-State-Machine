
from base_state import BaseState

# inherits BaseState properties and functions
class GotoBankAndDepositMoney(BaseState):
    def __init__(self):
        super().__init__()
        self.current_location = "Bank"
        self.agent_action = "Depositing Money"
        self.state_name = "GotoBankAndDepositMoney"