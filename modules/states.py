from enum import Enum, auto


class States(Enum):
    REGISTER_MENU = auto()
    TEST = auto()
    CONFIRMATION = auto()
    FINISHED_TEST = auto()
