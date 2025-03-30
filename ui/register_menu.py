from modules.button import Button
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.states import States
from modules.input import Inputbox
from modules.colors import *
import pygame as pg
import sys


def draw_register_menu(
    root: pg.Surface, state_handler: State_handler, test_handler: Test_handler
):

    button = Button(
        pg.Rect(200, 250, 200, 50),
        root,
        "Start Test",
        main_green,
        hover_green,
        clicked_green,
    )
    input_label = Inputbox(
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

            input_label.handle_input(event)
            if input_label.text != "" and button.is_clicked(event):
                running = False

            elif input_label.text == "" and button.is_clicked(event):
                input_label.invalid_input_error()

        root.fill(dark_green_background)
        button.draw()
        input_label.draw()
        pg.display.update()
    test_handler.student_name_surname = input_label.get_text()
    state_handler.change_state(States.TEST)
