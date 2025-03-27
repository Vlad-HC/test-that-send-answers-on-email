from modules.button import Button
from modules.input import InputLabel
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.states import States
from modules.colors import *
import pygame as pg
import sys


def draw_test_menu(
    root: pg.Surface, state_handler: State_handler, test_handler: Test_handler
):

    print(test_handler.student_name_surname)
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        root.fill((0, 0, 0))
        pg.display.update()

    state_handler.change_state(States.FINISHED_TEST)
