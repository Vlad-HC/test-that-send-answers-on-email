import pygame as pg


class UIElement:
    def __init__(self):
        self.hovered = False
        self.clicked = False
        self.pressed = False

    def is_clicked(self, event, rect: pg.Rect):
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and rect.collidepoint(event.pos):
                return True
        return False

    def is_pressed(self, event, rect: pg.Rect):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and rect.collidepoint(event.pos):
                return True
        return False

    def is_hovered(self, rect: pg.Rect):
        mousePos = pg.mouse.get_pos()

        if rect.collidepoint(mousePos):
            return True
        else:
            return False

    def handle(self, event, rect: pg.Rect):
        self.clicked = self.is_clicked(event, rect)
        self.pressed = self.is_pressed(event, rect)
        self.hovered = self.is_hovered(rect)
