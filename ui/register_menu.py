from modules.button import Button
from modules.input import InputLabel
import pygame as pg
import sys


def draw_register_menu(root: pg.Surface):
    main_green = (116, 128, 43)
    hover_green = (150, 166, 56)
    clicked_green = (160, 176, 69)
    button = Button(
        pg.Rect(50, 50, 200, 50),
        root,
        "Start Test",
        main_green,
        hover_green,
        clicked_green,
    )
    name_label = InputLabel(
        pg.Rect(100, 100, 100, 100),
        root,
        main_green,
        clicked_green,
        (0, 0, 0),
        "enter your name",
    )

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if button.is_pressed(event):
                print("pressed")

            if button.is_clicked(event):
                print("clicked")

        root.fill((22, 23, 14))
        button.draw()
        name_label.draw()
        pg.display.update()
