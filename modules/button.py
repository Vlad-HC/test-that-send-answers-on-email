import pygame as pg
from pygame import Rect, Surface
from modules.UIElement import UIElement


class Button(UIElement):

    def __init__(
        self,
        rect: Rect,
        surface: Surface,
        text: str,
        main_color: tuple[int, int, int],
        hover_color: tuple[int, int, int],
        font_size=None,
    ):
        super().__init__()
        self.rect = rect
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.rect.size[0]
        self.height = self.rect.size[1]
        self.root = surface
        self.text = text
        self.background_color = main_color
        self.main_color = main_color
        self.hover_color = hover_color
        self.font_size = font_size if font_size is not None else self.height // 2
        self.FONT = pg.font.SysFont("comicsans", self.font_size)

    def draw(self):
        if self.is_hovered(self.rect):
            self.background_color = self.hover_color

        else:
            self.background_color = self.main_color

        pg.draw.rect(self.root, self.background_color, self.rect)

        text_surface = self.FONT.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )
        self.root.blit(text_surface, text_rect)

    def onclick(self, action, action_value):
        if self.clicked:
            action(action_value)
