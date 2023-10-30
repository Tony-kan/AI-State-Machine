# defines the basic framework of all the states
class BaseState:
    def __init__(self):
        self.current_location =""
        self.agent_action =""
        self.state_name = ""

# functions to set and get location 
#  agent,stateName action in that state
    def set_current_location(self,location):
        self.current_location = location

    def get_current_location(self):
        return self.current_location

    def set_agent_action(self,agent_action):
        self.agent_action = agent_action

    def get_agent_action(self):
       return self.agent_action
    
    def set_state_name(self,state_name):
        self.state_name = state_name

    def get_state_name(self):
       return self.state_name
