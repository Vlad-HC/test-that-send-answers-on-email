import pygame as pg
from pygame import Rect, Surface
import string


class InputLabel:
    def __init__(
        self,
        rect: pg.Rect,
        surface: pg.Surface,
        active_box_color: tuple[int, int, int],
        inactive_box_color: tuple[int, int, int],
        font_color: tuple[int, int, int],
        placeholder: str,
        font_size=None,
        maxchars=999,
    ):
        self.root = surface
        self.rect = rect
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.rect.width
        self.height = self.rect.height
        self.active_box_color = active_box_color
        self.inactive_box_color = inactive_box_color
        self.font_color = font_color
        self.font_size = font_size if font_size is not None else self.height // 2
        self.FONT = pg.font.SysFont("comicsans", self.font_size)
        self.active = False
        self.placeholder = placeholder
        self.showing_placeholder = True
        self.maxchars = maxchars
        self.text = ""

    def draw(self):
        color = self.active_box_color if self.active else self.inactive_box_color

        display_text = self.placeholder if self.showing_placeholder else self.text
        text_color = (115, 115, 115) if self.showing_placeholder else self.font_color

        pg.draw.rect(self.root, color, self.rect, 10)

        text_surface = self.FONT.render(display_text, True, text_color)
        text_rect = text_surface.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )
        self.root.blit(text_surface, text_rect)

    def handle_input(self, event):
        pg.key.set_repeat(400, 50)
        valid_chars = string.ascii_letters + string.digits + string.punctuation + " "

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.active = True
                # print(self, self.active)
                if self.showing_placeholder:
                    self.text = ""
                    self.showing_placeholder = False
            if event.button == 1 and not self.rect.collidepoint(event.pos):
                self.active = False
                # print(self, self.active)

        if self.active and event.type == pg.KEYDOWN:

            # LCTRL + BACKSPACE
            if event.key == pg.K_BACKSPACE and (pg.key.get_mods() & pg.KMOD_CTRL):
                if len(self.text) != 0:
                    words = str.split(self.text, " ")
                    words.pop()
                    self.text = " ".join(words)

            # BACKSPACE
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]

            # TAB
            elif event.key == pg.K_TAB:
                words = str.split(self.text, " ")
                words.append("    ")
                self.text = " ".join(words)

            # ESC
            elif event.key == pg.K_ESCAPE:
                self.active = False

            # all keys except keys above
            elif len(self.text) + 1 <= self.maxchars:
                if event.unicode in valid_chars:
                    self.text += event.unicode

        elif not self.active and self.text == "":
            self.showing_placeholder = True

    def get_text(self):
        return self.text
