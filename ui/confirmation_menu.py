from modules.confirmation import ConfirmationDialog
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from modules.UIElement import UIElement
from modules.states import States
from modules.colors import *
import pygame as pg
import sys


def draw_confirmation(
    root: pg.Surface,
    state_handler: State_handler,
    test_handler: Test_handler,
):

    conf_dialog = ConfirmationDialog(pg.Rect(100, 300, 400, 300), root, "You wanna finish test?")

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            conf_dialog.yesbtn.handle(event, conf_dialog.yesbtn.rect)
            conf_dialog.nobtn.handle(event, conf_dialog.nobtn.rect)

            if conf_dialog.yesbtn.clicked:
                state_handler.change_state(States.FINISHED_TEST)
                return

            elif conf_dialog.nobtn.clicked:
                state_handler.change_state(States.TEST)
                return

        root.fill(dark_green_background)

        UIElement.draw_ui()

        pg.display.update()
