import pygame as pg
from pygame import Rect, Surface
import string


class Textbox:
    def __init__(
        self,
        text: str,
        pos: tuple[int, int],
        max_width: int,
        font_size: int = 20,
        font_color: tuple[int, int, int] = (0, 0, 0),
        backgroud_color: tuple[int, int, int] = None,
    ):
        self.text = text
        self.font_color = font_color
        self.max_width = max_width
        self.background_color = backgroud_color
        self.font_size = font_size
        self.FONT = pg.font.SysFont("comicsans", self.font_size)
        self.text_r = self.FONT.render(text, True, self.font_color)
        self.rect = self.text_r.get_rect()
        print(self.rect.width)
        self.rect.width = self.max_width
        print(self.rect.width)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def wrap_text(self):
        words = self.text.split()
        for word in words:
            ...

    def draw(self, root: pg.Surface):
        if self.background_color != None:
            self.background = pg.draw.rect(root, self.background_color, self.rect)

        self.rect.centerx = root.get_width() // 2
        root.blit(self.text_r, self.rect)
