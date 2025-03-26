import pygame as pg
from modules.states import States
from ui.register_menu import  draw_register_menu
import sys

pg.init()

WIDTH, HEIGHT = 600, 600

ROOT = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("TEST")

fpslock = 60

clock = pg.time.Clock()

current_state = States.REGISTER_MENU
while True:
    clock.tick(fpslock)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if current_state == States.REGISTER_MENU:
        draw_register_menu(ROOT)

    if current_state == States.TEST:
        ...

    if current_state == States.FINISHED_TEST:
        ...

    
