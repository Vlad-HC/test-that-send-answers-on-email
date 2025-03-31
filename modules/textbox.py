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
        text_padding: int = 20,
        line_space: int = 30,
        border_r: int = 0,
    ):
        self.line_space = line_space
        self.text = text
        self.border_r = border_r
        self.font_color = font_color
        self.max_width = max_width
        self.text_padding = text_padding
        self.background_color = backgroud_color
        self.font_size = font_size
        self.FONT = pg.font.SysFont("comicsans", self.font_size)
        self.text_r = self.FONT.render(text, True, self.font_color)
        self.rect = self.text_r.get_rect()
        self.rect.width = self.max_width + self.text_padding
        self.rect.height += self.text_padding
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.height = self.rect.height

    def wrap_text(self):
        words = self.text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            text_width, _ = self.FONT.size(test_line)

            if text_width > self.max_width:
                lines.append(current_line.strip())
                current_line = word + " "
            else:
                current_line = test_line

        lines.append(current_line.strip())
        return lines

    def draw(self, root: pg.Surface):

        if self.background_color != None:
            self.background = pg.draw.rect(
                root, self.background_color, self.rect, border_radius=self.border_r
            )

        self.rect.centerx = root.get_width() // 2

        lines = self.wrap_text()
        for i, line in enumerate(lines):
            text_surface = self.FONT.render(line, True, self.font_color)

            root.blit(
                text_surface,
                (
                    self.rect.x + (self.text_padding // 2),
                    self.rect.y + (self.text_padding // 2) + i * self.line_space,
                ),
            )
        self.rect.height = self.height + self.line_space * i
