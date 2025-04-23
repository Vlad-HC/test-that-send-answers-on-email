import pygame as pg
from pygame import Rect, Surface
import string


class Inputbox:
    cursor_pos: int

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
        super().__init__()
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
        self.placeholder_font_color = (115, 115, 115)
        self.maxchars = maxchars
        self.text = ""
        self.cursor_pos = 0
        Inputbox.cursor_bar = pg.cursors.compile(pg.cursors.textmarker_strings)

    def get_display_text(self):
        return self.placeholder if self.showing_placeholder else self.text

    def draw(self):
        color = self.active_box_color if self.active else self.inactive_box_color

        text_color = self.placeholder_font_color if self.showing_placeholder else self.font_color

        pg.draw.rect(self.root, color, self.rect, 5)

        text_surface = self.FONT.render(self.get_display_text(), True, text_color)
        text_rect = text_surface.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )

        if self.width < text_rect.width + 20:
            self.rect.width = text_rect.width + 20
            self.rect.x = text_rect.x - 10
        else:
            self.rect.width = self.width
            self.rect.x = self.x

        self.root.blit(text_surface, text_rect)

        if self.active:

            t = self.get_display_text()[: self.cursor_pos]
            txt = self.FONT.render(
                t,
                True,
                (self.placeholder_font_color if self.showing_placeholder else self.font_color),
            )

            pg.draw.rect(
                self.root,
                (255, 255, 255),
                pg.Rect(
                    text_rect.x + txt.get_width(),
                    text_rect.y,
                    3,
                    self.FONT.get_linesize(),
                ),
            )

    def handle(self, event):
        pg.key.set_repeat(400, 50)
        valid_chars = string.ascii_letters + string.digits + string.punctuation + " "

        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.active = True
                if self.showing_placeholder:
                    self.text = ""
                    self.showing_placeholder = False
            else:
                self.active = False

        if self.active and event.type == pg.KEYDOWN:

            # LCTRL + BACKSPACE
            if event.key == pg.K_BACKSPACE and (pg.key.get_mods() & pg.KMOD_CTRL):
                if len(self.text) != 0:
                    words = str.split(self.text, " ")
                    self.cursor_pos -= len(words.pop()) + 1
                    self.text = " ".join(words)

            # BACKSPACE
            elif event.key == pg.K_BACKSPACE:
                if len(self.text) != 0 and self.cursor_pos > 0:
                    self.text = self.text[: self.cursor_pos - 1] + self.text[self.cursor_pos : :]
                    self.cursor_pos -= 1

            elif event.key == pg.K_DELETE:
                if len(self.text) != 0 and self.cursor_pos < len(self.text):
                    self.text = self.text[: self.cursor_pos] + self.text[self.cursor_pos + 1 : :]

            # TAB
            elif event.key == pg.K_TAB:
                words = str.split(self.text, " ")
                words.append("    ")
                self.text = " ".join(words)

            # ESC
            elif event.key == pg.K_ESCAPE:
                self.active = False

            elif event.key == pg.K_LEFT:
                if self.cursor_pos > 0:
                    self.cursor_pos -= 1
            elif event.key == pg.K_RIGHT:
                if self.cursor_pos < len(self.text):
                    self.cursor_pos += 1

            # all keys except keys above
            elif len(self.text) + 1 <= self.maxchars:
                if len(event.unicode) != 0 and event.unicode in valid_chars:
                    self.text = (
                        self.text[: self.cursor_pos]
                        + event.unicode
                        + self.text[self.cursor_pos : :]
                    )
                    self.cursor_pos += 1

        elif not self.active and self.text == "":
            self.showing_placeholder = True

    def get(self):
        return self.text

    def invalid_input_error(self):
        self.placeholder_font_color = (128, 0, 0)
