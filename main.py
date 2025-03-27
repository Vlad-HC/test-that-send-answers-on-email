import sys
import pygame as pg
from modules.states import States
from modules.state_handler import State_handler
from modules.test_handler import Test_handler
from ui.register_menu import draw_register_menu
from ui.test_menu import draw_test_menu

pg.init()
state_handler_instance = State_handler(States.REGISTER_MENU)
test_handler_instance = Test_handler()

WIDTH, HEIGHT = 600, 800

ROOT = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("TEST")

fpslock = 60

clock = pg.time.Clock()

while True:
    clock.tick(fpslock)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    current_state = state_handler_instance.current_state

    if current_state == States.REGISTER_MENU:
        draw_register_menu(ROOT, state_handler_instance, test_handler_instance)

    if current_state == States.TEST:
        draw_test_menu(ROOT, state_handler_instance, test_handler_instance)

    if current_state == States.FINISHED_TEST:
        ...
