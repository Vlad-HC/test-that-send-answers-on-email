import pygame as pg
from pygame import Rect, Surface


class Button:

    def __init__(
        self,
        rect: Rect,
        surface: Surface,
        text: str,
        color: tuple[int, int, int],
        hover_color: tuple[int, int, int],
        clicked_color: tuple[int, int, int],
        font_size=None,
    ):
        self.rect = rect
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.rect.size[0]
        self.height = self.rect.size[1]
        self.root = surface
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.font_size = font_size if font_size is not None else self.height // 2
        self.FONT = pg.font.SysFont("comicsans", self.font_size)
    def draw(self):
        mousePos = pg.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            pg.draw.rect(self.root, self.hover_color, self.rect)

        else:
            pg.draw.rect(self.root, self.color, self.rect)

        text_surface = self.FONT.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )
        self.root.blit(text_surface, text_rect)

    def is_pressed(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                # print(self, "pressed")
                return True
        return False

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                # print(self, "clicked")
                return True
        return False

    def onclick(self, event, action, action_value):
        if self.is_clicked(event):
            action(action_value)
