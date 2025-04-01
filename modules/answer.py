import pygame as pg
from modules.textbox import Textbox
from modules.colors import *


class Answer:
    def __init__(
        self,
        answer_str: str,
        pos: tuple[int, int],
        max_width: int,
        number: int = None,
    ):
        self.background_color = hover_green
        self.answer_str = answer_str
        self.pos = pos
        self.active = False
        self.max_width = max_width
        self.number = number
        self.textbox = Textbox(
            self.answer_str,
            self.pos,
            self.max_width,
            backgroud_color=self.background_color,
        )
        self.rect = self.textbox.rect
        if self.number != None:
            self.textbox.text = f"{self.number}. {self.textbox.text}"
            print(self.textbox.text)

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                return True
        return False

    def draw(self, root: pg.Surface):
        self.background_color = light_green_clicked if self.active else hover_green
        self.textbox.background_color = self.background_color
        self.textbox.draw(root)

    def __str__(self):
        return f"{self.number}. {self.answer_str} \n {self.active}"
