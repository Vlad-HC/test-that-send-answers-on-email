from modules.button import Button
from modules.input import Inputbox
from modules.textbox import Textbox
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.states import States
from modules.colors import *
import pygame as pg
import sys


def draw_test_menu(
    root: pg.Surface, state_handler: State_handler, test_handler: Test_handler
):
    textbox = Textbox(
        "How many chromosomes do you have? How many chromosomes do you have? How many chromosomes do you have? ",
        (0, 20),
        max_width=500,
        font_color=(255, 255, 255),
        backgroud_color=clicked_green,
    )

    print(test_handler.student_name_surname)
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        root.fill(dark_green_background)
        textbox.draw(root)
        pg.display.update()
