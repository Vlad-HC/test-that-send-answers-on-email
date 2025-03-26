from modules.button import Button
from modules.input import InputLabel
from modules.states import States
import pygame as pg
import sys


def show_error_message(root: pg.Surface, message: str):
    font = pg.font.SysFont("comicsans", 30)
    rect = pg.Rect(150, 100, 300, 200)
    pg.draw.rect(root, (255, 0, 0), rect)

    # Render the message text
    text = font.render(message, True, (255, 255, 255))
    root.blit(text, rect)


def draw_register_menu(root: pg.Surface):
    main_green = (116, 128, 43)
    hover_green = (150, 166, 56)
    clicked_green = (160, 176, 69)
    button = Button(
        pg.Rect(200, 250, 200, 50),
        root,
        "Start Test",
        main_green,
        hover_green,
        clicked_green,
    )
    name_label = InputLabel(
        pg.Rect(50, 100, 500, 100),
        root,
        clicked_green,
        main_green,
        (255, 255, 255),
        "enter your name",
        30,
        30,
    )

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            name_label.handle_input(event)
            if name_label.text != "" and button.is_clicked(event):
                break

            elif name_label.text == "" and button.is_clicked(event):
                print("message")
                show_error_message(root, "Enter Name !")

        root.fill((22, 23, 14))
        button.draw()
        name_label.draw()
        pg.display.update()
