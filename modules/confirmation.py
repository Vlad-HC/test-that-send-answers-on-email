import pygame as pg
from modules.textbox import Textbox
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

    def draw(self):
        bg = pg.draw.rect(self.root, main_green, rect=self.rect)
        # bg_surface = pg.Surface()
        txtbox = Textbox(self.root, self.text, (bg.x + 50, bg.y + 50), 300)
