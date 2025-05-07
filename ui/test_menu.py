from modules.button import Button
from modules.input import Inputbox
from modules.load_system import load
from modules.textbox import Textbox
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.answers_group import Answers_group
from modules.states import States
from modules.scroll_handler import scroll_handler
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

    question_counter = Textbox(
        root,
        f"{test_handler.ind + 1} / {len(q)}",
        (300, 700),
        font_color=white,
    )

    textbox = Textbox(
        root,
        question,
        (0, 20),
        max_width=500,
        font_color=white,
        backgroud_color=clicked_green,
    )
    
    if answers != None:
        UIElement.remove(answer_input)
        UIElement.add(answer_group)
        answer_group.set_previous(test_handler.get_previous_answer())

    else:
        UIElement.remove(answer_group)
        UIElement.add(answer_input)
        answer_input.text = test_handler.get_previous_answer()  # >>> need improvments

    question_counter.scrollable = False
    previousbtn.scrollable = False
    nextbtn.scrollable = False
    textbox.scrollable = False

    scroll = scroll_handler()
    scroll.add_scrollable_elems(UIElement.instances)

    clock = pg.time.Clock()
    timer = 0
    running = True
    while running:

        dt = clock.tick(60)
        timer += dt
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if answers != None:
                answer_group.handle(event)

            else:
                answer_input.handle(event)

            scroll.handle(event)
            nextbtn.handle(event, nextbtn.rect)
            previousbtn.handle(event, previousbtn.rect)

            # buttons functionality
            if nextbtn.clicked or previousbtn.clicked:
                if UIElement.check(answer_input):
                    test_handler.save_answer(answer_input.get(), timer)
                else:
                    test_handler.save_answer(answer_group.get(), timer)

                if nextbtn.clicked:
                    if test_handler.ind != (len(q) - 1):
                        test_handler.ind += 1
                    else:
                        state_handler.change_state(States.CONFIRMATION)

                if previousbtn.clicked and test_handler.ind != 0:
                    test_handler.ind -= 1

                return

        root.fill(dark_green_background)

        UIElement.draw_ui()

        pg.display.update()
