from modules.button import Button
from modules.input import Inputbox
from modules.load_system import load
from modules.textbox import Textbox
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.answers_group import Answers_group
from modules.states import States
from modules.UIElement import UIElement
from modules.colors import *
import pygame as pg
import sys


def draw_test_menu(
    root: pg.Surface,
    state_handler: State_handler,
    test_handler: Test_handler,
):
    UIElement.clear()
    q, ans = load()
    question = q[test_handler.ind]
    answers = ans[test_handler.ind]

    nextbtn = Button(
        pg.Rect(400, 700, 160, 50),
        root,
        "NEXT",
        main_green,
        hover_green,
    )

    previousbtn = Button(
        pg.Rect(40, 700, 160, 50),
        root,
        "PREVIOUS",
        main_green,
        hover_green,
    )

    textbox = Textbox(
        root,
        question,
        (0, 20),
        max_width=500,
        font_color=(255, 255, 255),
        backgroud_color=clicked_green,
    )

    answer_group = Answers_group(
        root,
        answers,
        (0, 300),
        500,
    )

    answer_input = Inputbox(
        pg.Rect(50, 400, 500, 100),
        root,
        clicked_green,
        main_green,
        (255, 255, 255),
        "enter your answer",
        15,
        50,
    )

    if answers != None:
        UIElement.remove(answer_input)
        UIElement.add(answer_group)

    else:
        UIElement.remove(answer_group)
        UIElement.add(answer_input)

    start_time = pg.time.get_ticks()
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if answers != None:
                answer_group.handle(event)

            else:
                answer_input.handle(event)

            nextbtn.handle(event, nextbtn.rect)
            previousbtn.handle(event, previousbtn.rect)

            # buttons functionality
            if nextbtn.clicked or previousbtn.clicked:
                current_time = pg.time.get_ticks()
                time = current_time - start_time
                if UIElement.check(answer_input):
                    test_handler.save_answer(answer_input.get(), time)
                else:
                    test_handler.save_answer(answer_group.get(), time)

            if nextbtn.clicked:
                if test_handler.ind != (len(q) - 1):
                    test_handler.ind += 1
                else:
                    state_handler.change_state(States.FINISHED_TEST)
                return

            if previousbtn.clicked and test_handler.ind != 0:
                test_handler.ind -= 1
                return

        root.fill(dark_green_background)
        # textbox.draw()
        # answer_ui.draw()
        # nextbtn.draw()
        # previousbtn.draw()
        UIElement.draw_ui()

        pg.display.update()
