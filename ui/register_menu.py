from modules.button import Button
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.states import States
from modules.input import Inputbox
from modules.colors import *
import pygame as pg
import sys


def draw_register_menu(root: pg.Surface, state_handler: State_handler, test_handler: Test_handler):

    button = Button(
        pg.Rect(200, 250, 200, 50),
        root,
        "Start Test",
        main_green,
        hover_green,
    )
    name_input = Inputbox(
        pg.Rect(50, 100, 500, 100),
        root,
        clicked_green,
        main_green,
        (255, 255, 255),
        "enter your name surname",
        30,
        30,
    )
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            button.handle(event, button.rect)
            name_input.handle(event)
            if name_input.text != "" and button.clicked:
                running = False

            elif name_input.text == "" and button.clicked:
                name_input.invalid_input_error()

        root.fill(dark_green_background)
        button.draw()
        name_input.draw()
        pg.display.update()
    test_handler.student_name_surname = name_input.get()
    state_handler.change_state(States.TEST)
