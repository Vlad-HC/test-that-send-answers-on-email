from modules.states import States


class State_handler:
    def __init__(self, deafault_state: States):
        self.current_state = deafault_state

    def change_state(self, new_state: States):
        self.current_state = new_state
