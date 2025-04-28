import pygame as pg
from modules.textbox import Textbox
from modules.UIElement import UIElement

from modules.colors import *


class Answer(UIElement):

    def __init__(
        self,
        root: pg.Surface,
        answer_str: str,
        pos: tuple[
            int,
            int,
        ],
        max_width: int,
        number: int = None,
    ):
        super().__init__()
        self.root = root
        self.background_color = hover_green
        self.answer_str = answer_str
        self.pos = pos
        self.active = False
        self.max_width = max_width
        self.number = number
        self.textbox = Textbox(
            self.root,
            self.answer_str,
            self.pos,
            self.max_width,
            backgroud_color=self.background_color,
        )
        self.rect = self.textbox.rect
        if self.number != None:
            self.textbox.text = f"{self.number}. {self.textbox.text}"

    def __str__(
        self,
    ):
        return f"{self.number}. {self.answer_str} \n {self.active}"

    def draw(
        self,
    ):
        self.background_color = light_green_clicked if self.active else self.background_color
        self.textbox.background_color = self.background_color
        # self.textbox.draw()
