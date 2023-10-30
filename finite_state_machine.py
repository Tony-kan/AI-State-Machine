from go_home_and_sleep_until_rested import GoHomeAndSleepUntilRested
from go_to_bank_and_deposit_money import GotoBankAndDepositMoney
from go_to_workplace_and_make_money import GotoWorkplaceAndMakeMoney
from satisfy_hunger import SatisfyHunger

# defines finite states and state transitions
class FiniteStateMachine:
    def __init__(self):
        self.current_state = GoHomeAndSleepUntilRested()
        self.current_state_name = self.current_state.get_state_name()
        # self.agent = Agent()


# function to change the current state to a new state
#output the transition
    def change_state(self,userInput):

        #transitions from GoHomeAndSleepUntilRested state
        if self.current_state.get_state_name() == GoHomeAndSleepUntilRested().get_state_name():
           if userInput == "1":
                self.set_current_state(GotoWorkplaceAndMakeMoney())
                print(f"\nAgent not Fatigued \nTransitioning to GotoWorkPlaceAndMakeMoney state\n")
           

        #Transitions from GotoWorkplaceAndMakeMoney state
        elif self.current_state.get_state_name() == GotoWorkplaceAndMakeMoney().get_state_name():
            if userInput == "1":
                print(f"\nAgent is hungry \nTransitioning to SatisfyHunger State\n")
                self.set_current_state(SatisfyHunger())
                
            elif userInput == "2":
                 print(f"\nAgent has made enough money \nTransitioning to GotoBankAndDepositMoney State\n")
                 self.set_current_state(GotoBankAndDepositMoney())
           

         #Transitions from GotoBankAndDepositMoney state
        elif self.current_state.get_state_name() == GotoBankAndDepositMoney().get_state_name():
            if userInput == "1":
                print(f"\nAgent is not satisfied with the amount of money in the Bank \nTransitioning to GotoWorkPlaceAndMakeMoney State\n")
                self.set_current_state(GotoWorkplaceAndMakeMoney())
                
            elif userInput == "2":
                 print(f"\nAgent is satisfied with the amount in the bank \nTransitioning to GoHomeAndSleepUntilRested State\n")
                 self.set_current_state(GoHomeAndSleepUntilRested())
            

        #Transitions from SatisfyHunger state 
        elif self.current_state.get_state_name() == SatisfyHunger().get_state_name():
            if userInput == "1":
                print(f"\nAgent is not Hungry \nTransitioning to GotoWorkPlaceAndMakeMoney State\n")
                self.set_current_state(GotoWorkplaceAndMakeMoney())
                

# functions to output and set new currentState
    def get_current_state(self):
     return self.current_state

    def set_current_state(self,new_state):
       self.current_state = new_state

#function to output current state info
    def get_current_state_and_its_info(self):
        print(f"Agent is in a {self.current_state.get_state_name()} state \nThe location is : {self.current_state.get_current_location()} \nAgent action : {self.current_state.get_agent_action()}")
       


   
        