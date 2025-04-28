import pygame as pg
from modules.textbox import Textbox
from modules.states import States
from modules.button import Button
from modules.UIElement import UIElement
from modules.colors import *


class ConfirmationDialog(UIElement):
    def __init__(
        self,
        rect: pg.Rect,
        root: pg.Surface,
        text: str,
    ):
        super().__init__()
        self.rect = rect
        self.root = root
        self.text = text

        self.txtbox = Textbox(
            self.root,
            self.text,
            (self.rect.x + 50, self.rect.y + 50),
            300,
            backgroud_color=black,
            font_color=(255, 0, 0),
        )
        self.nobtn = Button(
            pg.Rect(self.rect.bottomleft[0] + 5, self.rect.bottomleft[1] - 55, 100, 50),
            self.root,
            "No",
            main_green,
            hover_green,
        )
        self.yesbtn = Button(
            pg.Rect(self.rect.bottomright[0] - 105, self.rect.bottomright[1] - 55, 100, 50),
            self.root,
            "Yes",
            main_green,
            hover_green,
        )

    def draw(self):
        bg = pg.draw.rect(self.root, black, rect=self.rect)
        # bg_surface = pg.Surface()
