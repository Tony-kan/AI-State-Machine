
from finite_state_machine import FiniteStateMachine
from go_home_and_sleep_until_rested import GoHomeAndSleepUntilRested
from go_to_bank_and_deposit_money import GotoBankAndDepositMoney
from go_to_workplace_and_make_money import GotoWorkplaceAndMakeMoney
from satisfy_hunger import SatisfyHunger

# trigger state change by getting imput from users
class Agent:
    def __init__(self): 
     self.fsm = FiniteStateMachine()

#start function to loop the display options until the valid option is entered
    def start(self):
       while True:
         self.transition_options(self.fsm.get_current_state().get_state_name())
         option = input("Select an option: ")
         if option == '0':
             break
         self.fsm.change_state(option)

    # agentLocationAndAction()
    def transition_options(self,state):
        if state == GoHomeAndSleepUntilRested().get_state_name():
            print("\n----------------------------------------------------------------------\n")
            self.fsm.get_current_state_and_its_info()
            print("\n  Options : ")
            print("----------------------------------------------------------------------")
            print("1.GotoWorkplaceAndMakeMoney \n0.Quit ")
            print("----------------------------------------------------------------------\n")
                             

        elif state == GotoWorkplaceAndMakeMoney().get_state_name():
            print("\n----------------------------------------------------------------------\n")
            self.fsm.get_current_state_and_its_info()
            print("\n  Options : ")
            print("----------------------------------------------------------------------")
            print("1.Satisfy Hunger \n2.GotoBankAndDepositMoney \n0.Quit ")
            print("----------------------------------------------------------------------\n")

        elif state == GotoBankAndDepositMoney().get_state_name():
            print("\n----------------------------------------------------------------------\n")
            self.fsm.get_current_state_and_its_info()
            print("\n  Options : ")
            print("----------------------------------------------------------------------")
            print("1.GotoWorkplaceAndMakeMoney \n2.GoHomeAndSleepUntilRested \n0.Quit")
            print("----------------------------------------------------------------------\n")
            

        elif state == SatisfyHunger().get_state_name():
            print("\n----------------------------------------------------------------------\n")
            self.fsm.get_current_state_and_its_info()
            print("\n  Options : ")
            print("----------------------------------------------------------------------\n")
            print("1.Gotoworkplace \n0.Quit ")
            print("----------------------------------------------------------------------\n")
           
        else:
            print("The option selected is not defined")

     

agent = Agent()
agent.start()



