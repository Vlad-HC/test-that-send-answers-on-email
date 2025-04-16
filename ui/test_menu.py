from modules.button import Button
from modules.input import Inputbox
from modules.load_system import load
from modules.textbox import Textbox
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.answers_group import Answers_group
from modules.states import States
from modules.colors import *
import pygame as pg
import sys

q, ans = load()
ind = 0

def draw_test_menu(
    root: pg.Surface, state_handler: State_handler, test_handler: Test_handler
):
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
        q[ind],
        (0, 20),
        max_width=500,
        font_color=(255, 255, 255),
        backgroud_color=clicked_green,
    )
    answer_group = Answers_group(
        ans[ind],
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
            nextbtn.handle(event,nextbtn.rect)
            previousbtn.handle(event,nextbtn.rect)
            if nextbtn.clicked:
                ind =+ 1

            if previousbtn.clicked:
                ind =- 1
            
        root.fill(dark_green_background)
        textbox.draw(root)
        answer_group.draw(root)
        nextbtn.draw()
        previousbtn.draw()

        pg.display.update()
