from modules.button import Button
from modules.input import Inputbox
from modules.textbox import Textbox
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.answers_group import Answers_group
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
    answer_group = Answers_group(
        [
            "111sdjkfhsdkjhfj skdhfjksdhfjksdhfjksdh111 sdjkfhsdkj hfjskdhfj ksdhfjksdhfj ksdh111sd jkfhsdkjh fjskdhfjksdhfjksdhfjksdh 11 1sdj kfhsd kjhfjskdhfjksdhfjksdhfjksdh111s",
            "222",
            "333",
        ],
        (0, 300),
        500,
    )

    print(test_handler.student_name_surname)
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            answer_group.handle_answers(event)
        root.fill(dark_green_background)
        textbox.draw(root)
        answer_group.draw(root)
        pg.display.update()
