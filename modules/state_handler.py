from modules.states import States
from modules.UIElement import UIElement


class State_handler:
    def __init__(self, deafault_state: States):
        self.current_state = deafault_state

    def change_state(self, new_state: States):
        UIElement.instances = []
        self.current_state = new_state
